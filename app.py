from flask import Flask, render_template, request
import os
import markdown
from analysis.mutation_analysis import load_maf
from analysis.mutation_analysis import analyze_mutations
from analysis.visualization import generate_plots
from llm_interpreter import explain_results

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["maf_file"]

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)

    file.save(filepath)

    # Load MAF
    df = load_maf(filepath)

    # Analyze
    results = analyze_mutations(df)

    # Generate plots
    plots = generate_plots(df)

    ai_summary = explain_results(results)
    ai_summary = markdown.markdown(ai_summary,extensions=["fenced_code", "tables"])

    return render_template(
        "results.html",
        results=results,
        plots=plots,
        ai_summary=ai_summary
    )


if __name__ == "__main__":
    app.run(debug=True)