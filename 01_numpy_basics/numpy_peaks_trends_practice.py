"""NumPy practice: finding peaks, ranking patients, and trends over time.

Part A uses a patients-by-days heart-rate matrix, similar to the vitals
matrix you already practiced with. Part B uses one patient's continuous
readings to practice change-over-time and sensor-range clipping.

Rules:
- Do not use for loops for the TODO functions.
- Use NumPy functions (argmax, argmin, argsort, diff, clip) instead.
- Complete one task at a time and run the file after each task.
"""

import numpy as np


patient_ids = np.array([201, 202, 203, 204, 205])
heart_rate_matrix = np.array(
    [
        [72, 74, 70, 73],
        [98, 102, 104, 100],
        [88, 90, 86, 89],
        [110, 108, 112, 115],
        [76, 80, 78, 74],
    ]
)

continuous_readings = np.array([70, 72, 78, 95, 110, 105, 90, 80])


def patient_with_highest_average(ids, matrix):
    """Return the ID of the patient with the highest average heart rate.

    Task 1: argmax
    - Calculate each patient's average with np.mean(matrix, axis=1).
    - Use np.argmax on the averages to find the position of the highest one.
    - Use that position to index into ids.

    Expected:
    204
    """
    # TODO: replace pass
    average = np.mean(matrix, axis = 1)
    highest_average = np.argmax(average)
    return ids[highest_average]


def patient_with_lowest_average(ids, matrix):
    """Return the ID of the patient with the lowest average heart rate.

    Task 2: argmin
    - Same idea as Task 1, but with np.argmin.

    Expected:
    201
    """
    # TODO: replace pass
    average = np.mean(matrix, axis = 1)
    lowest_average = np.argmin(average)
    return ids[lowest_average]


def rank_patients_by_average(ids, matrix):
    """Return patient IDs ordered from lowest to highest average heart rate.

    Task 3: argsort
    - Calculate each patient's average.
    - Use np.argsort on the averages. It returns the positions that would
      sort the array, from smallest to largest.
    - Use those positions to reorder ids.

    Expected:
    [201, 205, 203, 202, 204]
    """
    # TODO: replace pass
    average = np.mean(matrix, axis = 1)
    sort = np.argsort(average)
    return ids[sort]


def successive_changes(readings):
    """Return the change between each reading and the one before it.

    Task 4: np.diff
    - np.diff(readings) returns an array one element shorter than readings,
      where each value is readings[i+1] - readings[i].

    Expected:
    [2, 6, 17, 15, -5, -15, -10]
    """
    # TODO: replace pass
    return np.diff(readings)


def clip_to_sensor_range(readings, lower=60, upper=100):
    """Return readings clamped to the sensor's valid range.

    Task 5: np.clip
    - Values below lower become lower.
    - Values above upper become upper.
    - Values already inside the range are unchanged.

    Expected:
    [70, 72, 78, 95, 100, 100, 90, 80]
    """
    # TODO: replace pass
    return np.clip(readings,lower,upper)
    #把超过最大或者最小的换成最大或者最小

def main():
    print("Task 1: patient with highest average")
    print(patient_with_highest_average(patient_ids, heart_rate_matrix))
    print("Expected: 204")

    print("\nTask 2: patient with lowest average")
    print(patient_with_lowest_average(patient_ids, heart_rate_matrix))
    print("Expected: 201")

    print("\nTask 3: patients ranked by average")
    print(rank_patients_by_average(patient_ids, heart_rate_matrix))
    print("Expected: [201 205 203 202 204]")

    print("\nTask 4: successive changes")
    print(successive_changes(continuous_readings))
    print("Expected: [  2   6  17  15  -5 -15 -10]")

    print("\nTask 5: clipped readings")
    print(clip_to_sensor_range(continuous_readings))
    print("Expected: [ 70  72  78  95 100 100  90  80]")


if __name__ == "__main__":
    main()
