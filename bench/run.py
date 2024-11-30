import argparse
import json
import platform
import time
from pathlib import Path
from typing import Optional

import polars as pl

BENCH_DIR = Path(__file__).parent
DATA_DIR = BENCH_DIR.parent / "tests" / "data"

DEFAULT_BENCH_RESULTS_PATH = BENCH_DIR / "results.csv"


def run_benchmark(results_file: Optional[str] = None, strict_models: bool = False):
    result = import_models_and_validate_data(strict_models=strict_models)

    machine_info = get_machine_info()
    context_info = get_context_info(strict_models)

    print("Machine Info:", machine_info)
    print("Context Info:", context_info)
    print("Benchmark Result:", result)

    if results_file:
        results_path = Path(results_file)
    else:
        results_path = DEFAULT_BENCH_RESULTS_PATH

    # Run info combines machine, context, and benchmark times info
    run_info = {**machine_info, **context_info, **result}

    # Load current results DataFrame
    results_df = load_results_dataframe(results_path)

    # Create a DataFrame with single row for new run data
    single_run_df = pl.DataFrame([run_info], schema=results_df.schema)

    # Concatenate the new DataFrame with the existing one
    results_df = pl.concat([results_df, single_run_df], how="vertical")

    # Save the updated DataFrame back to the CSV file
    results_df.write_csv(str(results_path))

    print(f"Results saved to {results_path}")


def load_results_dataframe(results_path: Path):
    schema = {
        "system": pl.String,
        "machine": pl.String,
        "arch": pl.String,
        "python_impl": pl.String,
        "python_version": pl.String,
        "pydantic_version": pl.String,
        "strict_models": pl.Boolean,
        "import_time_s": pl.Float32,
        "validate_time_s": pl.Float32,
    }
    if results_path.exists():
        # Load existing CSV into polars DataFrame
        return pl.read_csv(str(results_path))

    # Create an empty polars DataFrame
    return pl.DataFrame(schema=schema)


def get_machine_info() -> dict[str, str]:
    return {
        "system": platform.system(),
        "machine": platform.machine(),
        "arch": platform.architecture()[0],
        "python_impl": platform.python_implementation(),
        "python_version": platform.python_version(),
    }


def format_machine_id(machine_info: dict[str, str]) -> str:
    return "{}-{}-{}-{}-{}".format(
        machine_info["system"],
        machine_info["machine"],
        machine_info["arch"],
        machine_info["python_impl"],
        machine_info["python_version"],
    )


def get_context_info(strict_models: bool):
    from mymodels._compat import PYDANTIC_VERSION

    return {"pydantic_version": PYDANTIC_VERSION, "strict_models": strict_models}


def import_models_and_validate_data(strict_models: bool = False):
    t0 = time.time()
    if strict_models:
        from mymodels.strict.models import AnyClass122
    else:
        from mymodels.models import AnyClass122
    t1 = time.time()
    import_time_s = t1 - t0

    from mymodels.tools import validate_as

    data: list[dict] = []
    json_paths = DATA_DIR.glob("*.json")
    for json_path in json_paths:
        with open(json_path) as f:
            model_dicts = json.load(f)
        data.extend(model_dicts)

    t0 = time.time()
    validate_as(list[AnyClass122], data)
    t1 = time.time()
    validate_time_s = t1 - t0

    return {"import_time_s": import_time_s, "validate_time_s": validate_time_s}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Benchmarking script.")
    parser.add_argument(
        "--strict-models",
        action="store_true",
        help="Use strict models during benchmarking.",
    )
    parser.add_argument(
        "--results-file",
        type=str,
        default=None,
        help="Specify a custom path for the results CSV file.",
    )

    args = parser.parse_args()

    run_benchmark(results_file=args.results_file, strict_models=args.strict_models)
