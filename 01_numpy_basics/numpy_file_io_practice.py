"""NumPy practice: reading raw sensor data from a file, and two ways to save it.

Every numpy exercise so far used arrays typed directly into the script.
Real sensor data starts life as a file. This one builds a small pipeline:
load a raw reading stream -> detect which readings are outliers ->
save only the clean ones, in two different file formats.

Rules:
- Do not use for loops for the TODO functions.
"""

import numpy as np


INPUT_PATH = "01_numpy_basics/data/heart_rate_stream.txt"
CLEAN_TEXT_PATH = "01_numpy_basics/data/clean_heart_rate.csv"
CLEAN_BINARY_PATH = "01_numpy_basics/data/clean_heart_rate.npy"


def load_readings(path):
    """Return a 1D array loaded from a comma-separated text file.

    Task 1: np.loadtxt
    - Use np.loadtxt(path, delimiter=",").
    - A text file has no dtype information, same problem as pd.read_csv
      had — loadtxt will give you float64 values here.

    Expected:
    [ 72.  74.  73.  75. 130.  74.  72.  73.  20.  75.  74.  73.]
    """
    # TODO: replace pass
    return np.loadtxt(path,delimiter=",")
    #告诉 NumPy：你的文件里面每一列数据是用什么符号隔开的。


def flag_anomalies(readings, threshold=2.0):
    """Return a boolean mask marking readings far from the average.

    Task 2: z-scores (no single numpy function does this — combine a few)
    - A z-score says how many standard deviations a value is from the
      mean: z = (value - mean) / std.
    - Compute readings.mean() and readings.std() once each.
    - Compute the z-score for every reading at once (no loop needed —
      numpy applies +, -, / elementwise across the whole array).
    - A reading is an anomaly if the absolute value of its z-score is
      greater than threshold.

    Expected (True at positions 4 and 8, the 130 and the 20):
    [False False False False  True False False False  True False False False]
    """
    # TODO: replace pass
    mean = readings.mean()
    std = readings.std()
    z_scores = (readings - mean)/std
    """NumPy 会自动逐元素计算。"""
    anomalies = np.abs(z_scores) > threshold
    return anomalies


def remove_anomalies(readings, anomaly_mask):
    """Return only the non-anomalous readings.

    Task 3: invert a mask
    - You already have a mask marking the anomalies as True.
    - Use ~anomaly_mask to flip it, then index readings with that.

    Expected:
    [72. 74. 73. 75. 74. 72. 73. 75. 74. 73.]
    """
    # TODO: replace pass
    return readings[~anomaly_mask]


def save_clean_readings(clean_readings, text_path, binary_path):
    """Save clean_readings to both a text file and a binary .npy file.

    Task 4: np.savetxt and np.save — two formats, two purposes
    - np.savetxt(text_path, clean_readings, delimiter=",") writes plain
      numbers a human (or Excel) can open and read directly.
    - np.save(binary_path, clean_readings) writes numpy's own binary
      format — not human-readable, but it preserves the array's exact
      values, shape, and dtype with no rounding or reparsing involved.
    - This function doesn't need to return anything.
    """
    # TODO: replace pass
    np.savetxt(text_path, clean_readings, delimiter=",")
    #writes plain numbers a human (or Excel) can open and read directly.

    np.save(binary_path, clean_readings)
    #not human-readable, but it preserves the array's exact values, shape, and dtype


def verify_round_trip(binary_path, original_array):
    """Return whether loading binary_path back gives exactly original_array.
    一个 NumPy 数组保存成文件，再读回来以后，是否和原来的数组完全一样。

    Task 5: np.load, and why the binary format exists
    - Use np.load(binary_path) to read the file back into an array.
    - Use np.array_equal(loaded_array, original_array) to compare —
      == on two arrays gives you an array of True/False, not one answer,
      so you can't use it directly in an if-check.

    Expected:
    True

    (If you instead reloaded from the .csv with np.loadtxt and compared,
    it would still be True here because these values happen to be plain
    integers — but it wouldn't be safe to assume that in general. Text
    round-trips can lose precision on values with many decimal places;
    the binary .npy format never does, which is why it exists.)
    """
    # TODO: replace pass
    load_array =  np.load(binary_path)
    return np.array_equal(load_array, original_array)

    """数组比较要用 array_equals, 不是==, 用.npy 文件不是 CSV, 因为CSV 没有 dshape 和 dim"""


def main():
    readings = load_readings(INPUT_PATH)
    print("Task 1: loaded readings")
    print(readings)

    print("\nTask 2: anomaly mask")
    anomaly_mask = flag_anomalies(readings)
    print(anomaly_mask)

    print("\nTask 3: clean readings")
    clean_readings = remove_anomalies(readings, anomaly_mask)
    print(clean_readings)

    print("\nTask 4: saving clean readings (text + binary)")
    save_clean_readings(clean_readings, CLEAN_TEXT_PATH, CLEAN_BINARY_PATH)
    print(f"Check that {CLEAN_TEXT_PATH} and {CLEAN_BINARY_PATH} now exist.")

    print("\nTask 5: round-trip check")
    print(verify_round_trip(CLEAN_BINARY_PATH, clean_readings))
    print("Expected: True")


if __name__ == "__main__":
    main()
