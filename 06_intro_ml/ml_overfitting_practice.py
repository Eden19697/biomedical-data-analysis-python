"""ML: overfitting, or why train accuracy alone can lie to you.

Back in ml_risk_classifier_practice.py, Task 3 explained why you never
test a model on the same rows it trained on. This file lets you see
exactly what happens if you check anyway: you compute accuracy on the
training set itself, not just the test set, and compare the two.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


INPUT_PATH = "06_intro_ml/data/labeled_patients.csv"
FEATURE_COLUMNS = ["heart_rate", "oxygen_level", "temperature"]


def load_and_split():
    data = pd.read_csv(INPUT_PATH)
    X = data[FEATURE_COLUMNS]
    y = data["risk_category"]
    return train_test_split(X, y, test_size=0.2, random_state=42)


def train_test_accuracy(model, X_train, y_train, X_test, y_test):
    """Return (train_accuracy, test_accuracy) for an already-fitted model.

    Task 1
    - Run model.predict on X_train and separately on X_test.
    - Compare each set of predictions to its own true labels
      (y_train vs predictions-on-X_train, y_test vs predictions-on-X_test).
    - Return both accuracy numbers as a tuple, train first.

    Expected, for a DecisionTreeClassifier(random_state=42) with no
    depth limit, trained on this data:
    (1.0, 0.8333333333333334)
    """
    # TODO: replace pass
    predictionA = model.predict(X_train)
    predictionB = model.predict(X_test)
    return (accuracy_score(y_train, predictionA),accuracy_score(y_test, predictionB))


def train_shallow_tree(X_train, y_train, max_depth):
    """Return a DecisionTreeClassifier trained with a depth limit.

    Task 2: max_depth — limiting how many yes/no questions the tree
    is allowed to ask before it must commit to an answer
    - model = DecisionTreeClassifier(random_state=42, max_depth=max_depth)
    - Fit it, same as always.

    A tree with no depth limit (what you used in every ML file so far)
    can keep splitting until every single training row is perfectly
    separated — including any noise or one-off quirks specific to those
    48 rows that won't generalize to a new patient. That's exactly what
    produced the 1.0 training accuracy in Task 1: not genuine
    understanding, closer to memorization. A depth limit forces the tree
    to stop early and settle for more general, less hyper-specific rules.
    """
    # TODO: replace pass
    model = DecisionTreeClassifier(random_state=42, max_depth=max_depth)
    model.fit(X_train, y_train)
    return model


def accuracy_by_depth(X_train, y_train, X_test, y_test, depths):
    """Return a DataFrame with train and test accuracy for each depth tried.

    Task 3 — this one has no pandas/sklearn method that does it for you;
    you have to loop over depths yourself and collect the results
    - For each value in depths: train a tree at that depth (Task 2),
      compute its train and test accuracy (Task 1), and record a row
      of (depth, train_accuracy, test_accuracy).
    - A plain for loop is the right tool here — this loop is building
      several different models, not processing rows of one array, so
      it's not the kind of loop numpy asked you to avoid.
    - Return the collected rows as a DataFrame with those three columns.

    Expected train/test accuracy pattern as depth increases:
    depth 1: both low (too simple to capture the pattern — underfitting)
    depth 2: train and test roughly equal (a good balance)
    depth 3-4: train keeps climbing, test stays flat or dips (the gap
               between them is overfitting, growing as depth grows)
    """
    # TODO: replace pass
    row = []
    for depth in depths:
        model = train_shallow_tree(X_train, y_train, max_depth=depth)
        train_acc, test_acc = train_test_accuracy(model, X_train, y_train, X_test, y_test)
        row.append({"depth": depth, "train_accuracy": train_acc, "test_accuracy": test_acc})
    return pd.DataFrame(row)


def main():
    X_train, X_test, y_train, y_test = load_and_split()

    full_tree = DecisionTreeClassifier(random_state=42)
    full_tree.fit(X_train, y_train)

    print("Task 1: train vs test accuracy, unlimited depth")
    print(train_test_accuracy(full_tree, X_train, y_train, X_test, y_test))

    print("\nTask 2: a depth-2 tree")
    shallow = train_shallow_tree(X_train, y_train, max_depth=2)
    print(train_test_accuracy(shallow, X_train, y_train, X_test, y_test))

    print("\nTask 3: accuracy across several depths")
    print(accuracy_by_depth(X_train, y_train, X_test, y_test, [1, 2, 3, 4, None]))


if __name__ == "__main__":
    main()
