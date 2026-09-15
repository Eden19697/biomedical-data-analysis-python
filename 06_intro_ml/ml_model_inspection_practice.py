"""ML review: inspect the decision tree instead of training a new model.

You already have a trained, working model. This file doesn't add any
new ML concepts — it reuses pandas skills you already have (boolean
masks, adding columns, sorting) to look inside a model you built and
answer two questions: exactly which cases did it get wrong, and which
of the three vitals did it actually rely on most?
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


INPUT_PATH = "06_intro_ml/data/labeled_patients.csv"
FEATURE_COLUMNS = ["heart_rate", "oxygen_level", "temperature"]


def build_results_table(model, X_test, y_test):
    """Return a copy of X_test with actual, predicted, and correct columns added.

    Task 1
    - Start with X_test.copy().
    - Add an "actual" column from y_test.values.
    - Add a "predicted" column from model.predict(X_test).
    - Add a "correct" column: True where actual equals predicted.

    Expected: 12 rows, 2 of them with correct == False.
    """
    # TODO: replace pass
    results = X_test.copy()
    results["actual"] = y_test.values
    #.values 把它变成一个纯粹的、按顺序排列的数组,这样赋值给 results 的新列时,才是"一行对一行"地对齐,不会因为索引对不上而出错或者错位
    results["predicted"] = model.predict(X_test)
    results["correct"] = results["actual"] == results["predicted"]
    return results




def misclassified_patients(results):
    """Return only the rows where the model's prediction was wrong.

    Task 2 — a boolean mask, same pattern you've used since your very
    first numpy exercises.

    Expected: 2 rows. Look at them once you have them — in both cases,
    is the model's guess a wild miss, or is it "off by one" (predicting
    the category right next to the correct one)? That difference matters
    a lot more in practice than the raw count of 2 wrong answers.
    """
    # TODO: replace pass
    mask = results["correct"] == False
    return results[mask]


def feature_importance_ranking(model, feature_names):
    """Return the model's feature importances, ranked highest first.

    Task 3
    - model.feature_importances_ is a plain numpy array, one number per
      feature, in the same order as feature_names — same shape idea as
      the numpy arrays you've worked with all along, not something new.
    - Build a Series from it: pd.Series(model.feature_importances_, index=feature_names).
    - Sort it descending (you've done this exact call before).

    Expected order (highest to lowest):
    oxygen_level, heart_rate, temperature

    This is worth sitting with for a second: in compute_deviation_score,
    you gave temperature the *highest* weight (x10) of the three. But the
    tree ranks it *lowest* here. That's not a contradiction — importance
    depends on how often a feature actually helps separate the training
    examples, not on the size of a coefficient in some formula. In this
    dataset, temperature rarely crosses its fever threshold at all (most
    generated values cluster tightly around normal), so the tree gets
    little practical use out of it, no matter how much it would matter
    if it did fire. oxygen_level crosses its threshold far more often,
    so the tree leans on it more. A feature can matter a lot "in theory"
    and still matter little in a specific dataset.
    """
    # TODO: replace pass
    importances = pd.Series(model.feature_importances_, index=feature_names)
    return importances.sort_values(ascending=False)
    # Model.feature_importances_ 不是一个函数,注意它后面没有括号——它是模型训练完之后自带的一个属性(attribute),存的是一份现成的数据,不需要"调用"它,直接读它的值就行。
    """三个数字加起来正好是 1(0.293+0.518+0.189=1.0),可以理解成"重要性占比"——oxygen_level 占了这次判断依据里的 51.8%,是三者中占比最大的
    具体是怎么算出来的(概念上,不用死记公式):决策树内部由一连串"是不是"的判断组成(比如"氧气是不是低于 94.5"),每一次判断都能把一堆混杂的病人(有
    normal 也有 urgent)分得更"干净"一点。feature_importances_ 统计的就是:整棵树里,用某个特征做判断这件事,总共帮树把病人分得更干净了多少——用得越多、分得越有效,这个特征的重要性数值就越高"""

def main():
    data = pd.read_csv(INPUT_PATH)
    X = data[FEATURE_COLUMNS]
    y = data["risk_category"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)

    results = build_results_table(model, X_test, y_test)
    print("Task 1: full results table")
    print(results)

    print("\nTask 2: misclassified patients")
    print(misclassified_patients(results))

    print("\nTask 3: feature importance ranking")
    print(feature_importance_ranking(model, FEATURE_COLUMNS))


if __name__ == "__main__":
    main()
