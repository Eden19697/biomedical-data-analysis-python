"""Pandas practice: rolling windows and pivot tables.

Rolling windows smooth noisy signals and reveal changes in variability,
which is how you would process a continuous sensor stream. Pivot tables
summarize a long table into a grid, useful for comparing groups.
This exercise uses simulated data for programming practice only.
"""

import pandas as pd

"""difference between DF and Series:
Series = 一列数据（带标签）
DataFrame = 多列数据组成的表格"""

heart_rate_signal = pd.Series([72, 75, 110, 74, 73, 120, 71, 70], name="heart_rate")

department_readings = pd.DataFrame(
    {
        "department": ["cardiology", "cardiology", "respiratory", "respiratory", "cardiology", "respiratory"],
        "day": ["Day1", "Day2", "Day1", "Day2", "Day1", "Day1"],
        "heart_rate": [72, 76, 105, 101, 88, 112],
    }
)


def smoothed_signal(signal, window=3):
    """Return the rolling mean of signal over the given window size.

    Task 1: rolling mean
    - Use signal.rolling(window=window).mean().
    - The first (window - 1) values will be NaN; that's expected, since
      there aren't enough prior points yet to average.

    Expected (rounded), positions 2 onward:
    85.666667, 86.333333, 85.666667, 89.0, 88.0, 87.0
    """
    # TODO: replace pass
    return signal.rolling(window= window).mean()
    """rolling(3) 表示每次看连续 3 个心率值，.mean() 求这三个值的平均。
    它可以让忽高忽低的数据变平滑。前两个结果是 NaN,因为还凑不够 3 个数。"""


def signal_variability(signal, window=3):
    """Return the rolling standard deviation of signal over the window.

    Task 2: rolling std
    - Use signal.rolling(window=window).std().
    - A rising value here means the signal is becoming less stable, which
      is useful for flagging irregular sensor behavior.

    Expected (rounded), positions 2 onward:
    21.13, 20.50, 21.08, 26.85, 27.73, 28.58
    """
    # TODO: replace pass
    return signal.rolling(window=window).std()


def department_day_pivot(dataframe):
    """Return mean heart rate for each department, one column per day.

    Task 3: pivot_table
    - Use dataframe.pivot_table(values="heart_rate", index="department",
      columns="day", aggfunc="mean").

    Expected:
                  Day1   Day2
    cardiology    80.0   76.0
    respiratory  108.5  101.0
    """
    # TODO: replace pass
    return dataframe.pivot_table(values="heart_rate", index="department",
      columns="day", aggfunc="mean")


def main():
    print("Task 1: smoothed signal (rolling mean)")
    print(smoothed_signal(heart_rate_signal))

    print("\nTask 2: signal variability (rolling std)")
    print(signal_variability(heart_rate_signal))

    print("\nTask 3: department/day pivot table")
    print(department_day_pivot(department_readings))


if __name__ == "__main__":
    main()
