"""NumPy practice: simple patient risk screening.

This exercise combines multiple boolean conditions, similar to a simple data
quality or clinical-screening rule. It is for NumPy practice only and is not
medical advice or a clinical decision rule.

Rules:
- Do not use for loops.
- Name each boolean array as a *_mask.
- Put each comparison in parentheses before combining conditions with & or |.
"""

import numpy as np


patient_ids = np.array([101, 102, 103, 104, 105, 106])
heart_rates = np.array([72, 105, 88, 112, 96, 64])
oxygen_levels = np.array([98, 95, 97, 91, 99, 96])
temperatures = np.array([36.7, 37.9, 36.5, 38.2, 37.1, 36.8])


def high_risk_ids(ids, rates, oxygen):
    """Return IDs with both high heart rate and low oxygen.

    Task 1:
    - high heart rate: strictly greater than 100
    - low oxygen: strictly less than 95
    - Combine the two masks with &.

    Expected:
    [104]
    """
    # TODO: replace pass
    high_risk = (rates > 100) & (oxygen < 95)
    return ids[high_risk]



def follow_up_ids(ids, rates, temps):
    """Return IDs with high heart rate OR a fever.

    Task 2:
    - high heart rate: strictly greater than 100
    - fever: greater than or equal to 38.0
    - Combine the two masks with |.

    Expected:
    [102, 104]
    """
    # TODO: replace pass
    high_risk = (rates > 100) | (temps >= 38.0)
    return ids[high_risk]


def patient_risk_labels(rates, oxygen):
    """Return one label for each patient: high risk, monitor, or normal.

    Task 3:
    - high risk: high heart rate AND low oxygen
    - monitor: high heart rate OR low oxygen, but not high risk
    - normal: neither condition
    - Use nested np.where. No loop is needed.

    Expected:
    ['normal', 'monitor', 'normal', 'high risk', 'normal', 'normal']
    """
    # TODO: replace pass
    high_rate_mask = rates > 100
    low_oxygen_mask = oxygen < 95

    high_risk_mask = high_rate_mask & low_oxygen_mask
    monitor_mask = high_rate_mask | low_oxygen_mask

    return np.where(
        high_risk_mask,
        "high risk",
        np.where(monitor_mask, "monitor", "normal")
    )
#np.where(condition, condition is True‘s value, condition is False‘s value)


def main():
    print("Task 1: high-risk IDs")
    print(high_risk_ids(patient_ids, heart_rates, oxygen_levels))
    print("Expected: [104]")

    print("\nTask 2: follow-up IDs")
    print(follow_up_ids(patient_ids, heart_rates, temperatures))
    print("Expected: [102 104]")

    print("\nTask 3: patient risk labels")
    print(patient_risk_labels(heart_rates, oxygen_levels))
    print("Expected: ['normal' 'monitor' 'normal' 'high risk' 'normal' 'normal']")


if __name__ == "__main__":
    main()
