import pandas as pd

def calculate_co_attainment(co_marks_file, indirect_file):

    # DIRECT ATTAINMENT (UNCHANGED)
    
    df = pd.read_excel(co_marks_file)
    total_students = len(df)

    co_total_cols = [col for col in df.columns if col.endswith("_Total")]
    direct_attainment = {}

    for col in co_total_cols:
        co = col.replace("_Total", "")
        df[col] = pd.to_numeric(df[col], errors="coerce")
        valid_marks = df[col].dropna()

        count = (valid_marks >= 60).sum()
        percentage = (count / total_students) * 100

        if percentage >= 80:
            level = 3
        elif percentage >= 70:
            level = 2
        elif percentage >= 60:
            level = 1
        else:
            level = 0

        direct_attainment[co] = level

    # -------------------------
    # INDIRECT ATTAINMENT (UPDATED – OPTION 2)
    # -------------------------
    indirect_df = pd.read_excel(indirect_file)

    # Convert to numeric safely
    indirect_df["PartA"] = pd.to_numeric(indirect_df["PartA"], errors="coerce")

    # Average Part A (common for all COs)
    avg_part_a = indirect_df["PartA"].mean()

    indirect_attainment = {}

    for co in ["CO1", "CO2", "CO3", "CO4", "CO5"]:
        indirect_df[co] = pd.to_numeric(indirect_df[co], errors="coerce")

        avg_part_b = indirect_df[co].mean()

        # NBA formula
        indirect_percent = (0.4 * avg_part_a) + (0.6 * avg_part_b)

        # Convert percentage → level
        if indirect_percent >= 80:
            level = 3
        elif indirect_percent >= 70:
            level = 2
        elif indirect_percent >= 60:
            level = 1
        else:
            level = 0

        indirect_attainment[co] = round(level, 2)

    # -------------------------
    # FINAL CO ATTAINMENT (UNCHANGED)
    # -------------------------
    final_attainment = {}
    for co in direct_attainment:
        final_attainment[co] = round(
            0.8 * direct_attainment[co] +
            0.2 * indirect_attainment.get(co, 0),
            2
        )

    return direct_attainment, indirect_attainment, final_attainment
