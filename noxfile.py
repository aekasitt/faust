from pathlib import Path

import nox
import nox.command

__DIR__ = Path(__file__).parent

nox.options.sessions = ["test"]

BENCHMARK_REPEAT = 20


@nox.session(venv_backend="uv")
@nox.parametrize("pydantic", ["1.10.18", "2.10.2"], ids=["pydantic-v1", "pydantic-v2"])
def test(session: nox.Session, pydantic: str):
    session.run_install(
        "uv", "sync", "--frozen", env={"UV_PROJECT_ENVIRONMENT": session.virtualenv.location}
    )
    session.install(f"pydantic=={pydantic}")
    session.run("pytest", "-svv")


@nox.session(venv_backend="uv")
@nox.parametrize(
    "pydantic",
    [
        "1.10.18",
        # "2.6.3",
        "2.7.2",
        "2.8.2",
        "2.9.2",
        "2.10.2",
    ],
    ids=[
        "pydantic-v1",
        # "pydantic-v2.6",
        "pydantic-v2.7",
        "pydantic-v2.8",
        "pydantic-v2.9",
        "pydantic-v2.10",
    ],
)
def benchmark(session: nox.Session, pydantic: str):
    session.run_install(
        "uv", "sync", "--frozen", env={"UV_PROJECT_ENVIRONMENT": session.virtualenv.location}
    )
    session.install(f"pydantic=={pydantic}")

    session.run("python", "bench/run.py", "--no-save")  # Warmup
    repeat = BENCHMARK_REPEAT
    for _ in range(repeat):
        session.run("python", "bench/run.py")

    session.run("python", "bench/run.py", "--strict-models", "--no-save")  # Warmup
    for _ in range(repeat):
        session.run("python", "bench/run.py", "--strict-models")

    # Generate plot of results
    session.run("python", "bench/plot.py")


@nox.session(python=False)
def format(session: nox.Session):  # noqa: A001
    session.run("ruff", "check", "--fix")
    session.run("ruff", "format")


@nox.session(python=False)
def lint(session: nox.Session):
    session.run("ruff", "check", "--no-fix")
    session.run("ruff", "format", "--check")
