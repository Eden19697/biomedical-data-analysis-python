"""Pandas practice: custom row logic with apply().

Every previous exercise used a built-in method (mean, sort_values,
rolling...) that already existed in pandas. Sometimes the rule you need
is specific to your own problem, and there's no built-in for it. apply()
lets you run your own function across a DataFrame or Series.

This exercise builds a small risk-scoring pipeline, one stage at a time:
score each patient -> label each patient -> pull out only the ones that
need attention, worst first. This is simulated data for programming
practice only, not a real clinical scoring system.
"""

import pandas as pd


patients = pd.DataFrame(
    {
        "patient_id": [101, 102, 103, 104, 105, 106],
        "heart_rate": [72, 105, 88, 130, 96, 58],
        "oxygen_level": [98, 94, 97, 89, 99, 96],
        "temperature": [36.7, 37.9, 36.5, 39.0, 37.1, 36.8],
    }
)


def compute_deviation_score(row):
    """Return one patient's total deviation score, as a plain Python function.

    Task 1: write the scoring rule (no pandas method for this — just logic)
    row is one row of the DataFrame, so row["heart_rate"] etc. works like a
    dictionary lookup. Combine three deviation amounts:

    - heart_rate: normal range is 60-100, inclusive. Outside that range,
      the deviation is however many bpm past the nearer edge (e.g. a
      heart rate of 105 is 5 over 100, so its deviation is 5).
    - oxygen_level: normal is 95 or above. Below that, the deviation is
      (95 - oxygen_level) * 2 — oxygen drops are weighted more heavily.
    - temperature: normal is 37.5 or below. Above that, the deviation is
      (temperature - 37.5) * 10 — fever is weighted heaviest of all.
    - A vital inside its normal range contributes 0.

    Return the sum of all three deviations.

    Expected for patient 104 (heart_rate=130, oxygen_level=89, temperature=39.0):
    (130 - 100) + (95 - 89) * 2 + (39.0 - 37.5) * 10 = 30 + 12 + 15 = 57.0

    Expected for patient 101 (72, 98, 36.7), all vitals normal:
    0.0
    """
    # TODO: replace pass
    deviation = 0
    if row["heart_rate"] > 100:
      deviation = deviation + (row["heart_rate"]-100)
    elif row["heart_rate"] < 60:
      deviation = deviation + (60 - row["heart_rate"])
    if row["oxygen_level"] < 95:
      deviation += (95 - row["oxygen_level"])*2
    if row["temperature"] > 37.5:
        deviation = deviation + (row["temperature"] - 37.5)*10
    return deviation


def add_risk_scores(dataframe):
    """Return a copied DataFrame with a risk_score column.

    Task 2: DataFrame.apply(..., axis=1)
    - Start with dataframe.copy().
    - axis=1 makes apply hand your function one row at a time (a Series),
      instead of one column at a time — that's what compute_deviation_score
      expects.
    - Set copied_dataframe["risk_score"] = copied_dataframe.apply(
          compute_deviation_score, axis=1).

    Expected risk_score column, patients 101-106 in order:
    [0.0, 11.0, 0.0, 57.0, 0.0, 2.0]
    """
    # TODO: replace pass
    copied_dataframe = dataframe.copy()
    copied_dataframe["risk_score"] = copied_dataframe.apply(compute_deviation_score, axis = 1)
    """一行一行地把整行数据(row)拿出来,喂给 compute_deviation_score 这个函数,
    把每次算出来的分数收集起来,最后变成一整列。"""
    return copied_dataframe


def categorize_score(score):
    """Return a risk_category label for a single score value.

    Task 3: a second small helper function
    - score == 0           -> "normal"
    - 0 < score <= 5        -> "watch"
    - score > 5             -> "urgent"

    Expected:
    categorize_score(0) -> "normal"
    categorize_score(2) -> "watch"
    categorize_score(57) -> "urgent"
    """
    # TODO: replace pass
    if score == 0:
        return "normal"
    elif 0< score <= 5:
        return "watch"
    elif score > 5:
        return "urgent"



def add_risk_categories(dataframe):
    """Return a copied DataFrame with a risk_category column.

    Task 4: Series.apply()
    - Start with dataframe.copy().
    - This time apply runs on a single column (a Series), not whole rows,
      so no axis argument is needed: dataframe["risk_score"].apply(...).
    - Set copied_dataframe["risk_category"] using categorize_score.

    Expected risk_category column, patients 101-106 in order:
    ['normal', 'urgent', 'normal', 'urgent', 'normal', 'watch']
    """
    # TODO: replace pass
    copied_dataframe = dataframe.copy()
    copied_dataframe["risk_category"] = copied_dataframe["risk_score"].apply(categorize_score)
    return copied_dataframe


def urgent_patients_by_severity(dataframe):
    """Return only urgent patients, worst risk_score first.

    Task 5: put the pipeline together
    - Filter dataframe to rows where risk_category == "urgent".
    - Sort the result by risk_score, descending.
    - Reset the index with drop=True.
    - This combines a boolean mask and sort_values, both from earlier
      exercises, with the two new columns you just built.

    Expected patient_id order:
    [104, 102]
    """
    # TODO: replace pass
    mask = dataframe["risk_category"] == "urgent"
    urgent = dataframe[mask]
    return urgent.sort_values("risk_score", ascending = False).reset_index(drop= True)


def main():
    print("Task 1: single deviation score")
    print("Patient 104 score:", compute_deviation_score(patients.iloc[3]))
    print("Expected: 57.0")

    print("\nTask 2: risk_score column")
    scored = add_risk_scores(patients)
    print(scored[["patient_id", "risk_score"]])

    print("\nTask 3: single category label")
    print(categorize_score(57))
    print("Expected: urgent")

    print("\nTask 4: risk_category column")
    categorized = add_risk_categories(scored)
    print(categorized[["patient_id", "risk_score", "risk_category"]])

    print("\nTask 5: urgent patients, worst first")
    print(urgent_patients_by_severity(categorized)[["patient_id", "risk_score"]])


if __name__ == "__main__":
    main()
