"""Matplotlib practice: turning numbers into readable plots.

Unlike numpy/pandas practice, there's no single "Expected" value to check
here — the point is a picture. Each task saves a PNG into this folder's
output/ directory. After completing a task, open the PNG and compare it
against the description to check your work.
"""

import matplotlib.pyplot as plt
import pandas as pd


OUTPUT_DIR = "04_matplotlib_basics/output"

heart_rate_signal = pd.Series([72, 75, 110, 74, 73, 120, 71, 70], name="heart_rate")

department_avg_heart_rate = pd.Series(
    {"cardiology": 80.0, "respiratory": 103.0, "neurology": 96.0}
)

patients = pd.DataFrame(
    {
        "patient_id": [101, 102, 103, 104, 105, 106],
        "heart_rate": [72, 105, 88, 112, 96, 64],
        "oxygen_level": [98, 95, 97, 91, 99, 96],
    }
)


def plot_signal_line(signal, output_path):
    """Save a line plot of signal over time.

    Task 1: basic line plot
    - Create a figure with plt.subplots().
    - Plot signal.values with ax.plot().
    - Set a title, x-label ("Time"), and y-label ("Heart rate (bpm)").
    - Save with fig.savefig(output_path), then plt.close(fig).

    Check the PNG: one blue line, rising and falling, no flat/empty plot.
    """
    # TODO: replace pass
    fig, ax = plt.subplots()
    ax.plot(signal.values)
    ax.set_title("Heart rate over time")
    ax.set_xlabel("Time")
    ax.set_ylabel("Heart rate (bpm)")
    fig.tight_layout()
    fig.savefig(output_path)
    plt.close(fig)
    """fig, ax = plt.subplots() —— 这一步固定写法,建一个"画布"(fig)和上面的一块"绘图区域"(ax)。以后你所有的画图操作(画线、加标题、加坐标轴标签)都是在 ax 上调用方法,不是在 fig 上
        ax.plot(signal.values) —— 在这块区域上画一条折线。signal.values 把 pandas 的 Series 转成普通 numpy 数组的数值,plot 会把它们当成 y 轴的值,x 轴自动用 0,1,2,3...(索引位置)
        ax.set_title(...) / ax.set_xlabel(...) / ax.set_ylabel(...) —— 给图加标题和两个轴的说明文字,不加的话别人看这张图不知道横竖轴代表什么
        fig.savefig(output_path) —— 把整张图存成文件(PNG),这是"保存"的动作,存在 fig 上,不是 ax 上
        plt.close(fig) —— 画完存完之后关掉这张图,释放内存。如果一次跑多个任务、每个都建一张新图,不关掉的话内存会越攒越多"""


def plot_signal_with_smoothing(signal, output_path, window=3):
    """Save a plot with the raw signal and its rolling mean overlaid.

    Task 2: two lines + legend
    - Plot the raw signal as one line, labeled "raw".
    - Plot signal.rolling(window=window).mean() as a second line,
      labeled "rolling mean".
    - Call ax.legend() so both labels appear.

    Check the PNG: two lines on the same axes; the "rolling mean" line
    should look smoother (less jagged) than "raw", with a legend box
    identifying which is which.
    """
    # TODO: replace pass
    fig, ax = plt.subplots()
    ax.plot(signal.values, label = "raw")
    ax.plot(signal.rolling(window=window).mean().values,
            label= "rolling mean")
    ax.set_title("Heart rate and rolling mean")
    ax.set_xlabel("Time")
    ax.set_ylabel("Heart rate (bpm)")
    ax.legend()
    fig.tight_layout()
    fig.savefig(output_path)
    plt.close(fig)


def plot_department_bar_chart(averages, output_path):
    """Save a bar chart of average heart rate per department.

    Task 3: bar chart from a Series
    - averages.index holds the department names.
    - averages.values holds the numbers.
    - Use ax.bar(averages.index, averages.values).

    Check the PNG: three bars, one per department, with respiratory
    clearly the tallest (~103) and cardiology the shortest (~80).
    """
    # TODO: replace pass
    fig, ax = plt.subplots()
    ax.bar(averages.index, averages.values)
    ax.set_title("Average heart rate by department")
    ax.set_xlabel("Department")
    ax.set_ylabel("Heart rate (bpm)")
    fig.tight_layout()
    fig.savefig(output_path)
    plt.close(fig)


def plot_priority_scatter(dataframe, output_path):
    """Save a scatter plot highlighting high-priority patients.

    Task 4: scatter plot with two groups and a legend
    - A patient is high priority if heart_rate > 100 OR oxygen_level < 95.
    - Split dataframe into two subsets using that mask (and its inverse).
    - Plot each subset with a separate ax.scatter() call (x=heart_rate,
      y=oxygen_level) so they get different colors automatically.
    - Label each call ("normal", "priority") and call ax.legend().

    Check the PNG: most points in one color, with 2 points (patients 102
    and 104) in a different color, positioned further right or lower.
    """
    # TODO: replace pass
    mask = (dataframe["heart_rate"] > 100) | (dataframe["oxygen_level"] < 95)
    normal = dataframe[~mask]
    priority = dataframe[mask]

    fig, ax = plt.subplots()
    ax.scatter(normal["heart_rate"], normal["oxygen_level"],label="normal")
    ax.scatter(priority["heart_rate"], priority["oxygen_level"],label="priority")

    ax.set_title("Priority patients by vital signs")
    ax.set_xlabel("Heart rate (bpm)")
    ax.set_ylabel("Oxygen level (%)")
    ax.legend()
    fig.tight_layout()
    fig.savefig(output_path)
    plt.close(fig)



def plot_signal_and_variability(signal, output_path, window=3):
    """Save a two-panel figure: raw signal on top, rolling std below.

    Task 5: subplots
    - Use plt.subplots(2, 1) to get a figure with two stacked Axes.
    - On the first Axes, plot the raw signal.
    - On the second Axes, plot signal.rolling(window=window).std().
    - Give each Axes its own title ("Heart rate", "Variability").
    - Use fig.tight_layout() before saving so the titles don't overlap.

    Check the PNG: top panel matches Task 1's shape; bottom panel is
    lowest in the calm middle stretch and spikes where the top panel
    has a sudden jump (around the 110 and 120 readings).
    """
    # TODO: replace pass
    fig, axes = plt.subplots(2,1)
    #plt.subplots(rows, columns)
    axes[0].plot(signal.values, label = "raw")
    axes[1].plot(signal.rolling(window=window).std(), label="rolling std")

    axes[0].set_title("Heart rate")
    axes[1].set_title("Variability")
    axes[0].set_ylabel("Heart rate (bpm)")
    axes[1].set_xlabel("Time")
    axes[1].set_ylabel("Rolling std (bpm)")

    fig.tight_layout()
    fig.savefig(output_path)
    plt.close(fig)



def main():
    import os

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    plot_signal_line(heart_rate_signal, f"{OUTPUT_DIR}/task1_line.png")
    print("Task 1 saved to output/task1_line.png")

    plot_signal_with_smoothing(heart_rate_signal, f"{OUTPUT_DIR}/task2_smoothing.png")
    print("Task 2 saved to output/task2_smoothing.png")

    plot_department_bar_chart(department_avg_heart_rate, f"{OUTPUT_DIR}/task3_bar.png")
    print("Task 3 saved to output/task3_bar.png")

    plot_priority_scatter(patients, f"{OUTPUT_DIR}/task4_scatter.png")
    print("Task 4 saved to output/task4_scatter.png")

    plot_signal_and_variability(heart_rate_signal, f"{OUTPUT_DIR}/task5_subplots.png")
    print("Task 5 saved to output/task5_subplots.png")


if __name__ == "__main__":
    main()
