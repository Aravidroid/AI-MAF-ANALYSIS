import matplotlib.pyplot as plt
import os

PLOT_DIR = "static/plots"

os.makedirs(PLOT_DIR, exist_ok=True)

def generate_plots(df):

    plots = []

    top_genes = (
        df["Hugo_Symbol"]
        .value_counts()
        .head(10)
    )

    plt.figure(figsize=(10,5))

    top_genes.plot(kind="bar")

    plt.title("Top Mutated Genes")

    plot_path = os.path.join(
        PLOT_DIR,
        "top_genes.png"
    )

    plt.savefig(plot_path)

    plots.append(plot_path)

    return plots