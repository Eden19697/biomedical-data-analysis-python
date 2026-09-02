"""Pandas practice: choose your own tool.

Every task before this one told you exactly which method to use. This
file only describes what result you need — figuring out which of the
tools you already know (boolean mask, sort_values, groupby, value_counts,
apply) fits each situation is the actual point of the exercise.

Reference, all from earlier exercises — no new syntax here:
- Keep only some rows: dataframe[dataframe["col"] > value]
- Reorder rows: dataframe.sort_values("col", ascending=False)
- One number per category: dataframe.groupby("col")["other_col"].mean()
- Count rows per category: dataframe["col"].value_counts()
- Your own row-by-row rule: dataframe.apply(your_function, axis=1)
"""

import pandas as pd


patients_full = pd.DataFrame(
    {
        "patient_id": [101, 102, 103, 104, 105, 106],
        "department": ["cardiology", "respiratory", "cardiology", "neurology", "respiratory", "cardiology"],
        "heart_rate": [72, 105, 88, 130, 96, 58],
        "temperature": [36.7, 37.9, 36.5, 39.0, 37.1, 36.8],
        "risk_category": ["normal", "urgent", "normal", "urgent", "normal", "watch"],
    }
)


def feverish_patients_by_severity(dataframe):
    """Return patients with temperature above 37.0, hottest first.

    Task 1
    - Only include patient_id and temperature columns in the result.

    Expected patient_id order:
    [104, 102, 105]
    """
    # TODO: replace pass
    hot = dataframe["temperature"] > 37.0
    hottest = dataframe[hot].sort_values(
        by="temperature",
        ascending=False)
    return hottest[["patient_id", "temperature"]].reset_index(drop=True)


def patient_count_by_department(dataframe):
    """Return how many patients belong to each department.

    Task 2

    Expected:
    cardiology     3
    respiratory    2
    neurology      1
    """
    # TODO: replace pass
    return dataframe["department"].value_counts()


def average_heart_rate_by_department(dataframe):
    """Return the average heart rate for each department.

    Task 3

    Expected:
    cardiology       72.666667
    neurology       130.000000
    respiratory     100.500000
    """
    # TODO: replace pass
    return dataframe.groupby("department")["heart_rate"].mean()

def build_summary(row):
    return f"{row['patient_id']} ({row['department']}): {row['risk_category']}"

def patient_summary_lines(dataframe):
    """Return one string per patient: "<id> (<department>): <risk_category>".

    Task 4
    - Example for patient 101: "101 (cardiology): normal".
    - There's no built-in for this exact text format — you need your own
      function that reads several columns from one row and returns a string.

    Expected, patients 101-106 in order:
    ['101 (cardiology): normal', '102 (respiratory): urgent',
     '103 (cardiology): normal', '104 (neurology): urgent',
     '105 (respiratory): normal', '106 (cardiology): watch']
    """
    # TODO: replace pass
    return dataframe.apply(build_summary, axis = 1).tolist()


def main():
    print("Task 1: feverish patients, hottest first")
    print(feverish_patients_by_severity(patients_full))

    print("\nTask 2: patients per department")
    print(patient_count_by_department(patients_full))

    print("\nTask 3: average heart rate per department")
    print(average_heart_rate_by_department(patients_full))

    print("\nTask 4: summary lines")
    print(patient_summary_lines(patients_full))


if __name__ == "__main__":
    main()
