"""ML review: the exact same recipe, a different model, fewer hints.

Same data, same six-step recipe as ml_risk_classifier_practice.py
(load -> split features/labels -> train/test split -> fit -> predict ->
accuracy). This time the model is LogisticRegression instead of
DecisionTreeClassifier, and the instructions don't spell out every line —
if you actually internalized the recipe, this should feel like typing
something you already know, not solving something new.

One thing worth noticing once you're done: this model's accuracy is not
the same number as the decision tree's. Different models can learn the
same data differently well — there's no single "the" accuracy for a
dataset, only "this model, on this data, scored this."
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


INPUT_PATH = "06_intro_ml/data/labeled_patients.csv"
FEATURE_COLUMNS = ["heart_rate", "oxygen_level", "temperature"]


def load_and_split(path):
    """Load the data and return X_train, X_test, y_train, y_test.

    Task 1 — the first three steps from last time, combined into one
    function. Same column names, same test_size and random_state as before.

    Expected sizes:
    48 training rows, 12 test rows
    """
    # TODO: replace pass
    dataframe = pd.read_csv(path)
    X = dataframe[FEATURE_COLUMNS]
    y = dataframe["risk_category"]
    return train_test_split(X, y, test_size=0.2, random_state=42)
    """train_test_split 一次性生成了四样东西:X_train, X_test, y_train, y_test
    (训练用的 X、测试用的 X、训练用的 y、测试用的 y),load_and_split 把这四个原封不动
    地返回出去。"""



def train_logistic_regression(X_train, y_train):
    """Return a LogisticRegression model trained on the training data.

    Task 2
    - model = LogisticRegression(max_iter=1000, random_state=42)
    - (max_iter=1000 just gives the model enough iterations to finish
      training without a warning — logistic regression fits by iterative
      search, unlike a decision tree, but you don't need to know the
      details yet, just that this argument exists so it converges.)
    - Same fit step as before.
    """
    # TODO: replace pass
    model = LogisticRegression(max_iter=1000, random_state=42)
    model.fit(X_train, y_train)
    return model


def evaluate(model, X_test, y_test):
    """Return this model's accuracy on the test set.

    Task 3

    Expected:
    0.75 (9 out of 12 — worse than the decision tree's 0.833. That's a
    real result, not a mistake: on this particular dataset, a decision
    tree happens to fit the pattern better than a straight-line-style
    model does.)
    """
    # TODO: replace pass
    predictions = model.predict(X_test)
    return accuracy_score(y_test, predictions)



def predict_new_patient(model, heart_rate, oxygen_level, temperature):
    """Return this model's prediction for one new patient.

    Task 4 — same idea as before, same test values.

    Expected for (130, 89, 39.0):
    'urgent'
    """
    # TODO: replace pass
    row = pd.DataFrame([[heart_rate, oxygen_level, temperature]], columns = FEATURE_COLUMNS)
    return model.predict(row)[0]

def main():
    X_train, X_test, y_train, y_test = load_and_split(INPUT_PATH)
    print("Task 1:", len(X_train), "training rows,", len(X_test), "test rows")

    model = train_logistic_regression(X_train, y_train)
    print("Task 2: model trained")

    accuracy = evaluate(model, X_test, y_test)
    print("Task 3: accuracy =", accuracy)

    print("Task 4:", predict_new_patient(model, 130, 89, 39.0))


if __name__ == "__main__":
    main()
