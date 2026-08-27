"""NumPy practice: missing sensor readings, dtype, and safe cleaning.

np.nan represents a missing numeric value. Because np.nan is a floating-point
value, an array containing it normally has a float dtype.

This uses simulated data for programming practice, not a clinical rule.
"""

import numpy as np


oxygen_levels = np.array([98.0, np.nan, 97.0, 91.0, np.nan, 96.0])


def missing_reading_indices(values):
    """Return the indexes containing np.nan.

    Task 1: missing values
    - np.isnan(values) creates a boolean mask.
    - np.where(mask)[0] returns the indexes where that mask is True.

    Expected:
    [1, 4]
    """
    # TODO: replace pass
    missing_mask = np.isnan(values)
    return np.where(missing_mask)[0]#where把 True 全部提取出来

def fill_missing_with_mean(values):
    """Return a cleaned copy where missing values use the valid-value mean.

    Task 2: copy + nan-aware mean
    - Start with values.copy() so the original input stays unchanged.
    - Use np.nanmean, not np.mean; nanmean ignores missing values.
    - Use np.isnan(cleaned_values) as the assignment mask.

    Expected:
    [98.0, 95.5, 97.0, 91.0, 95.5, 96.0]
    """
    # TODO: replace pass
    clean_values = values.copy()
    mean_value = np.nanmean(clean_values)
    missing = np.isnan(clean_values)

    clean_values[missing] = mean_value#把 True 的位置拿出来改为均值
    return clean_values


def valid_oxygen_mask(values, minimum=95.0):
    """Return a mask for values that are present and at least minimum.

    Task 3: combine conditions
    - A missing value must be False, even though it is not below minimum.
    - Use ~np.isnan(values) for "is not missing".
    - Combine it with values >= minimum using &.

    Expected:
    [True, False, True, False, False, True]
    """
    # TODO: replace pass
    missing = ~np.isnan(values)
    over = values >= minimum
    return missing & over


def rounded_integer_readings(values):
    """Round valid float readings, then return integer values.

    Task 4: dtype conversion
    - np.rint rounds values to the nearest whole number.
    - astype(int) converts rounded float values to integer dtype.
    - Only use this after missing values have been filled.

    Expected after filling the supplied data:
    [98, 96, 97, 91, 96, 96]
    """
    # TODO: replace pass
    return np.rint(values).astype(int)


def main():
    print("Original readings:", oxygen_levels)
    print("dtype:", oxygen_levels.dtype)
    print("Expected dtype: float")

    print("\nTask 1: missing-reading indexes")
    print(missing_reading_indices(oxygen_levels))
    print("Expected: [1 4]")

    print("\nTask 2: cleaned readings")
    cleaned_levels = fill_missing_with_mean(oxygen_levels)
    print(cleaned_levels)
    print("Expected: [98.  95.5 97.  91.  95.5 96. ]")
    print("Original still has missing values:", oxygen_levels)

    print("\nTask 3: valid oxygen mask")
    print(valid_oxygen_mask(oxygen_levels))
    print("Expected: [ True False  True False False  True]")

    print("\nTask 4: rounded integer readings")
    print(rounded_integer_readings(cleaned_levels))
    print("Expected: [98 96 97 91 96 96]")


if __name__ == "__main__":
    main()
