from flask import Flask, render_template, request
import os
import pandas as pd

from logic.co_attainment import calculate_co_attainment
from logic.po_attainment import calculate_po_attainment
from logic.plot import (
    plot_direct_co,
    plot_indirect_co,
    plot_direct_vs_indirect,
    plot_final_co,
    plot_po_pso,
    plot_co_po
)

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
GRAPH_FOLDER = "static/graphs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(GRAPH_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    co_file = request.files["co_marks"]
    indirect_file = request.files["indirect"]
    mapping_file = request.files["mapping"]

    co_path = os.path.join(UPLOAD_FOLDER, co_file.filename)
    indirect_path = os.path.join(UPLOAD_FOLDER, indirect_file.filename)
    mapping_path = os.path.join(UPLOAD_FOLDER, mapping_file.filename)

    co_file.save(co_path)
    indirect_file.save(indirect_path)
    mapping_file.save(mapping_path)

    # ---- Calculations ----
    direct, indirect_att, final = calculate_co_attainment(co_path, indirect_path)
    po_att = calculate_po_attainment(final, mapping_path)

    # ---- Graphs ----
    graphs = {
        "direct": plot_direct_co(direct),
        "indirect": plot_indirect_co(indirect_att),
        "compare": plot_direct_vs_indirect(direct, indirect_att),
        "final": plot_final_co(final),
        "po": plot_po_pso(po_att),
        "mapping": plot_co_po(mapping_path)
    }

    # Save graphs
    graph_files = {}
    for name, fig in graphs.items():
        path = f"{GRAPH_FOLDER}/{name}.png"
        fig.savefig(path, bbox_inches="tight")
        graph_files[name] = path

    return render_template(
        "results.html",
        direct=direct,
        indirect=indirect_att,
        final=final,
        po=po_att,
        graphs=graph_files
    )


if __name__ == "__main__":
    app.run(debug=True)
