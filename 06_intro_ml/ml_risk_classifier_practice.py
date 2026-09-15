"""Intro to ML: teach a model the rule you used to write by hand.

Back in pandas_apply_practice.py, you wrote compute_deviation_score and
categorize_score yourself — an explicit rule mapping heart_rate,
oxygen_level, and temperature to a risk_category label. This file's
60 patients were labeled with that same kind of rule, but the model you
build here is never shown the rule. It only sees examples (the vitals)
and their answers (the labels), and has to work out a similar pattern
on its own from data. That's the core idea of supervised learning.

This is simulated data for programming practice only, not a real
clinical model.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


INPUT_PATH = "06_intro_ml/data/labeled_patients.csv"
FEATURE_COLUMNS = ["heart_rate", "oxygen_level", "temperature"]


def load_labeled_data(path):
    """Return the labeled patient data as a DataFrame.

    Task 1 — you know this one already
    Expected shape:
    (60, 5)
    """
    # TODO: replace pass
    return pd.read_csv(path)


def prepare_features_and_labels(dataframe):
    """Split the data into features (X) and the label to predict (y).

    Task 2: features vs. labels — the first new idea
    - "Features" (X) are the inputs the model is allowed to look at:
      dataframe[FEATURE_COLUMNS].
    - The "label" (y) is the answer it's trying to learn to predict:
      dataframe["risk_category"].
    - Everything from here on works with X and y separately, never the
      whole DataFrame at once — the model must never see risk_category
      mixed in with its inputs, or it isn't really learning anything.
    - Return them as a tuple: (X, y).

    Expected X columns:
    ['heart_rate', 'oxygen_level', 'temperature']
    Expected y name:
    risk_category
    """
    # TODO: replace pass
    X = dataframe[FEATURE_COLUMNS]#喂给模型的输入,X(特征,features)
    y = dataframe["risk_category"]#模型要学会预测的答案,y(标签,label)
    return X, y


def split_train_test(X, y):
    """Split X and y into a training set and a held-out test set.

    Task 3: train_test_split — why you never grade a model on data it studied
    - Use train_test_split(X, y, test_size=0.2, random_state=42).
    - test_size=0.2 holds out 20% of the rows to test on later; the
      model will never see these during training.
    - random_state=42 makes the split reproducible — same idea as the
      seed you used with np.random.default_rng back in the numpy
      reproducibility exercise.
    - Why hold out data at all? If you trained and tested on the exact
      same rows, a model could just memorize the answers instead of
      learning the underlying pattern, and you'd have no way to tell
      the difference. Testing on unseen rows is the only honest check.
    - Returns four things, in this order: X_train, X_test, y_train, y_test.

    Expected sizes:
    48 training rows, 12 test rows
    """
    # TODO: replace pass
    return train_test_split(X, y, test_size= 0.2, random_state=42)


def train_classifier(X_train, y_train):
    """Return a decision tree classifier trained on the training data.

    Task 4: fit — this is the actual "learning" step
    - model = DecisionTreeClassifier(random_state=42)
    - model.fit(X_train, y_train)
    - A decision tree learns a sequence of yes/no questions about the
      features (e.g. "is oxygen_level below 94.5?") that best separate
      the training examples into their correct labels — conceptually
      not so different from the if/elif chain you wrote by hand in
      compute_deviation_score, except the tree figures out its own
      thresholds from the data instead of you specifying 95 and 37.5.
    - Return the fitted model.
    """
    # TODO: replace pass
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)
    return model


def evaluate_model(model, X_test, y_test):
    """Return the model's accuracy on the held-out test set.

    Task 5: predict + accuracy_score
    - predictions = model.predict(X_test)
    - Use accuracy_score(y_test, predictions) to compare predictions
      against the real labels — the fraction it got exactly right.

    Expected:
    0.833... (10 out of 12 test patients correctly classified)
    """
    # TODO: replace pass
    predictions = model.predict(X_test)#猜测答案"
    return accuracy_score(y_test, predictions)#accuracy_score(真实答案, 预测答案)


def predict_new_patient(model, heart_rate, oxygen_level, temperature):
    """Return the model's predicted risk_category for one new patient.

    Task 6: using a trained model on a single new case
    - scikit-learn expects a 2D table even for one row, so wrap the
      values in a one-row DataFrame first:
      row = pd.DataFrame([[heart_rate, oxygen_level, temperature]],
                          columns=FEATURE_COLUMNS)
    - model.predict(row) returns an array with one prediction in it —
      return just that single value (index [0]), not the whole array.

    Expected for heart_rate=130, oxygen_level=89, temperature=39.0
    (the same patient 104 numbers from compute_deviation_score,
    which by hand scored 57.0 -> "urgent"):
    'urgent'
    """
    # TODO: replace pass
    row = pd.DataFrame([[heart_rate, oxygen_level, temperature]], columns = FEATURE_COLUMNS)
    return model.predict(row)[0]


def main():
    data = load_labeled_data(INPUT_PATH)
    print("Task 1: loaded data")
    print(data.shape)

    X, y = prepare_features_and_labels(data)
    print("\nTask 2: features and labels separated")
    print("X columns:", list(X.columns))
    print("y name:", y.name)

    X_train, X_test, y_train, y_test = split_train_test(X, y)
    print("\nTask 3: train/test split")
    print(f"{len(X_train)} training rows, {len(X_test)} test rows")

    model = train_classifier(X_train, y_train)
    print("\nTask 4: model trained")

    accuracy = evaluate_model(model, X_test, y_test)
    print("\nTask 5: test accuracy")
    print(accuracy)

    print("\nTask 6: predicting a new, unseen patient")
    print(predict_new_patient(model, 130, 89, 39.0))
    print("Expected: urgent")


if __name__ == "__main__":
    main()
