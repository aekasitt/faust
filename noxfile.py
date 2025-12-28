#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from argparse import ArgumentParser, Namespace
from collections.abc import Sequence

import nox

nox.options.sessions = ["test"]

BENCHMARK_REPEAT = 20


@nox.session(venv_backend="uv")
@nox.parametrize(
  "model_validator",
  [
    ("msgspec", "0.19.0"),
    ("pydantic", "1.10.18"),
    ("pydantic", "2.12.3"),
  ],
  ids=["msgspec", "pydantic-v1", "pydantic-v2"],
)
def test(session: nox.Session, model_validator: tuple[str, str]):
  libname, version = model_validator
  session.run_install(
    "uv", "sync", "--frozen", env={"UV_PROJECT_ENVIRONMENT": session.virtualenv.location}
  )
  session.install(f"{libname}=={version}")
  session.run("pytest", "-svv")


@nox.session(venv_backend="uv")
@nox.parametrize(
  "model_validator",
  [
    ("msgspec", "0.19.0"),
    ("pydantic", "1.10.18"),
    ("pydantic", "2.12.3"),
  ],
  ids=[
    "msgspec",
    "pydantic-v1",
    "pydantic-v2",
  ],
)
def benchmark(session: nox.Session, model_validator: tuple[str, str]):
  libname, version = model_validator
  args = _parse_benchmark_args(session.posargs)
  repeat: int = args.repeat
  results_file = args.results_file

  extra_args = (f"--results-file={results_file}",) if results_file else ()

  session.run_install(
    "uv", "sync", "--frozen", env={"UV_PROJECT_ENVIRONMENT": session.virtualenv.location}
  )
  session.install(f"{libname}=={version}")

  bench_arg_combos = (
    [],
    ["--strict-models"],
    ["--defer-build"],
    ["--strict-models", "--defer-build"],
  )
  for bench_args in bench_arg_combos:
    session.run("python", "src/faust/bench.py", "--no-save")  # Warmup
    for _ in range(repeat):
      session.run("python", "src/faust/bench.py", *bench_args, *extra_args)

  # Generate plot of results
  session.run("python", "src/faust/plot.py", *extra_args)


def _parse_benchmark_args(args: Sequence[str]) -> Namespace:
  parser: ArgumentParser = ArgumentParser(prog="nox -s benchmark")
  parser.add_argument("--repeat", type=int, default=BENCHMARK_REPEAT, help="Number of repetitions")
  parser.add_argument("--results-file", type=str, default=None, help="Results file path")
  return parser.parse_args(args)


@nox.session(python=False)
def format(session: nox.Session):  # noqa: A001
  session.run("ruff", "check", "--fix")
  session.run("ruff", "format")


@nox.session(python=False)
def lint(session: nox.Session):
  session.run("ruff", "check", "--no-fix")
  session.run("ruff", "format", "--check")
