# Biomedical Data Analysis with Python

A hands-on learning portfolio for biomedical data analysis with Python. This repository begins with NumPy-based vital-sign and patient-data exercises; later chapters will add tabular analysis, visualization, and introductory machine learning.

> **Educational use only.** The included datasets and analyses are for programming practice, not clinical use or medical decision-making.

## Available chapter

### 01 · NumPy basics

Exercises use small practice datasets to cover:

- array creation, shapes, copying, and combining signals
- loading and saving CSV, text, and NumPy files
- missing-value handling and reproducible random sampling
- vital-sign trends, peak detection, and simple risk screening

## Repository structure

```text
01_numpy_basics/
├── data/                         Practice vital-sign data
└── numpy_*_practice.py           Standalone NumPy exercises
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
```

## Notes on the data and results

The included datasets are small practice datasets or simulated patient data. They demonstrate programming techniques only and are not validated clinical tools.

## License

Released under the [MIT License](LICENSE).
