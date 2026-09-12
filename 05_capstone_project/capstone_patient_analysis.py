"""Capstone: a full patient-data pipeline, numpy + pandas + matplotlib.

This combines everything from the last several weeks into one pipeline:
load real data -> clean it -> find bad readings -> summarize by group ->
look at the data visually. Tasks 1-4 don't tell you which method to
use — that's the point, decide for yourself from what you already know.
Tasks 5-7 are brand new (histogram, box plot, correlation heatmap), so
those come with full instructions.

This is simulated data for programming practice only, not a real
clinical dataset.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


INPUT_PATH = "05_capstone_project/data/raw_patient_vitals.csv"
OUTPUT_DIR = "05_capstone_project/output"


def load_patient_data(path):
    """Return the raw patient data as a DataFrame.

    Task 1
    - The file has a header row and a patient_id column, like every CSV
      you've loaded before.

    Expected shape:
    (12, 5)
    """
    # TODO: replace pass
    return pd.read_csv(path)
    #with header and id means use pandas


def fill_missing_oxygen(dataframe):
    """Return a copied DataFrame with missing oxygen_level values filled in.

    Task 2 — a judgment call, not just a method name
    - Two rows are missing oxygen_level.
    - These are 12 unrelated patients measured once each, not one
      patient's continuous signal over time — so think about which of
      the two missing-value techniques you already know (from earlier
      exercises) actually fits this shape of data, and use that one.

    Expected oxygen_level for patient 103 and patient 108 after filling:
    96.0 for both
    """
    # TODO: replace pass
    copied_dataframe = dataframe.copy()
    median_value = dataframe["oxygen_level"].median()
    copied_dataframe["oxygen_level"] = copied_dataframe["oxygen_level"].fillna(median_value)
    return copied_dataframe


def remove_outliers(dataframe, threshold=2.0):
    """Return a copied DataFrame with statistically extreme heart_rate rows removed.

    Task 3 — you've written this exact calculation before, in a
    different file, on a plain numpy array instead of a DataFrame column
    - Convert the heart_rate column to a numpy array.
    - Work out how far each value is from the average, in standard
      deviations (you named this kind of calculation before).
    - Keep only the rows where that value's magnitude is within threshold.

    Expected: 11 rows remain (patient 107's heart_rate of 190 is removed)
    """
    # TODO: replace pass
    copied_dataframe = dataframe.copy()
    array = copied_dataframe["heart_rate"].to_numpy()

    mean = array.mean()
    std = array.std()

    z_score = (array - mean)/std
    mask = np.abs(z_score) <= threshold

    return copied_dataframe[mask]



def department_average_heart_rate(dataframe):
    """Return average heart_rate per department, on the cleaned data.

    Task 4

    Expected:
    cardiology      80.75
    neurology       83.25
    respiratory    101.00
    """
    # TODO: replace pass
    return dataframe.groupby("department")["heart_rate"].mean()


def plot_heart_rate_histogram(dataframe, output_path):
    """Save a histogram showing the distribution of heart_rate values.

    Task 5: ax.hist — new chart type
    - A histogram groups numeric values into ranges ("bins") and draws a
      bar for how many values fall in each range — it answers "what does
      the overall spread of this variable look like?", which a single
      mean/std number can't show you (two very different distributions
      can share the same mean).
    - title: "Heart rate distribution"
    - Save and close like every plotting task before this one.

    Check the PNG: most bars clustered in the 70s-100s range, roughly
    matching where most of your 11 cleaned patients fall.
    """
    # TODO: replace pass
    fig, ax = plt.subplots()
    ax.hist(dataframe["heart_rate"], bins=6)
    ax.set_title("Heart rate distribution")
    ax.set_xlabel("Heart rate (bpm)")
    ax.set_ylabel("Patient count")
    fig.tight_layout()
    fig.savefig(output_path)
    plt.close(fig)


def plot_heart_rate_boxplot_by_department(dataframe, output_path):
    """Save a box plot comparing heart_rate across departments.

    Task 6: ax.boxplot — new chart type
    - A box plot needs a list of arrays, one per group, not one combined
      column — unlike everything you've plotted so far.
    - Build that list with a comprehension:
      groups = [
          dataframe[dataframe["department"] == department]["heart_rate"]
          for department in dataframe["department"].unique()
      ]
    - fig, ax = plt.subplots()
    - ax.boxplot(groups, tick_labels=dataframe["department"].unique())
    - Save and close as usual.

    Check the PNG: three boxes side by side, with respiratory's box
    sitting noticeably higher than the other two (matches Task 4's
    numbers — this is the same fact, seen instead of read).
    """
    # TODO: replace pass
    groups =[
        dataframe[dataframe["department"] == department]["heart_rate"]
        #找出这个部门所有人的 heart_rate。
        for department in dataframe["department"].unique()
        #三个部门，三次循环
    ]
    fig, ax = plt.subplots()
    ax.boxplot(groups, tick_labels=dataframe["department"].unique())
    ax.set_title("Heart rate by department")
    ax.set_xlabel("Department")
    ax.set_ylabel("Heart rate (bpm)")
    fig.tight_layout()
    #unique用于找到有哪些组
    fig.savefig(output_path)
    plt.close(fig)



def plot_correlation_heatmap(dataframe, output_path):
    """Save a heatmap of the correlation matrix between the numeric vitals.

    Task 7: ax.imshow — new chart type, reusing corr() from pandas practice
    - columns = ["heart_rate", "oxygen_level", "temperature"]
    - corr_matrix = dataframe[columns].corr() — you've done this exact
      call before.
    - fig, ax = plt.subplots()
    - image = ax.imshow(corr_matrix, vmin=-1, vmax=1)
    - fig.colorbar(image)  # shows what each color means, -1 to 1
    - Save and close as usual.

    Check the PNG: a 3x3 grid of colored squares, diagonal squares all
    the same color (self-correlation = 1.0), and the heart_rate/oxygen_level
    square a visibly different color from heart_rate/temperature — matching
    the fact that one of those pairs correlates much more strongly than
    the other (you calculated exactly this in pandas_describe_corr_practice.py).
    """
    # TODO: replace pass
    columns = ["heart_rate", "oxygen_level", "temperature"]
    corr_matrix = dataframe[columns].corr()
    fig, ax = plt.subplots()
    image = ax.imshow(corr_matrix, cmap="coolwarm", vmin=-1, vmax=1)
    ax.set_xticks(range(len(columns)))
    #xticks 控制 x 轴标签
    ax.set_yticks(range(len(columns)))
    ax.set_xticklabels(columns)
    ax.set_yticklabels(columns)
    ax.set_title("Correlation among vital signs")
    for row_index in range(len(columns)):
        for column_index in range(len(columns)):
            value = corr_matrix.iloc[row_index, column_index]
            text_color = "white" if abs(value) > 0.5 else "black"
            ax.text(column_index, row_index, f"{value:.2f}", ha="center", va="center", color=text_color)
    fig.colorbar(image, ax=ax, label="Pearson correlation")
    fig.tight_layout()
    #颜色对应数值。
    fig.savefig(output_path)
    plt.close(fig)


def main():
    import os

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    raw = load_patient_data(INPUT_PATH)
    print("Task 1: raw data")
    print(raw)

    filled = fill_missing_oxygen(raw)
    print("\nTask 2: missing oxygen filled")
    print(filled[["patient_id", "oxygen_level"]])

    clean = remove_outliers(filled)
    print("\nTask 3: outliers removed")
    print(f"{len(clean)} rows remain")

    print("\nTask 4: average heart rate by department")
    print(department_average_heart_rate(clean))

    plot_heart_rate_histogram(clean, f"{OUTPUT_DIR}/task5_histogram.png")
    print("\nTask 5 saved to output/task5_histogram.png")

    plot_heart_rate_boxplot_by_department(clean, f"{OUTPUT_DIR}/task6_boxplot.png")
    print("Task 6 saved to output/task6_boxplot.png")

    plot_correlation_heatmap(clean, f"{OUTPUT_DIR}/task7_heatmap.png")
    print("Task 7 saved to output/task7_heatmap.png")


if __name__ == "__main__":
    main()
