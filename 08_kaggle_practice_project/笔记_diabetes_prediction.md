# 08. Kaggle 实战项目笔记 —— 糖尿病预测（Diabetes Prediction）

数据集：[Diabetes Data Set](https://www.kaggle.com/datasets/vikasukani/diabetes-data-set)（Kaggle, vikasukani）。这是第一个完整走完"清洗 → EDA → 建模 → 调优"全流程的实战项目，之前 01~07 都是单点技能练习，这个项目的重点是把它们串成一条线，并且学会怎么给结果挑毛病、怎么迭代。整体思路是：**先看数据长什么样 -> 找数据里的坑 -> 建一个能跑的模型 -> 检查模型哪里不可信 -> 针对性修**。

## 核心概念

### 1. 用医学常识识别"伪装成 0 的缺失值"
```python
(diabetes_data == 0).sum()
```
```
Glucose          13
BloodPressure    90
SkinThickness   573
Insulin         956
BMI              28
```
`Glucose`、`BloodPressure`、`SkinThickness`、`Insulin`、`BMI` 这几列理论上不可能是 0（血压为 0 意味着人已经死了），这些 0 其实是"缺失值被记成了 0"。这个判断**不是靠统计异常值检测（z-score 那一套）**，是靠医学常识——统计方法看不出"0 合不合理"，只有懂这个字段的含义才行。`Pregnancies` 的 301 个 0 则是合理的（可以没怀孕过），所以没有处理。

**使用场景**：拿到任何真实数据集，先看每一列的取值范围是否符合这个字段本身的物理/业务含义，比 anomaly detection 更直接。

### 2. 先 `replace(0, NaN)` 再 `fillna(median)` 的顺序
```python
diabetes_data[cols] = diabetes_data[cols].replace(0, np.nan)
diabetes_data.fillna(diabetes_data.median(), inplace=True)
```
顺序不能反。必须先把非法的 0 换成 `NaN`，`median()` 才会跳过这些值去算真正有效数据的中位数；如果不替换直接算中位数，0 会被当成正常数据参与计算，把中位数拉低。

**使用场景**：任何"已知某些值是无效标记"的清洗场景，先标记为 `NaN`，再统计填补，两步不能颠倒。

### 3. seaborn EDA 套路：分布 → 分组对比 → 相关性
```python
sns.histplot(data=df, x=feature, kde=True)                          # 单变量分布
sns.boxplot(data=df, x="Outcome", y=feature, ax=ax)                 # 按结果分组对比
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")                 # 相关性矩阵
sns.pairplot(df, hue="Outcome")                                     # 两两关系 + 分类上色
```
这四步是通用套路：先看单个变量长什么样，再看这个变量在"结果不同"的两组人里是否有差异，最后看所有变量两两之间的关系。

**使用场景**：拿到任何带二分类标签的数据，做特征筛选/建模前的第一遍探索。

### 4. 逻辑回归为什么会不收敛（`ConvergenceWarning`）
梯度下降每一步的更新公式：
```
新权重 = 旧权重 - 学习步长 × 误差 × 这个特征的原始数值
```
原始数值直接乘进了更新幅度里。本项目里 `Insulin`（15~846）和 `DiabetesPedigreeFunction`（0.08~2.4）量纲差几百倍，同样的"误差 × 步长"，两个特征对应权重每一步挪动的幅度能差出上千倍——一个大步震荡、一个小步蜗行，100 次迭代内根本走不到最优点。

**使用场景**：任何基于梯度下降的模型（逻辑回归、神经网络……），遇到 `ConvergenceWarning`，先怀疑特征量纲不统一，而不是无脑加大 `max_iter`。

### 5. `StandardScaler`：`fit_transform` 训练集，`transform` 测试集
```python
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)   # 算出均值/标准差，并换算
X_test_scaled = scaler.transform(X_test)          # 只用训练集算出的均值/标准差换算，不重新算
```
`fit` 是"计算这一列的均值和标准差"，`transform` 是"拿这两个数去换算"。测试集不能重新 `fit`，否则等于让模型间接看到了测试集的分布信息（**数据泄漏**），评估出来的效果会比真实部署时更乐观、不可信。

**使用场景**：任何需要标准化/归一化的 pipeline，"统计量只能来自训练集"是铁律，PCA、归一化、异常值裁剪等都适用同一原则。

### 6. `model.coef_` 只有缩放后才能互相比较大小
缩放前，系数大小会被特征本身的数值范围"污染"：数值范围大的特征（如 `Insulin`）哪怕真实影响大，系数也会显得小；数值范围小的特征（如 `DiabetesPedigreeFunction`）系数会显得大。缩放后所有特征都是"每变化 1 个标准差"的统一单位，系数绝对值才能反映真实的相对重要性。

```python
coef_series = pd.Series(model.coef_[0], index=X.columns)
coef_series.sort_values(key=abs, ascending=False)
```
```
Glucose                     1.03
BMI                         0.56
Pregnancies                 0.44
DiabetesPedigreeFunction    0.27
Age                         0.15
Insulin                    -0.11
SkinThickness               0.03
BloodPressure              -0.01
```
排序要用 `key=abs`：系数有正有负，正负只代表方向（正相关/负相关），不代表影响力大小，直接按数值排序会把大的负数错误地排到末尾。

**使用场景**：想用线性模型的系数做"特征重要性"分析时，缩放是前提条件，不能跳过。

### 7. 为什么热力图相关系数和 `coef_` 排名对不上：共线性
热力图是"一对一"看每个变量单独跟 `Outcome` 的关系；`coef_` 是"一次性把所有变量放一起"算的。如果两个特征本身就相关（比如 `SkinThickness` 和 `BMI`），模型会发现其中一个的信息已经被另一个"代言"了，从而压低它的系数——即使这个特征单看热力图跟结果关系也不小。本项目里 `Insulin` 的系数是负的且偏小，大概率是因为跟 `Glucose` 存在相关性，信号被 `Glucose` 抢走了。

**使用场景**：解释线性模型系数时，多个高相关特征同时存在会让单个系数的解释力下降，这不是模型算错了，是特征间共线性的正常表现。

### 8. `accuracy` 在类别不平衡数据下会误导人
```
Outcome
0    1316
1     684
```
接近 2:1 不平衡。整体 `accuracy` 会被数量多的那一类主导，看着还行（0.79），但拆开看：
```python
confusion_matrix(Y_test, X_test_prediction)
classification_report(Y_test, X_test_prediction)
```
```
[[238  25]
 [ 58  79]]
              precision    recall  f1-score
0             0.80        0.90     0.85
1             0.76        0.58     0.66
```
`Outcome=1`（有糖尿病）的 recall 只有 0.58——137 个真正有病的人，模型漏诊了 58 个。医疗场景里漏诊代价远高于误诊，所以单看 accuracy 会掩盖这个真实存在的问题。

**使用场景**：任何分类任务，只要类别不是接近 1:1，都要拆开看每一类的 precision/recall，不能只信一个总的 accuracy。

### 9. `class_weight='balanced'` 的原理与代价
```python
model = LogisticRegression(class_weight='balanced')
```
训练时给数量少的那一类（`Outcome=1`）的每个错误乘上更大的惩罚权重，逼模型更重视少数类，不再一味讨好数量多的那一类。效果对比：

| | 不加权 | 加权后 |
|---|---|---|
| 有病 recall | 0.58 | 0.77 |
| 有病 precision | 0.76 | 0.63 |
| accuracy | 0.79 | 0.77 |

漏诊人数从 58 降到 32，代价是误诊人数从 25 涨到 62、整体 accuracy 略降。这是 precision-recall 的权衡：宁可多误诊（多做一次检查），也不想漏诊（真正的病人没被发现）。

**使用场景**：类别不平衡 + 漏掉少数类代价高的场景（医疗筛查、风控、故障检测），`class_weight='balanced'` 是最低成本的第一步优化，不需要额外装库。

---

## 代码模板

**1. 医学 0 值当缺失值处理**
```python
cols = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]
df[cols] = df[cols].replace(0, np.nan)
df.fillna(df.median(), inplace=True)
```
变量含义：`cols` 是"理论上不可能为 0"的字段列表，需要结合具体数据集的业务含义手动列出，不能通用。

**2. EDA 四件套**
```python
sns.histplot(data=df, x=feature, kde=True)
sns.boxplot(data=df, x=label_col, y=feature)
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
sns.pairplot(df, hue=label_col)
```

**3. 切分 + 缩放 + 训练**
```python
X = df.drop(columns=label_col)
Y = df[label_col]
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, stratify=Y, random_state=2
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression(class_weight='balanced')
model.fit(X_train_scaled, Y_train)
```
变量含义：`stratify=Y` 保证切分后训练集/测试集的类别比例跟原数据一致，不平衡数据必须加。

**4. 模型评估**
```python
pred = model.predict(X_test_scaled)
print(accuracy_score(Y_test, pred))
print(confusion_matrix(Y_test, pred))
print(classification_report(Y_test, pred))
```

---

## 常见错误

**错误 1：`plt.show` 少了括号**
```python
# 错误写法
plt.title("Correlation Heatmap")
plt.show
```
**为什么错**：`plt.show` 不加括号只是引用了这个函数对象本身，没有调用它。Jupyter 会把 cell 最后一个表达式的值打印出来，于是输出里多了一行 `<function matplotlib.pyplot.show(...)>`。因为 inline 后端本身会自动渲染 cell 里最后的图像，所以图还是能看到，但会多出这行多余输出。
```python
# 正确写法
plt.title("Correlation Heatmap")
plt.show()
```

**错误 2：改完代码没重新跑，输出还是旧的（出现了两次）**
这是整个项目里踩得最多的坑。第一次是把 `accuracy_score(X_train_prediction)` 改成两个参数后，忘了重新执行那个 cell，看到的还是修改前的 `TypeError` 报错。第二次是加完 `StandardScaler` 之后，`model.fit`、准确率计算这几个 cell 都没重跑，看到的 `ConvergenceWarning` 和准确率数字全是缩放之前的旧结果。

**为什么错**：Jupyter 的 cell 输出是"上次执行"的快照，不会因为你编辑了源代码就自动刷新。只看代码本身是否写对是不够的，必须重新执行才能确认代码和输出是同步的。

**正确做法**：改完代码后，用 "Restart Kernel and Run All" 完整重跑一遍，而不是只跑被改的那一个 cell（改的 cell 后面依赖它的 cell 也可能是旧结果）。

**错误 3：`accuracy_score` 参数顺序颠倒**
```python
# 错误写法（不报错，但语义反了）
accuracy_score(X_train_prediction, Y_train)
```
**为什么错**：`accuracy_score` 的标准签名是 `accuracy_score(y_true, y_pred)`，真实标签在前、预测值在后。因为 accuracy 只是比较两边是否相等，顺序颠倒不影响数值结果，所以这个错误不会报错、也发现不了，纯粹是习惯问题——但换成 precision/recall 这类不对称的指标，参数顺序错了结果就真的错。
```python
# 正确写法
accuracy_score(Y_train, X_train_prediction)
```

**错误 4：用没缩放的 `X_test` 喂给缩放数据训练出来的模型**
```python
# 错误写法
X_test_prediction = model.predict(X_test)   # X_test 没有经过 scaler.transform
```
**为什么错**：`model` 是拿 `X_train_scaled` 训练的，它学到的权重是针对"标准化之后的数值范围"设计的。预测时如果传进去没缩放的原始数据，两边量纲完全不匹配，预测结果不可信（虽然代码本身不会报错，因为特征数量和列名对得上，程序能跑，但结果是错的）。
```python
# 正确写法
X_test_prediction = model.predict(X_test_scaled)
```

---

## FAQ

### 为什么判断"哪些 0 是缺失值"不能用统计方法（z-score）？
z-score 这类方法是找"跟其他数据差异很大的值"，但 0 在数值上并不一定跟其他数据差异很大（比如 `Insulin` 本身波动范围就很大），统计上看未必是"异常"。真正让 0 不合理的是这个字段的**业务含义**——血压、血糖不可能是 0，这是常识判断，不是统计判断，必须结合数据代表什么去想。

### 为什么解决了 scaler 的问题，`ConvergenceWarning` 直接就消失了？
因为它们是同一个问题，不是两个独立的 bug。"不收敛"的病因就是"量纲不统一导致优化路径震荡"，`StandardScaler` 直接修复了这个病因，`ConvergenceWarning` 作为病症自然跟着消失，不是"顺手解决了另一个问题"。

### 为什么测试集不能自己重新 `fit`？
`fit` 得到的均值/标准差代表"你现在掌握的关于数据分布的全部信息"。真实部署场景里模型是没办法提前拿到未来数据、算出它的统计量的，能用的只有训练时看到的数据。如果测试集自己 `fit`，相当于让模型间接偷看了测试集的分布，评估结果会比真实场景里能达到的更乐观，这就是"数据泄漏"。

### 热力图和 `coef_` 排名不一致，是不是算错了？
不是。热力图看的是"单个变量 vs 结果"的关系，`coef_` 看的是"控制住其他所有变量之后，这个变量还剩多少独立解释力"。如果两个变量本身相关（共线性），两种视角给出的排名对不上是正常现象。

### 为什么用 `class_weight='balanced'` 而不是直接砍掉一些多数类样本？
`class_weight='balanced'` 不改变数据本身，只改变损失函数里每个错误的权重，实现简单、不需要额外的库，也不会因为删数据丢失信息。砍样本（欠采样）或者复制/合成少数类样本（过采样、SMOTE）是更激进的做法，需要额外的库（`imbalanced-learn`），也更容易在切分环节踩坑（比如采样在切分之前做，导致训练集和测试集有重复信息）。数据量不算特别大、问题不算特别极端的情况下，先用 `class_weight` 是性价比最高的第一步。

---

## 练习题

**1. 换一个分类器，对比 `coef_` 和 `feature_importances_`**
```python
from sklearn.ensemble import RandomForestClassifier
```
用 `RandomForestClassifier` 在同样的 `X_train_scaled`/`Y_train` 上训练，输出 `.feature_importances_`，跟本项目算出来的逻辑回归 `coef_` 排名对比一下，哪些特征两个模型都认为重要，哪些不一致。
**预期输出**：一个按重要性排序的特征列表，`Glucose` 大概率两边都排第一。
**考察点**：线性模型（系数）和树模型（特征重要性）对"重要性"的计算方式完全不同，树模型不需要缩放数据也能公平比较特征。

**2. 调整分类阈值而不是用 `class_weight`**
```python
probs = model.predict_proba(X_test_scaled)[:, 1]
pred_custom = (probs >= 0.3).astype(int)   # 默认阈值是 0.5，改成 0.3
```
用 `predict_proba` 拿到预测概率，手动把判定阈值从默认的 0.5 降到 0.3，重新算 `classification_report`，看 `Outcome=1` 的 recall 有没有进一步提升，precision 掉了多少。
**预期输出**：recall 比 `class_weight='balanced'` 时更高，precision 更低。
**考察点**：`class_weight` 是在训练阶段调整，调阈值是在预测阶段调整，两者都能提升 recall，但作用的环节不同，也可以叠加使用。

**3. 用 `MinMaxScaler` 替换 `StandardScaler`，观察结果差异**
```python
from sklearn.preprocessing import MinMaxScaler
```
把 `StandardScaler` 换成 `MinMaxScaler`（缩放到 0~1 区间而不是均值 0 标准差 1），重新训练，对比 `ConvergenceWarning` 是否还会出现、准确率有没有明显变化。
**预期输出**：`ConvergenceWarning` 同样会消失（因为量纲统一了），准确率跟 `StandardScaler` 版本接近但不完全一样。
**考察点**：解决量纲不统一问题不止一种缩放方法，理解每种方法数学上做了什么，而不是死记"用 StandardScaler 就对了"。

---

## 复习顺序

**必须掌握**
1. 医学常识判断 0 是不是缺失值的思路（不是统计异常值检测）
2. `replace(0, NaN)` 必须在 `fillna(median)` 之前
3. `fit_transform` 只能用训练集，`transform` 用于测试集，理解数据泄漏
4. 类别不平衡时不能只看 accuracy，要拆开看 precision/recall

**建议熟练**
1. 量纲不统一为什么会导致梯度下降不收敛（更新公式那条逻辑）
2. `model.coef_` 必须在缩放后才能互相比较
3. `class_weight='balanced'` 的原理和 precision-recall 的权衡取舍

**以后进阶**
1. 树模型的 `feature_importances_` 和线性模型系数的本质区别
2. 手动调整分类阈值（`predict_proba` + 自定义阈值）
3. 过采样/欠采样（SMOTE 等），以及为什么这些方法必须在数据切分之后做

---

## 本章检查清单

- [ ] 能说出这个数据集里哪几列的 0 是缺失值伪装的，以及为什么是靠常识而不是统计方法判断的
- [ ] 能写出"先 replace 0 为 NaN，再 fillna median"这个顺序，并说出反过来会有什么问题
- [ ] 能说出为什么量纲不统一会导致逻辑回归不收敛（能提到梯度下降更新公式）
- [ ] 能说出 `fit_transform`（训练集）和 `transform`（测试集）的区别，以及为什么测试集不能重新 fit
- [ ] 能说出为什么 `coef_` 要在缩放后才能互相比较大小
- [ ] 能解释一次"热力图相关性"和"模型系数"为什么可能对不上（共线性）
- [ ] 能说出为什么类别不平衡时 accuracy 会误导人，并且知道用 `confusion_matrix`/`classification_report` 拆开看
- [ ] 能说出 `class_weight='balanced'` 的原理，以及它带来的 precision/recall 权衡
- [ ] 能独立复述"改完代码要重新跑、不能只看代码写对了没有"这个调试习惯
