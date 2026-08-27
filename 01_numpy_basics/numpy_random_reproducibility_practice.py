"""NumPy practice: random simulation and reproducibility.

This uses simulated heart-rate data for programming practice only. A random
seed lets another person (or future you) reproduce the same result exactly.

Modern NumPy style: use np.random.default_rng(seed), not global random state.
"""

import numpy as np


patient_ids = np.array([101, 102, 103, 104, 105, 106])
observed_heart_rates = np.array([72.0, 105.0, 88.0, 112.0])


def simulate_heart_rates(patient_count=6, seed=42):
    """Return simulated heart rates from a normal distribution.

    Task 1: random generator + normal distribution
    - Create a local generator with np.random.default_rng(seed).
    - Use rng.normal with mean 75, standard deviation 8, and patient_count values.

    Expected when rounded to two decimals with seed=42:
    [77.44, 66.68, 81.0, 82.52, 59.39, 64.58]
    """
    # TODO: replace pass
    rng = np.random.default_rng(seed)
    return rng.normal(loc=75, scale=8, size=patient_count)
    """
    loc=75,模拟数据的中心平均值约为 75
    scale=8,数据有一定波动,标准差约为 8
    size=patient_count,生成 6 个值
    """


def is_reproducible(seed=42):
    """Return True if two independent generators with the same seed agree.

    Task 2: reproducibility
    - Make two separate generators, both with seed.
    - Have each generate five integers from 0 up to 99.
    - Use np.array_equal to compare the arrays.

    Expected:
    True
    同一个随机算法、同一个 seed,会产生同一串伪随机数。这样你下周重新运行,
    或别人运行你的 GitHub 项目，能得到同样结果。
    """
    # TODO: replace pass
    first_rng = np.random.default_rng(seed)
    second_rng = np.random.default_rng(seed)

    first_values = first_rng.integers(0, 100, size = 5)
    second_values = second_rng.integers(0, 100, size = 5)

    return np.array_equal(first_values, second_values)


def add_measurement_noise(readings, noise_std=1.5, seed=10):
    """Return readings with simulated normally distributed measurement noise.

    Task 3: matching random-array shape
    - Create a generator with seed.
    - Generate noise with mean 0, standard deviation noise_std, and readings.shape.
    - Return readings + noise.

    Expected for observed_heart_rates when rounded to two decimals:
    [70.34, 103.91, 86.83, 112.4]
    """
    # TODO: replace pass
    rng = np.random.default_rng(seed)
    noise = rng.normal(
        loc=0,
        scale=noise_std,
        size=readings.shape
    )
    return readings + noise


def sample_patient_ids(ids, sample_size=3, seed=7):
    """Return sample_size distinct IDs selected randomly.

    Task 4: random sampling
    - Use rng.choice.
    - Set replace=False so the same patient cannot appear twice.

    Expected for the supplied IDs and seed=7:
    [104, 105, 106]

    ids 可抽取的患者 ID
    size=sample_size 抽 3 位患者
    replace=False 抽过的患者不能再被抽到
    """
    # TODO: replace pass
    rng = np.random.default_rng(seed)
    return rng.choice(ids, size=sample_size, replace= False)


def main():
    print("Task 1: simulated heart rates")
    print(np.round(simulate_heart_rates(), 2))
    print("Expected: [77.44 66.68 81.   82.52 59.39 64.58]")

    print("\nTask 2: reproducible simulation")
    print(is_reproducible())
    print("Expected: True")

    print("\nTask 3: noisy observed readings")
    print(np.round(add_measurement_noise(observed_heart_rates), 2))
    print("Expected: [ 70.34 103.91  86.83 112.4 ]")

    print("\nTask 4: sampled patient IDs")
    print(sample_patient_ids(patient_ids))
    print("Expected: [104 105 106]")


if __name__ == "__main__":
    main()
