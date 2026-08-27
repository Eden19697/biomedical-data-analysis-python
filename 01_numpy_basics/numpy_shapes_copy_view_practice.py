"""NumPy practice: reshape, broadcasting, and copy versus view.

The raw array contains 12 heart-rate readings: three patients, each measured
at four time points. Rows will represent patients; columns will represent time
points.

Complete one task at a time. Run this file after each task.
"""

import numpy as np


raw_readings = np.array([72, 74, 70, 73, 98, 102, 104, 100, 88, 90, 86, 89])


def readings_to_matrix(readings, patient_count=3, time_points=4):
    """Reshape one-dimensional readings into (patients, time_points).

    Task 1: reshape
    - The array has 12 values, so 3 * 4 is valid.

    Expected:
    [[ 72,  74,  70,  73],
     [ 98, 102, 104, 100],
     [ 88,  90,  86,  89]]
    """
    # TODO: replace pass
    return readings.reshape(patient_count,time_points)


def calibrate_by_time_point(matrix, offsets):
    """Add one calibration offset to each time-point column.

    Task 2: broadcasting
    - offsets has one value per column, for example [0, 1, -1, 0].
    - Add it directly to matrix; do not use a loop.

    Expected for the supplied matrix and offsets:
    [[ 72,  75,  69,  73],
     [ 98, 103, 103, 100],
     [ 88,  91,  85,  89]]
    """
    # TODO: replace pass
    return matrix + offsets


def center_each_patient(matrix):
    """Subtract each patient's own mean from every value in that patient's row.

    Task 3: axis + keepdims + broadcasting
    - Calculate one mean per row with np.mean(..., axis=1, keepdims=True).
    - Subtract the resulting column-shaped array from matrix.

    Expected:
    [[-0.25,  1.75, -2.25,  0.75],
     [-3.  ,  1.  ,  3.  , -1.  ],
     [-0.25,  1.75, -2.25,  0.75]]
    """
    # TODO: replace pass
    patient_means = np.mean(matrix, axis = 1, keepdims= True)
    #keepdims=True：不要把“列”这维完全删掉，保留成 1 列，解决下方对齐问题
    return matrix - patient_means


def change_first_value_through_view(matrix, replacement=999):
    """Change the first value of a row slice, then return matrix.

    Task 4: view
    - Assign matrix[0] to a variable named first_patient_view.
    - Change first_patient_view[0].
    - Return matrix.

    Observation: a normal NumPy slice is a view. Changing the view also changes
    the original matrix!!!
    """
    # TODO: replace pass
    first_patient_view = matrix[0]
    first_patient_view[0] = replacement
    return matrix


def change_first_value_through_copy(matrix, replacement=999):
    """Change a copied row slice, then return (matrix, copied_row).

    Task 5: copy
    - Start with matrix[0].copy().
    - Change copied_row[0].
    - Return matrix and copied_row.

    Observation: changing the copy must not change the original matrix!!!
    """
    # TODO: replace pass
    copied_row = matrix[0].copy()
    copied_row[0] = replacement
    return matrix, copied_row



def main():
    print("Task 1: reshaped readings")
    matrix = readings_to_matrix(raw_readings)
    print(matrix)
    print("Expected shape: (3, 4)")

    print("\nTask 2: calibrated readings")
    print(calibrate_by_time_point(matrix, np.array([0, 1, -1, 0])))
    print("Expected row 1: [72 75 69 73]")

    print("\nTask 3: patient-centered readings")
    print(center_each_patient(matrix))
    print("Expected first row: [-0.25  1.75 -2.25  0.75]")

    print("\nTask 4: view changes the original")
    print(change_first_value_through_view(matrix.copy()))
    print("Expected first value: 999")

    print("\nTask 5: copy preserves the original")
    original, copied_row = change_first_value_through_copy(matrix.copy())
    print("original first value:", original[0, 0])
    print("copied row first value:", copied_row[0])
    print("Expected: 72, 999")


if __name__ == "__main__":
    main()
