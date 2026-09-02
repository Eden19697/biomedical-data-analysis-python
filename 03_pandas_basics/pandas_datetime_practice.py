"""Pandas practice: timestamped vital-sign data.

Real sensor and clinical datasets commonly record a timestamp with each
measurement. This exercise uses simulated data for programming practice only.
"""

import pandas as pd


vital_sign_data = {
    "patient_id": [102, 101, 104, 101, 102, 104],
    "timestamp": [
        "2026-07-01 09:00",
        "2026-07-01 08:00",
        "2026-07-02 20:00",
        "2026-07-01 20:00",
        "2026-07-02 09:00",
        "2026-07-02 08:00",
    ],
    "heart_rate": [105, 72, 109, 76, 101, 112],
    "oxygen_level": [95, 98, 92, 97, 96, 91],
}


def prepare_vital_signs_dataframe(data):
    """Return a DataFrame with datetime timestamps sorted chronologically.

    Task 1: datetime conversion and sorting
    - Create a DataFrame from data.
    - Convert the timestamp column with pd.to_datetime.
    - Sort rows by timestamp and reset the index with drop=True.

    Expected first row:
    patient_id: 101, timestamp: 2026-07-01 08:00, heart_rate: 72
    """
    # TODO: replace pass
    dataframe = pd.DataFrame(data)
    dataframe["timestamp"] = pd.to_datetime(dataframe["timestamp"])

    dataframe = dataframe.sort_values("timestamp")
    dataframe = dataframe.reset_index(drop=True)
    """reset_index(drop=True) = 筛选/删除数据后，把行号重新从 0 排一遍，不保留旧编号。"""

    return dataframe


def patient_readings(dataframe, patient_id):
    """Return all timestamped readings for one patient.

    Task 2: select rows by one column value
    - Build a mask with dataframe["patient_id"] == patient_id.
    - Use dataframe[mask].

    Expected IDs when patient_id=101:
    [101, 101]
    """
    # TODO: replace pass
    patient_mask = dataframe["patient_id"] == patient_id
    return dataframe[patient_mask]


def daily_mean_heart_rate(dataframe):
    """Return mean heart rate grouped by calendar date.

    Task 3: datetime accessor + groupby
    - dataframe["timestamp"].dt.date extracts the date part of each timestamp.
    - Group heart_rate by that date and calculate mean.

    Expected values:
    2026-07-01     84.333333
    2026-07-02    107.333333
    """
    # TODO: replace pass
    return(
        dataframe.groupby(dataframe["timestamp"].dt.date)["heart_rate"].mean()
    )
"""dataframe["timestamp"].dt.date
→ 得到每一行对应的日期

groupby(...)
→ 相同日期放进同一组

["heart_rate"]
→ 每组只查看心率列

.mean()
→ 计算该日期的平均心率"""


def readings_in_time_range(dataframe, start, end):
    """Return readings whose timestamp is between start and end, inclusive.

    Task 4: time-range filtering
    - Convert start and end using pd.Timestamp.
    - Build two timestamp comparisons and combine them with &.

    Expected for 2026-07-01 09:00 through 2026-07-02 09:00:
    patient IDs [102, 101, 104, 102]
    """
    # TODO: replace pass
    """Timestamp 是一个“时间对象”, pd.to_datetime() 是一个“转换工具”"""
    start_time = pd.Timestamp(start)
    end_time = pd.Timestamp(end)

    after_start_mask = dataframe["timestamp"] >= start_time
    before_end_mask = dataframe["timestamp"] <= end_time

    time_range_mask = after_start_mask & before_end_mask
    return dataframe[time_range_mask]



def add_measurement_day(dataframe):
    """Return a copied DataFrame with a measurement_day column.

    Task 5: add a datetime-derived column safely
    - Start with dataframe.copy().
    - Add copied_dataframe["measurement_day"] from timestamp.dt.day_name().

    Expected days:
    Wednesday for 2026-07-01 and Thursday for 2026-07-02.
    """
    # TODO: replace pass
    copied_dataframe = dataframe.copy()
    copied_dataframe["measurement_day"] = (
        copied_dataframe["timestamp"].dt.day_name()
        #它会把每条记录的时间转换成星期名称：
    )

    return copied_dataframe



def main():
    print("Task 1: prepared vital-sign DataFrame")
    vital_signs_dataframe = prepare_vital_signs_dataframe(vital_sign_data)
    print(vital_signs_dataframe)

    print("\nTask 2: readings for patient 101")
    print(patient_readings(vital_signs_dataframe, 101))

    print("\nTask 3: daily mean heart rate")
    print(daily_mean_heart_rate(vital_signs_dataframe))

    print("\nTask 4: readings in time range")
    print(readings_in_time_range(vital_signs_dataframe, "2026-07-01 09:00", "2026-07-02 09:00"))

    print("\nTask 5: measurement day")
    print(add_measurement_day(vital_signs_dataframe)[["patient_id", "timestamp", "measurement_day"]])


if __name__ == "__main__":
    main()
