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
```

## Notes on the data and results

The included datasets are small practice datasets or simulated patient data. They demonstrate programming techniques only and are not validated clinical tools.

## License

Released under the [MIT License](LICENSE).
