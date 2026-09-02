"""Pandas practice: combining data from separate sources.

Real datasets are rarely one tidy table. Demographics, sensor readings, and
lab results often live in separate files and need to be joined together.
This exercise uses simulated data for programming practice only.
"""

import pandas as pd


demographics = pd.DataFrame(
    {
        "patient_id": [101, 102, 103, 104, 105],
        "department": ["cardiology", "respiratory", "cardiology", "neurology", "respiratory"],
    }
)

vitals = pd.DataFrame(
    {
        "patient_id": [103, 101, 104, 102, 105],
        "heart_rate": [88, 72, 112, 105, 96],
        "oxygen_level": [97, 98, 91, 95, 99],
    }
)

day1_readings = pd.DataFrame({"patient_id": [101, 102], "heart_rate": [72, 105]})
day2_readings = pd.DataFrame({"patient_id": [101, 102], "heart_rate": [75, 101]})


def merge_patient_records(demographics_df, vitals_df):
    """Return one DataFrame combining demographics and vitals by patient_id.

    Task 1: pd.merge
    - The two tables are in a different patient order and don't need to be
      sorted first; merge matches rows by the shared "patient_id" column.
    - Use pd.merge(left, right, on="patient_id").

    Expected: 5 rows, columns patient_id/department/heart_rate/oxygen_level,
    in demographics_df's original patient order (101, 102, 103, 104, 105).
    """
    # TODO: replace pass
    return pd.merge(demographics_df, vitals_df, on= "patient_id")
    #类似 Excel 的“按共同列匹配”。即使两个表里病人的顺序不同，也会根据 patient_id 找到正确的一行。


def department_counts(dataframe):
    """Return how many patients are in each department.

    Task 2: value_counts
    - Use dataframe["department"].value_counts().

    Expected:
    cardiology     2
    respiratory    2
    neurology      1

    和 Counter 很像
    Counter:通用 Python 数据结构工具
    value_counts:Pandas 数据分析工具
    """
    # TODO: replace pass
    return dataframe["department"].value_counts()


def sort_by_heart_rate_desc(dataframe):
    """Return the DataFrame sorted from highest to lowest heart rate.

    Task 3: sort_values
    - Use sort_values("heart_rate", ascending=False).
    - Reset the index with drop=True afterward.

    Expected patient_id order:
    [104, 102, 105, 103, 101]
    """
    # TODO: replace pass
    return dataframe.sort_values("heart_rate", ascending= False).reset_index(drop= True)


def combine_two_days(day1, day2):
    """Return one DataFrame with day2's rows appended after day1's rows.

    Task 4: pd.concat
    - Use pd.concat([day1, day2], ignore_index=True) so the index is
      renumbered from 0 instead of repeating 0, 1, 0, 1.

    Expected heart_rate column, top to bottom:
    [72, 105, 75, 101]
    """
    # TODO: replace pass
    return pd.concat([day1,day2], ignore_index = True)
    """NumPy 处理“数值矩阵”Pandas 处理“带标签的数据表”
    ignore_index=True 会让新表的行号变成 0、1、2、3。"""


def main():
    print("Task 1: merged patient records")
    merged = merge_patient_records(demographics, vitals)
    print(merged)

    print("\nTask 2: department counts")
    print(department_counts(merged))

    print("\nTask 3: sorted by heart rate (desc)")
    print(sort_by_heart_rate_desc(merged))

    print("\nTask 4: two days combined")
    print(combine_two_days(day1_readings, day2_readings))


if __name__ == "__main__":
    main()
