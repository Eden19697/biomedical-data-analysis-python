"""Pandas practice: first-look statistics and correlation.

This is the standard first move on any new dataset, before writing a
single line of analysis: look at the summary statistics, then check
which variables move together. A strong correlation between two columns
can mean one is redundant, or it can mean you found something real —
either way, you need to know it's there before you build anything on
top of the data.
"""

import pandas as pd


patients = pd.DataFrame(
    {
        "patient_id": [101, 102, 103, 104, 105, 106, 107, 108],
        "activity_score": [20, 65, 30, 90, 45, 15, 70, 50],
        "heart_rate": [65, 98, 72, 115, 83, 60, 102, 88],
        "oxygen_level": [97, 94, 98, 96, 95, 99, 93, 97],
        "temperature": [36.9, 36.6, 37.1, 36.8, 37.2, 36.7, 36.5, 37.0],
    }
)

numeric_columns = ["activity_score", "heart_rate", "oxygen_level", "temperature"]


def overview_statistics(dataframe):
    """Return summary statistics for the numeric columns.

    Task 1: describe
    - Use dataframe[numeric_columns].describe().

    Expected activity_score row:
    count 8.0, mean 48.125, std ~26.04, min 15.0, max 90.0
    """
    # TODO: replace pass
    return dataframe[numeric_columns].describe()


def correlation_matrix(dataframe):
    """Return the correlation matrix for the numeric columns.

    Task 2: corr
    - Use dataframe[numeric_columns].corr().
    - Every column is perfectly correlated with itself, so the diagonal
      of the result will be all 1.0 — that's expected, not a bug.

    Expected activity_score/heart_rate correlation:
    about 0.999 (near-perfect — this dataset was built so higher
    activity means a higher heart rate almost every time)
    """
    # TODO: replace pass
    return dataframe[numeric_columns].corr()


def most_correlated_with(corr_matrix, column):
    """Return the (other_column, correlation) pair most strongly linked to column.

    Task 3: real logic, no single method does this
    - corr_matrix[column] gives one column's correlation with every column,
      including itself (always exactly 1.0 — you must exclude that entry,
      or it will always "win").
    - Use .drop(column) to remove the self-correlation entry.
    - Correlation can be strongly negative (near -1) and that counts as
      "strongly linked" too, so compare by .abs() before picking the max.
    - Use .idxmax() on the absolute values to get the column name with
      the largest magnitude, then look up its original (signed) value.
    - Return a tuple: (that_column_name, that_correlation_value).

    Expected for column="heart_rate":
    ("activity_score", a value near 0.999)

    Expected for column="temperature":
    ("oxygen_level", a value near 0.416 — much weaker than heart_rate's
    link to activity_score, which is the point: not every pair matters
    equally)
    """
    # TODO: replace pass
    corr = corr_matrix[column].drop(column)
    abs_corr = corr.abs()
    best = abs_corr.idxmax()
    return best, corr[best]
  #idxmax() 返回最大值所在的 index（标签）。


def main():
    print("Task 1: overview statistics")
    print(overview_statistics(patients))

    print("\nTask 2: correlation matrix")
    corr_matrix = correlation_matrix(patients)
    print(corr_matrix)

    print("\nTask 3: strongest link to heart_rate")
    print(most_correlated_with(corr_matrix, "heart_rate"))
    print("Expected column: activity_score, value near 0.999")

    print("\nTask 3b: strongest link to temperature")
    print(most_correlated_with(corr_matrix, "temperature"))
    print("Expected column: oxygen_level, value near 0.416")


if __name__ == "__main__":
    main()
