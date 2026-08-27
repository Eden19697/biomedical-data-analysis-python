"""NumPy practice: combining arrays and a first taste of linear algebra.

Part A combines separate readings and matrices, like merging two monitoring
sessions or adding a new patient/day to an existing dataset. Part B uses
matrix multiplication to compute a single weighted score from several
metrics at once, which is the same operation used inside many ML models.

Rules:
- Do not use for loops for the TODO functions.
- Use np.concatenate, np.vstack, np.hstack, and the @ operator instead.
- Complete one task at a time and run the file after each task.
"""

import numpy as np


morning_readings = np.array([72, 88, 96])
afternoon_readings = np.array([75, 90, 98])

existing_matrix = np.array(
    [
        [72, 74, 70],
        [98, 102, 104],
    ]
)
new_patient_row = np.array([80, 82, 79])
new_day_column = np.array([[75], [103]])

metrics_matrix = np.array(
    [
        [10, 5, 2],
        [20, 15, 8],
        [5, 2, 1],
        [30, 25, 15],
    ]
)
metric_weights = np.array([0.5, 0.3, 0.2])


def combine_sessions(morning, afternoon):
    """Return one array with the afternoon readings appended after morning.

    Task 1: np.concatenate
    - Combine two 1D arrays end to end.

    Expected:
    [72, 88, 96, 75, 90, 98]
    """
    # TODO: replace pass
    return np.concatenate([morning, afternoon])


def add_new_patient(matrix, new_row):
    """Return matrix with new_row appended as an additional patient (row).

    Task 2: np.vstack
    - Stack new_row underneath matrix, as a new row.
    vstack 的 v 是 vertical,表示垂直方向堆叠，也就是增加行
    Expected:
    [[ 72  74  70]
     [ 98 102 104]
     [ 80  82  79]]
    """
    # TODO: replace pass
    return np.vstack([matrix, new_row])


def add_new_day(matrix, new_column):
    """Return matrix with new_column appended as an additional day (column).

    Task 3: np.hstack
    - Stack new_column to the right of matrix, as a new column.
    - new_column already has shape (num_patients, 1), so it lines up.

    Expected:
    [[ 72  74  70  75]
     [ 98 102 104 103]]
    """
    # TODO: replace pass
    return np.hstack([matrix, new_column])


def weighted_risk_scores(matrix, weights):
    """Return one combined risk score per patient (row).

    Task 4: matrix multiplication
    - Each row of matrix holds several metrics for one patient.
    - weights holds one weight per metric, in the same order.
    - Use the @ operator: matrix @ weights.
    - This multiplies each metric by its weight and adds them together,
      all in one step, for every patient at once.

    Expected:
    [ 6.9 16.1  3.3 25.5]
    """
    # TODO: replace pass
    return matrix @ weights
    #@ 会自动对每一行做这种“乘权重后相加”的计算

def main():
    print("Task 1: combined session readings")
    print(combine_sessions(morning_readings, afternoon_readings))
    print("Expected: [72 88 96 75 90 98]")

    print("\nTask 2: matrix with new patient")
    print(add_new_patient(existing_matrix, new_patient_row))
    print("Expected:\n[[ 72  74  70]\n [ 98 102 104]\n [ 80  82  79]]")

    print("\nTask 3: matrix with new day")
    print(add_new_day(existing_matrix, new_day_column))
    print("Expected:\n[[ 72  74  70  75]\n [ 98 102 104 103]]")

    print("\nTask 4: weighted risk scores")
    print(weighted_risk_scores(metrics_matrix, metric_weights))
    print("Expected: [ 6.9 16.1  3.3 25.5]")


if __name__ == "__main__":
    main()
