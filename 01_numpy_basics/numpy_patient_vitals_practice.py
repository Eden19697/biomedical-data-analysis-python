"""NumPy practice: patient vital signs.

You have six patients. Each position in patient_ids matches the same position
in heart_rates, oxygen_levels, and temperatures.

Rules for this practice:
- Import NumPy as np.
- Do not use a for loop for Tasks 2-5.
- Use NumPy array operations, boolean masks, and indexing instead.
- Run this file after every completed task.

When you finish, send the file to Codex for review.
"""

import numpy as np


patient_ids = np.array([101, 102, 103, 104, 105, 106])
heart_rates = np.array([72, 105, 88, 112, 96, 64])
oxygen_levels = np.array([98, 95, 97, 91, 99, 96])
temperatures = np.array([36.7, 37.9, 36.5, 38.2, 37.1, 36.8])


def describe_heart_rates(values):
    """Return (mean, minimum, maximum) for heart-rate values.

    Task 1:
    - Use NumPy methods or functions, not a loop.
    - Return the three values in this exact order.

    Expected for heart_rates:
    (89.5, 64, 112)
    """
    # TODO: replace pass
    average = np.mean(values)
    minimum = np.min(values)
    maximum = np.max(values)
    return average, minimum, maximum



def high_heart_rate_ids(ids, rates, threshold=100):
    """Return IDs whose heart rate is strictly greater than threshold.

    Task 2:
    - First create a boolean mask from rates.
    - Use that same mask to select the matching IDs.

    Expected for the supplied data:
    [102, 104]
    """
    # TODO: replace pass
    high_rate_mask = rates > threshold
    return ids[high_rate_mask]



def low_oxygen_ids(ids, oxygen, threshold=95):
    """Return IDs whose oxygen level is strictly less than threshold.

    Task 3:
    - This is another boolean-indexing question.

    Expected for the supplied data:
    [104]
    """
    # TODO: replace pass
    low_oxygen_mask = oxygen < threshold
    return ids[low_oxygen_mask]


def fever_ids(ids, values, threshold=37.5):
    """Return IDs whose temperature is greater than or equal to threshold.

    Task 4:
    - Use >=, because exactly 37.5 also counts as a fever here.

    Expected for the supplied data:
    [102, 104]
    """
    # TODO: replace pass
    high_temp = values >= threshold
    return ids[high_temp]


def normal_heart_rates(rates, lower=60, upper=100):
    """Return heart rates in the inclusive normal range [lower, upper].

    Task 5:
    - Create two comparisons.
    - Combine them with NumPy's element-by-element & operator.
    - Put each comparison in parentheses before using &.

    Expected for the supplied data:
    [72, 88, 96, 64]
    """
    # TODO: replace pass
    heart_rates = (rates <= upper) & (rates >= lower)
    return rates[heart_rates]


def main():
    print("Array information")
    print("heart_rates shape:", heart_rates.shape)  # Expected: (6,)
    print("heart_rates dimensions:", heart_rates.ndim)  # Expected: 1
    print("heart_rates data type:", heart_rates.dtype)

    print("\nTask 1: heart-rate summary")
    print(describe_heart_rates(heart_rates))
    print("Expected: (89.5, 64, 112)")

    print("\nTask 2: high heart-rate IDs")
    print(high_heart_rate_ids(patient_ids, heart_rates))
    print("Expected: [102 104]")

    print("\nTask 3: low oxygen IDs")
    print(low_oxygen_ids(patient_ids, oxygen_levels))
    print("Expected: [104]")

    print("\nTask 4: fever IDs")
    print(fever_ids(patient_ids, temperatures))
    print("Expected: [102 104]")

    print("\nTask 5: normal heart rates")
    print(normal_heart_rates(heart_rates))
    print("Expected: [72 88 96 64]")


if __name__ == "__main__":
    main()
