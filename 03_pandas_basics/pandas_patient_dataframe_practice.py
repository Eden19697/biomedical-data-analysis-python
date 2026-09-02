"""Pandas practice: create and inspect a patient DataFrame.

A DataFrame is a table with named columns, similar to a spreadsheet or a CSV
file loaded into Python. This is simulated data for programming practice only.
"""

import pandas as pd


patient_data = {
    "patient_id": [101, 102, 103, 104, 105, 106],
    "department": ["cardiology", "respiratory", "cardiology", "respiratory", "neurology", "cardiology"],
    "heart_rate": [72, 105, 88, 112, 96, 64],
    "oxygen_level": [98, 95, 97, 91, None, 96],
    "temperature": [36.7, 37.9, 36.5, 38.2, 37.1, 36.8],
}


def create_patient_dataframe(data):
    """Return a DataFrame created from the supplied dictionary.

    Task 1: DataFrame creation
    - Use pd.DataFrame(data).
    - Each dictionary key becomes a column name.
    - Each same-position value becomes one patient's row.

    Expected shape:
    (6, 5)
    """
    # TODO: replace pass
    return pd.DataFrame(data)


def high_priority_patients(dataframe):
    """Return rows with heart rate above 100 OR oxygen below 95.

    Task 2: DataFrame boolean filtering
    - Build one condition from dataframe["heart_rate"].
    - Build one condition from dataframe["oxygen_level"].
    - Combine them with |, then use dataframe[combined_mask].

    Expected patient IDs:
    [102, 104]
    """
    # TODO: replace pass
    high_heart_rate_mask = dataframe["heart_rate"] > 100
    low_oxygen_mask = dataframe["oxygen_level"] < 95
    combined_mask = high_heart_rate_mask | low_oxygen_mask

    return dataframe[combined_mask]


def mean_heart_rate_by_department(dataframe):
    """Return the mean heart rate for each department.

    Task 3: groupby
    - Group by the "department" column.
    - Select "heart_rate".
    - Calculate mean().

    Expected values:
    cardiology     74.666667
    neurology      96.000000
    respiratory   108.500000
    """
    # TODO: replace pass
    return dataframe.groupby("department")["heart_rate"].mean()


def add_fever_column(dataframe, threshold=38.0):
    """Return a copied DataFrame with a True/False has_fever column.

    Task 4: add a calculated column safely
    - Start with dataframe.copy().
    - Set copied_dataframe["has_fever"] using temperature >= threshold.
    - Return the copied DataFrame.

    Expected fever patient ID:
    104
    """
    # TODO: replace pass
    data_copy = dataframe.copy()
    data_copy["has_fever"] = data_copy["temperature"] >= threshold
    return data_copy


def fill_missing_oxygen_with_median(dataframe):
    """Return a copied DataFrame with missing oxygen levels filled by its median.

    Task 5: missing data in Pandas
    - Start with dataframe.copy().
    - Calculate the oxygen_level median.
    - Use fillna(median_value) on the oxygen_level column.

    Expected oxygen levels:
    [98.0, 95.0, 97.0, 91.0, 96.0, 96.0]
    """
    # TODO: replace pass
    copied = dataframe.copy()
    median = copied["oxygen_level"].median()
    copied["oxygen_level"] = (copied["oxygen_level"].fillna(median))
    return copied


def main():
    print("Task 1: DataFrame")
    patient_dataframe = create_patient_dataframe(patient_data)
    print(patient_dataframe)
    print("Expected shape: (6, 5)")

    print("\nTask 2: high-priority patients")
    priority_patients = high_priority_patients(patient_dataframe)
    print(priority_patients[["patient_id", "heart_rate", "oxygen_level"]])
    print("Expected IDs: [102, 104]")

    print("\nTask 3: mean heart rate by department")
    print(mean_heart_rate_by_department(patient_dataframe))

    print("\nTask 4: fever column")
    fever_dataframe = add_fever_column(patient_dataframe)
    print(fever_dataframe[["patient_id", "temperature", "has_fever"]])
    print("Expected only patient 104 has_fever == True")

    print("\nTask 5: filled oxygen levels")
    filled_dataframe = fill_missing_oxygen_with_median(patient_dataframe)
    print(filled_dataframe[["patient_id", "oxygen_level"]])
    print("Expected patient 105 oxygen level: 96.0")


if __name__ == "__main__":
    main()
