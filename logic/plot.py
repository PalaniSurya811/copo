import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# -------------------------------------------------
# 1. Direct CO Attainment Graph
# -------------------------------------------------
def plot_direct_co(direct_attainment):
    cos = list(direct_attainment.keys())
    values = list(direct_attainment.values())

    fig, ax = plt.subplots()
    ax.bar(cos, values)
    ax.set_ylim(0, 3)
    ax.set_ylabel("Attainment Level (0–3)")
    ax.set_title("Direct CO Attainment")

    return fig


# -------------------------------------------------
# 2. Indirect CO Attainment Graph
# -------------------------------------------------
def plot_indirect_co(indirect_attainment):
    cos = list(indirect_attainment.keys())
    values = list(indirect_attainment.values())

    fig, ax = plt.subplots()
    ax.bar(cos, values)
    ax.set_ylim(0, 3)
    ax.set_ylabel("Attainment Level (0–3)")
    ax.set_title("Indirect CO Attainment")

    return fig


# -------------------------------------------------
# 3. Direct vs Indirect CO Comparison
# -------------------------------------------------
def plot_direct_vs_indirect(direct, indirect):
    cos = list(direct.keys())

    direct_vals = [direct[co] for co in cos]
    indirect_vals = [indirect.get(co, 0) for co in cos]

    x = np.arange(len(cos))
    width = 0.35

    fig, ax = plt.subplots()
    ax.bar(x - width/2, direct_vals, width, label="Direct")
    ax.bar(x + width/2, indirect_vals, width, label="Indirect")

    ax.set_xticks(x)
    ax.set_xticklabels(cos)
    ax.set_ylim(0, 3)
    ax.set_ylabel("Attainment Level (0–3)")
    ax.set_title("Direct vs Indirect CO Attainment")
    ax.legend()

    return fig


# -------------------------------------------------
# 4. Final CO Attainment Graph
# -------------------------------------------------
def plot_final_co(final_attainment):
    cos = list(final_attainment.keys())
    values = list(final_attainment.values())

    fig, ax = plt.subplots()
    ax.bar(cos, values)
    ax.set_ylim(0, 3)
    ax.set_ylabel("Final Attainment Level")
    ax.set_title("Final CO Attainment (0.8 Direct + 0.2 Indirect)")

    return fig


# -------------------------------------------------
# 5. PO / PSO Attainment Graph
# -------------------------------------------------
def plot_po_pso(po_attainment):
    pos = list(po_attainment.keys())
    values = list(po_attainment.values())

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(pos, values)
    ax.set_ylabel("Attainment Index")
    ax.set_title("PO / PSO Attainment")

    return fig


# -------------------------------------------------
# 6. CO–PO / PSO Mapping Graph (UNCHANGED – YOUR CODE)
# -------------------------------------------------
def plot_co_po(mapping_file):
    df = pd.read_excel(mapping_file)

    cos = df["CO"].tolist()
    po_cols = df.columns[1:]

    x = np.arange(len(cos))
    width = 0.8 / len(po_cols)

    fig, ax = plt.subplots(figsize=(14, 6))

    for i, po in enumerate(po_cols):
        values = df[po].tolist()
        ax.bar(x + i * width, values, width, label=po)

    ax.set_xticks(x + width * len(po_cols) / 2)
    ax.set_xticklabels(cos)
    ax.set_ylim(0, 3)
    ax.set_ylabel("Attainment Level (0–3)")
    ax.set_xlabel("Course Outcomes")
    ax.set_title("CO–PO / PSO Attainment (NBA / NAAC)")
    ax.legend(bbox_to_anchor=(1.05, 1), loc="upper left")

    return fig
