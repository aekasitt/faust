import argparse
from pathlib import Path
from typing import Optional

import plotly.graph_objects as go
import polars as pl
from plotly.subplots import make_subplots

BENCH_DIR = Path(__file__).parent

DEFAULT_BENCH_RESULTS_PATH = BENCH_DIR / "results.csv"
DEFAULT_BENCH_SAVEPLOT_PATH = BENCH_DIR / "results.png"


def plot_benchmark_results(results_file: Optional[str] = None, save_plot: Optional[str] = None):
    if results_file:
        results_path = Path(results_file)
    else:
        results_path = DEFAULT_BENCH_RESULTS_PATH

    if save_plot:
        save_plot_path = Path(save_plot)
    else:
        save_plot_path = DEFAULT_BENCH_SAVEPLOT_PATH

    # Load the results DataFrame
    results_df = pl.read_csv(results_path)

    # Ensure 'strict_models' is treated as a string for grouping
    results_df = results_df.with_columns(pl.col("strict_models").cast(pl.Utf8))

    # Group by 'pydantic_version' and 'strict_models', compute the mean of 'import_time_s' and 'validate_time_s'
    avg_df = results_df.group_by(["pydantic_version", "strict_models"]).mean()

    # Split 'pydantic_version' into 'major', 'minor', and 'patch' components
    avg_df = avg_df.with_columns(
        [
            pl.col("pydantic_version").str.split_exact(".", 2).alias("version_split"),
        ]
    )
    avg_df = avg_df.with_columns(
        [
            pl.col("version_split").struct.field("field_0").cast(pl.Int32).alias("pydantic_major"),
            pl.col("version_split").struct.field("field_1").cast(pl.Int32).alias("pydantic_minor"),
            pl.col("version_split").struct.field("field_2").cast(pl.Int32).alias("pydantic_patch"),
        ]
    )

    # pydantic_versions = sorted(avg_df["pydantic_version"].unique())
    strict_model_values = ["false", "true"]

    # Create subplots with shared x-axis
    n_rows = 3
    fig = make_subplots(
        rows=n_rows,
        cols=1,
        shared_xaxes=False,
        vertical_spacing=0.1,
        subplot_titles=(
            "Average Cold Import Time",
            "Average Cold Validation Time",
            "Average Warm Validation Time",
        ),
    )

    # Colors for strict_models
    colors = {"false": "rgb(31, 119, 180)", "true": "rgb(255, 127, 14)"}

    # Plot Import Time
    for strict_model in strict_model_values:
        subset = avg_df.filter(pl.col("strict_models") == strict_model).sort(
            by=["pydantic_major", "pydantic_minor", "pydantic_patch"]
        )
        name = (
            "Strict (mymodels.strict.models)"
            if strict_model == "true"
            else "Partial (mymodels.models)"
        )
        fig.add_trace(
            go.Bar(
                x=subset["pydantic_version"],
                y=subset["import_time_s"],
                name=name,
                marker_color=colors[strict_model],
                text=[f"{y:.3f}" for y in subset["import_time_s"]],
                textposition="auto",
            ),
            row=1,
            col=1,
        )
        fig.add_trace(
            go.Bar(
                x=subset["pydantic_version"],
                y=subset["validate_time_s"],
                name=name,
                marker_color=colors[strict_model],
                showlegend=False,
                text=[f"{y:.4f}" for y in subset["validate_time_s"]],
                textposition="auto",
            ),
            row=2,
            col=1,
        )
        fig.add_trace(
            go.Bar(
                x=subset["pydantic_version"],
                y=subset["validate_again_time_s"],
                name=name,
                marker_color=colors[strict_model],
                showlegend=False,
                text=[f"{y:.6f}" for y in subset["validate_again_time_s"]],
                textposition="auto",
            ),
            row=3,
            col=1,
        )

    # Update axes titles
    for irow in range(1, n_rows + 1):
        fig.update_xaxes(title_text="Pydantic Version", row=irow, col=1)
        fig.update_yaxes(title_text="Time (seconds)", row=irow, col=1)

    # Update layout
    fig.update_layout(
        title_text="Import and Validation Performance, by Pydantic Version and Models Variant",
        height=1400,
        legend_title="Models Variant",
    )

    # Save the plot
    fig.write_image(save_plot_path, width=1200, height=1000, scale=2)

    # Show the plot
    fig.show()


def update_facet_title(a: go.layout.Annotation):
    text: str = a.text
    return a.update(text=text.split("=")[1].replace("_", " ").title())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Plot benchmark results.")
    parser.add_argument(
        "--results-file",
        type=str,
        default=None,
        help="Specify a custom path for the results CSV file.",
    )
    parser.add_argument(
        "--save-plot",
        type=str,
        default=None,
        help="Specify a custom path for the plot PNG file.",
    )

    args = parser.parse_args()

    plot_benchmark_results(results_file=args.results_file, save_plot=args.save_plot)
