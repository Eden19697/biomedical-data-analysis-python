"""NumPy practice: a two-dimensional patient-vitals matrix.

Rows represent patients and columns represent three consecutive days.

             Day 1  Day 2  Day 3
Patient 201    72     74     70
Patient 202    98    102    104
Patient 203    88     90     86
Patient 204   110    108    112
Patient 205    76     80     78

Rules:
- Do not use for loops for the TODO functions.
- Use NumPy aggregation, boolean masks, and axis.
- Complete one task at a time and run the file after each task.
"""

import numpy as np


patient_ids = np.array([201, 202, 203, 204, 205])
heart_rate_matrix = np.array(
    [
        [72, 74, 70],
        [98, 102, 104],
        [88, 90, 86],
        [110, 108, 112],
        [76, 80, 78],
    ]
)


def daily_average_heart_rates(matrix):
    """Return the average heart rate for each day.

    Task 1:
    - Average down each column.
    - Use np.mean with the correct axis.

    Expected:
    [88.8, 90.8, 90.0]
    """
    # TODO: replace pass
    return np.mean(matrix, axis= 0)


def patient_average_heart_rates(matrix):
    """Return the average heart rate for each patient.

    Task 2:
    - Average across each row.
    - Use np.mean with the correct axis.

    Expected:
    [72.0, 101.333..., 88.0, 110.0, 78.0]
    """
    # TODO: replace pass
    return np.mean(matrix, axis = 1)


def high_average_heart_rate_ids(ids, matrix, threshold=100):
    """Return IDs whose three-day average is strictly greater than threshold.

    Task 3:
    - First calculate each patient's average.
    - Make a boolean mask from those averages.
    - Use the mask to select matching IDs.

    Expected:
    [202, 204]
    """
    # TODO: replace pass
    patient_averages = np.mean(matrix, axis=1)
    over_threshold = patient_averages > threshold

    return ids[over_threshold]


def patients_with_any_high_rate(ids, matrix, threshold=105):
    """Return IDs that had a rate strictly greater than threshold on any day.

    Task 4:
    - First make a True/False matrix with matrix > threshold.
    - Use np.any(..., axis=1) to reduce each patient's row to one True/False value.

    Expected:
    [204]
    """
    # TODO: replace pass
    high_rate_mask = matrix > threshold
    has_high_rate_mask = np.any(high_rate_mask, axis = 1)#if we have one true, return true
    return ids[has_high_rate_mask]


def patient_rate_ranges(matrix):
    """Return each patient's highest rate minus their lowest rate.

    Task 5:
    - Find one maximum per row.
    - Find one minimum per row.
    - Subtract the two resulting arrays.

    Expected:
    [4, 6, 4, 4, 4]
    """
    # TODO: replace pass
    highest_rates = np.max(matrix, axis = 1)
    lowest_rates = np.min(matrix, axis = 1)
    return highest_rates - lowest_rates


def main():
    print("Matrix information")
    print("shape:", heart_rate_matrix.shape)  # Expected: (5, 3)
    print("dimensions:", heart_rate_matrix.ndim)  # Expected: 2

    print("\nTask 1: daily averages")
    print(daily_average_heart_rates(heart_rate_matrix))
    print("Expected: [88.8 90.8 90. ]")

    print("\nTask 2: patient averages")
    print(patient_average_heart_rates(heart_rate_matrix))
    print("Expected: [ 72.         101.33333333  88.         110.          78.        ]")

    print("\nTask 3: high-average patient IDs")
    print(high_average_heart_rate_ids(patient_ids, heart_rate_matrix))
    print("Expected: [202 204]")

    print("\nTask 4: any high-rate patient IDs")
    print(patients_with_any_high_rate(patient_ids, heart_rate_matrix))
    print("Expected: [204]")

    print("\nTask 5: patient heart-rate ranges")
    print(patient_rate_ranges(heart_rate_matrix))
    print("Expected: [4 6 4 4 4]")


if __name__ == "__main__":
    main()
