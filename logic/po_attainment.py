import pandas as pd

def calculate_po_attainment(final_co_attainment, mapping_file):
    mapping_df = pd.read_excel(mapping_file)

    po_columns = mapping_df.columns[1:]

    po_scores = {po: [] for po in po_columns}

    for _, row in mapping_df.iterrows():
        co = row["CO"]
        for po in po_columns:
            po_scores[po].append(final_co_attainment[co] * row[po])

    po_attainment = {}
    for po, values in po_scores.items():
        po_attainment[po] = round(sum(values) / sum(mapping_df[po]), 2)

    return po_attainment
