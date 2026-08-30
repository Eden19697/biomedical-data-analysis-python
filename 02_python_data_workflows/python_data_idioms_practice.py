"""Python data-work idioms.

These tools are frequently used before or alongside NumPy and Pandas.
Complete one function at a time. Prefer clear names and readable code.
"""

from collections import Counter, defaultdict, deque


patient_ids = [101, 102, 103, 104, 105, 106]
heart_rates = [72, 105, 88, 112, 96, 64]


def normal_heart_rate_ids(ids, rates, lower=60, upper=100):
    """Return IDs whose rate is within the inclusive normal range.

    Task 1: list comprehension + zip
    - zip(ids, rates) pairs values from the two matching lists.
    - Use one list comprehension; do not write a normal for-loop block.

    Expected:
    [101, 103, 105, 106]
    """
    # TODO: replace pass
    return [
        patient_id
        for patient_id, rate in zip(ids, rates)
        if lower <= rate <= upper
    ]
"""
从 zip(patient_ids, heart_rates) 中逐对取出 patient_id 和 rate
如果 rate 在 60 到 100 之间；
就把 patient_id 放入新列表。
"""


def high_rate_positions(rates, threshold=100):
    """Return (index, rate) pairs for values strictly above threshold.

    Task 2: enumerate + list comprehension

    Expected:
    [(1, 105), (3, 112)]
    """
    # TODO: replace pass
    return [
        (index, rate)
        for index, rate in enumerate(rates)
        if rate > threshold
    ]


def symptom_counts(symptoms):
    """Return the occurrence count of every symptom.

    Task 3: Counter

    Expected for the supplied data:
    Counter({'cough': 3, 'fever': 2, 'fatigue': 1})

    counts[symptom] = counts.get(symptom, 0) + 1
    easier way of += 1
    """
    # TODO: replace pass
    return Counter(symptoms)


def group_patient_ids_by_department(records):
    """Group patient IDs by department.

    Task 4: defaultdict(list)
    - Each record is a (department, patient_id) tuple.

    Expected:
    {
        'cardiology': [101, 103],
        'respiratory': [102, 105],
        'neurology': [104],
    }

    defaultdic(list) 如果一个 key 第一次出现，自动给它创建空 list。
    """
    # TODO: replace pass
    groups = defaultdict(list)

    for department, patient_id in records:
        groups[department].append(patient_id)

    return groups




def serve_patient_queue(patient_queue):
    """Return patient IDs in the order they are served.

    Task 5: deque double-ended queue双端队列
    - Convert the incoming list to deque.
    - Repeatedly use popleft() until the queue is empty.
    - Return a normal list of served IDs.

    Expected for [101, 102, 103]:
    [101, 102, 103]

    Reminder: list.pop(0) is O(n); deque.popleft() is O(1).
    """
    # TODO: replace pass
    queue = deque(patient_queue)
    served_ids = []

    while queue:
        patient_id = queue.popleft()
        served_ids.append(patient_id)
    return served_ids


def valid_sensor_values(readings):
    """Yield one valid sensor value at a time, skipping None values.
    Generator 的思路是：需要一个值时，才产生一个值。

    Task 6: generator + yield
    - This function should use yield, not return a list.
    - Call list(valid_sensor_values(...)) in main to view the result.

    Expected for [72, None, 80, None, 76]:
    [72, 80, 76]
    """
    # TODO: replace pass
    for reading in readings:
        if reading is not None:
            yield reading


def main():
    print("Task 1: normal heart-rate IDs")
    print(normal_heart_rate_ids(patient_ids, heart_rates))
    print("Expected: [101, 103, 105, 106]")

    print("\nTask 2: high-rate positions")
    print(high_rate_positions(heart_rates))
    print("Expected: [(1, 105), (3, 112)]")

    symptoms = ["fever", "cough", "cough", "fatigue", "fever", "cough"]
    print("\nTask 3: symptom counts")
    print(symptom_counts(symptoms))
    print("Expected: Counter({'cough': 3, 'fever': 2, 'fatigue': 1})")

    records = [
        ("cardiology", 101),
        ("respiratory", 102),
        ("cardiology", 103),
        ("neurology", 104),
        ("respiratory", 105),
    ]
    print("\nTask 4: patients by department")
    print(dict(group_patient_ids_by_department(records)))
    print("Expected: {'cardiology': [101, 103], 'respiratory': [102, 105], 'neurology': [104]}")

    print("\nTask 5: served patient queue")
    print(serve_patient_queue([101, 102, 103]))
    print("Expected: [101, 102, 103]")

    print("\nTask 6: valid sensor values")
    print(list(valid_sensor_values([72, None, 80, None, 76])))
    print("Expected: [72, 80, 76]")


if __name__ == "__main__":
    main()
