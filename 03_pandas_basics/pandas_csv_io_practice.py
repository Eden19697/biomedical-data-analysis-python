"""Pandas practice: reading and writing real CSV files.

Every exercise so far has used data typed directly into the script. Real
work starts with a file on disk. This one reads from
data/patient_vitals.csv, which sits next to this script.
"""

import pandas as pd


INPUT_PATH = "03_pandas_basics/data/patient_vitals.csv"
OUTPUT_PATH = "03_pandas_basics/data/high_priority_patients.csv"


def load_patient_vitals(path):
    """Return a DataFrame loaded from the CSV file at path.

    Task 1: pd.read_csv
    - Use pd.read_csv(path).
    - A CSV has no dtype information built in, so pandas guesses each
      column's type from its values (see main() for what it guessed here).

    Expected shape:
    (6, 5)
    """
    # TODO: replace pass
    return pd.read_csv(path)



def summarize_numeric_columns(dataframe):
    """Return summary statistics (count, mean, std, min, quartiles, max)
    for every numeric column.

    Task 2: describe
    - Use dataframe.describe().
    - This is usually the first thing you run after loading any new
      dataset, before writing a single line of analysis code.

    Expected oxygen_level row:
    count 5.0, mean 95.4, min 91.0, max 98.0
    (count is 5, not 6, because one oxygen_level value is missing)
    """
    # TODO: replace pass
    return dataframe.describe()


def save_high_priority_patients(dataframe, output_path):
    """Filter to high-priority patients and write them to a new CSV file.

    Task 3: pd.DataFrame.to_csv
    - A patient is high priority if heart_rate > 100 OR oxygen_level < 95.
    - Filter the DataFrame with that mask.
    - Save it with filtered.to_csv(output_path, index=False).
      index=False keeps pandas from writing an extra unnamed row-number
      column into the file.
    - Return the filtered DataFrame too, so main() can print it.

    Expected patient IDs written to the file:
    [102, 104]
    """
    # TODO: replace pass
    mask = (dataframe["heart_rate"] > 100) | (dataframe["oxygen_level"] < 95)
    filtered = dataframe[mask]
    filtered.to_csv(output_path, index = False)
    return filtered


def main():
    patient_vitals = load_patient_vitals(INPUT_PATH)
    print("Task 1: loaded from CSV")
    print(patient_vitals)
    print("dtypes pandas inferred from the file:")
    print(patient_vitals.dtypes)

    print("\nTask 2: summary statistics")
    print(summarize_numeric_columns(patient_vitals))

    print("\nTask 3: high-priority patients saved to CSV")
    priority = save_high_priority_patients(patient_vitals, OUTPUT_PATH)
    print(priority)
    print(f"Check that {OUTPUT_PATH} now exists and has 2 data rows plus a header.")


if __name__ == "__main__":
    main()
