# Heart Disease Prediction Practice Project

A small introductory machine-learning project using a heart-disease classification dataset. It demonstrates a reproducible binary-classification workflow with logistic regression.

> **Educational use only.** This project is for programming practice and is not a clinical model, diagnostic tool, or medical guidance.

## Project Overview

The guided notebook and the completed reference notebook use the included CSV file. They load and inspect the data, split predictors from the binary `target` label, use a reproducible stratified train/test split, train logistic regression, evaluate held-out accuracy, and predict one new example.

## Key Features

- **Data Collection and Processing:** The project involves collecting a dataset containing features related to individuals' health, such as age, sex, blood pressure, cholesterol levels, and more. Using Pandas, the collected data is cleaned, preprocessed, and transformed to ensure it is suitable for analysis. The dataset is included in the repository for easy access.

- **Feature and Label Preparation:** The notebook separates predictor columns from the `target` label and uses a stratified train/test split with a fixed random state.

- **Train-Test Split:** To evaluate the performance of the classification model, the project employs the train-test split technique. The dataset is divided into training and testing subsets, ensuring that the model is trained on a portion of the data and evaluated on unseen data. This allows for an accurate assessment of the model's predictive capabilities.

- **Classification Model:** The notebooks train one `LogisticRegression` classifier; they do not compare multiple model families.

- **Model Evaluation:** Training and held-out test accuracy are reported. The results apply only to this dataset and split and are not clinical performance claims.

## Getting Started

To run this project locally, follow these steps:

1. From the repository root, install dependencies: `pip install -r requirements.txt`
2. Launch the guided notebook: `jupyter lab 07_github_practice_project/Heart_Disease_Prediction.ipynb`
3. Run cells from top to bottom. The CSV file is stored in the same folder, so no download is required.

## Conclusion

Use this project to practice the standard classification workflow, then compare your guided-notebook work with `Heart_Disease_Prediction_solution.ipynb`.

## License

This project is covered by the repository's [MIT License](../LICENSE).

## Acknowledgements

This exercise adapts a public learning project by [MYoussef885](https://github.com/MYoussef885/Heart_Disease_Prediction).
