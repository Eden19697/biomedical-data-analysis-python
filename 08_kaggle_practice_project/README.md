# Diabetes Prediction — Kaggle Practice Project

An educational binary-classification workflow that covers data cleaning, exploratory analysis, scaling, logistic regression, and class-imbalance evaluation.

> **Educational use only.** This project is for programming practice and must not be used for diagnosis, treatment, or other clinical decisions.

## Source and attribution

- **Dataset:** [Diabetes Data Set](https://www.kaggle.com/datasets/vikasukani/diabetes-data-set)
- **Original dataset author:** [vikasukani](https://www.kaggle.com/vikasukani) on Kaggle
- **Local copy:** `data/diabetes-dataset.csv`

The original dataset remains the property of its author and is subject to Kaggle's terms and any dataset-specific license. This repository preserves the source attribution and contains learning-oriented notebook adaptations and explanatory notes; it does not claim ownership of the source dataset.

## Contents

- `Diabetic_test.ipynb` — reproducible data-cleaning, EDA, and logistic-regression workflow
- `data/diabetes-dataset.csv` — local dataset copy used by the notebook
- `笔记_diabetes_prediction.md` — Chinese review notes and exercises

## Run locally

From the repository root:

```bash
pip install -r requirements.txt
jupyter lab 08_kaggle_practice_project/Diabetic_test.ipynb
```

Run cells from top to bottom. The notebook reads the included local CSV; no external download is needed.

## Workflow and limitations

The notebook replaces medically implausible zero values with missing values, imputes medians, visualizes distributions and relationships, scales training data only, fits a class-balanced logistic-regression model, and reports accuracy, a confusion matrix, and a classification report. Results depend on this dataset and split and are not clinical performance claims.
