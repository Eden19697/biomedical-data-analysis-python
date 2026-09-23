# Biomedical Data Analysis with Python

A hands-on learning portfolio for biomedical data analysis with Python. This repository begins with NumPy-based vital-sign and patient-data exercises; later chapters will add tabular analysis, visualization, and introductory machine learning.

> **Educational use only.** The included datasets and analyses are for programming practice, not clinical use or medical decision-making.

## Available chapters

### 01 · NumPy basics

Exercises use small practice datasets to cover:

- array creation, shapes, copying, and combining signals
- loading and saving CSV, text, and NumPy files
- missing-value handling and reproducible random sampling
- vital-sign trends, peak detection, and simple risk screening

### 02 · Python data workflows

Practice with useful standard-library tools that support data-processing work:

- paired filtering with `zip` and list comprehensions
- value positions with `enumerate`
- frequency counting and grouping with `Counter` and `defaultdict`
- FIFO queue processing with `deque`
- memory-efficient value filtering with generators

### 03 · Pandas basics

Practice table-oriented analysis with simulated patient data:

- DataFrame creation, boolean filtering, grouping, sorting, and missing-value handling
- CSV input/output, descriptive statistics, correlation, and merging
- datetime analysis, rolling windows, pivot tables, interpolation, and custom row logic

### 04 · Matplotlib basics

Practice turning vital-sign data into readable static figures:

- line charts and rolling-mean overlays
- departmental comparison bars and priority-patient scatter plots
- subplot layout and rolling variability views

### 05 · Capstone patient-vitals analysis

An end-to-end practice workflow for a small simulated patient dataset:

- CSV loading, median imputation, and z-score outlier removal
- departmental heart-rate summaries
- a histogram, department-level box plot, and annotated correlation heatmap

### 06 · Introduction to machine learning

Practice supervised classification with simulated patient-risk labels:

- feature/label separation and reproducible train/test splits
- decision-tree and logistic-regression classifiers
- held-out accuracy, misclassification review, feature importance, and overfitting comparisons

### 07 · GitHub practice project: heart-disease prediction

Apply the introductory workflow to a larger binary-classification dataset:

- guided and completed Jupyter notebooks for a logistic-regression classifier
- reproducible stratified train/test splitting and held-out accuracy checks
- local CSV input and a one-patient prediction example

### 08 · Kaggle practice project: diabetes prediction

Apply a complete binary-classification workflow to the Kaggle diabetes dataset:

- documented Kaggle dataset attribution and a local CSV copy for reproducibility
- zero-value cleaning, median imputation, exploratory analysis, and feature scaling
- class-balanced logistic regression with held-out metrics and a confusion matrix

### 09 · Regression practice project: insurance-cost prediction

Practice continuous-value prediction with an insurance-cost dataset:

- distribution and group-based exploratory analysis of medical-insurance charges
- one-hot encoding plus BMI and smoking interaction features
- linear-regression evaluation with RMSE, R², and residual diagnostics

## Repository structure

```text
01_numpy_basics/
├── data/                         Practice vital-sign data
└── numpy_*_practice.py           Standalone NumPy exercises
02_python_data_workflows/
└── python_data_idioms_practice.py  Python standard-library data workflows
03_pandas_basics/
├── data/                         Practice patient-vitals CSV files
└── pandas_*_practice.py          Standalone Pandas exercises
04_matplotlib_basics/
├── output/                       Rendered practice figures
└── matplotlib_vitals_plotting_practice.py
05_capstone_project/
├── data/                         Simulated patient-vitals CSV file
├── output/                       Rendered capstone figures
└── capstone_patient_analysis.py
06_intro_ml/
├── data/                         Simulated labeled-patient CSV file
└── ml_*_practice.py              Introductory scikit-learn exercises
07_github_practice_project/
├── heart_disease_data.csv         Local binary-classification dataset
├── Heart_Disease_Prediction.ipynb Guided practice notebook
└── Heart_Disease_Prediction_solution.ipynb  Completed reference notebook
08_kaggle_practice_project/
├── data/diabetes-dataset.csv       Kaggle dataset copy; attribution in chapter README
├── Diabetic_test.ipynb             Executable data-cleaning and classification notebook
├── README.md                       Source, attribution, and usage notes
└── 笔记_diabetes_prediction.md      Chinese review notes and exercises
09_regression_practice_project/
├── data/insurance.csv               Local medical-insurance cost dataset
└── Insurance_cost.ipynb             Executable regression workflow and diagnostics
```

## Getting started

```bash
git clone https://github.com/Eden19697/biomedical-data-analysis-python.git
cd biomedical-data-analysis-python
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run a practice file from the repository root, for example:

```bash
python 01_numpy_basics/numpy_patient_vitals_practice.py
python 02_python_data_workflows/python_data_idioms_practice.py
python 03_pandas_basics/pandas_patient_dataframe_practice.py
python 04_matplotlib_basics/matplotlib_vitals_plotting_practice.py
python 05_capstone_project/capstone_patient_analysis.py
python 06_intro_ml/ml_risk_classifier_practice.py
jupyter lab 07_github_practice_project/Heart_Disease_Prediction.ipynb
jupyter lab 08_kaggle_practice_project/Diabetic_test.ipynb
jupyter lab 09_regression_practice_project/Insurance_cost.ipynb
```

## Notes on the data and results

The included datasets are small practice datasets or simulated patient data. They demonstrate programming techniques only and are not validated clinical tools.

## License

Released under the [MIT License](LICENSE).
