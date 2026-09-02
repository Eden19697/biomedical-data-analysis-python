"""Pandas practice: filling gaps in a continuous signal.

You already filled missing values with a single number (the median).
That's fine for a table of unrelated patients, but wrong for a continuous
signal from one sensor — the value right before and after a gap is a much
better guide than the overall average. This exercise compares three ways
to fill gaps: interpolate, forward-fill, and backward-fill.
"""

import numpy as np
import pandas as pd


heart_rate_signal = pd.Series(
    [72, 74, np.nan, 78, 82, np.nan, np.nan, 90, 88], name="heart_rate"
)

oxygen_with_leading_gap = pd.Series(
    [np.nan, np.nan, 95, 96, 94], name="oxygen_level"
)


def interpolate_signal(signal):
    """Return signal with gaps filled by linear interpolation.

    Task 1: interpolate
    - Use signal.interpolate().
    - Each gap is filled with evenly spaced values between the reading
      before the gap and the reading after it, instead of one flat number.

    Expected (index 2, a single-point gap between 74 and 78):
    76.0
    Expected (index 5-6, a two-point gap between 82 and 90):
    84.666667, 87.333333
    """
    # TODO: replace pass
    return signal.interpolate()


def forward_filled_signal(signal):
    """Return signal with gaps filled by carrying the last known value forward.

    Task 2: ffill
    - Use signal.ffill().
    - Every NaN becomes a copy of the closest earlier valid value. This
      matches "the sensor froze, so assume the last reading held steady."

    Expected (index 2):
    74.0
    Expected (index 5-6):
    82.0, 82.0
    """
    # TODO: replace pass
    return signal.ffill()


def backward_filled_leading_gap(signal):
    """Return signal with a leading gap filled from the next valid value.

    Task 3: bfill
    - oxygen_with_leading_gap starts with two NaN values, so ffill can't
      fix them (there's nothing earlier to carry forward).
    - Use signal.bfill() instead: it fills each NaN with the closest
      later valid value.

    Expected (index 0-1):
    95.0, 95.0
    """
    # TODO: replace pass
    return signal.bfill()


def main():
    print("Original signal:")
    print(heart_rate_signal)

    print("\nTask 1: interpolated signal")
    print(interpolate_signal(heart_rate_signal))

    print("\nTask 2: forward-filled signal")
    print(forward_filled_signal(heart_rate_signal))

    print("\nTask 3: backward-filled leading gap")
    print("Original:")
    print(oxygen_with_leading_gap)
    print("Backward-filled:")
    print(backward_filled_leading_gap(oxygen_with_leading_gap))


if __name__ == "__main__":
    main()
