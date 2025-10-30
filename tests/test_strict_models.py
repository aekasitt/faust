#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import json
from pathlib import Path

import pytest

import faust.strict.models as models
from faust.tools import (
    dump_json_as,
    dump_json_file_as,
    model_dump,
    model_dump_json,
    validate_as,
    validate_json_as,
    validate_json_file_as,
)


class DateTimeModel(models.BaseModel):
    dt: datetime.datetime


ANYMODEL_NAMES = [
    "AnyClass129",
    "AnyClass124",
    "AnyClass128",
    "AnyClass130",
    "AnyClass132",
]


@pytest.mark.parametrize("anymodel_name", ANYMODEL_NAMES)
def test_validate_dump(anymodel_name: str, shared_datadir: Path):
    anymodel = getattr(models, anymodel_name)
    objs_path = shared_datadir / f"{anymodel_name}.json"
    with open(objs_path) as f:
        objs_data = json.load(f)
    objs: list[models.Class35] = validate_as(list[anymodel], objs_data)
    for obj_data, obj in zip(objs_data, objs):
        assert obj.model_type == obj.__class__.__name__
        serialized_dict = model_dump(obj)
        assert serialized_dict == obj_data


@pytest.mark.parametrize("anymodel_name", ANYMODEL_NAMES)
def test_validate_dump_json(anymodel_name: str, shared_datadir: Path):
    anymodel = getattr(models, anymodel_name)
    objs_path = shared_datadir / f"{anymodel_name}.json"
    with open(objs_path) as f:
        objs = validate_json_as(list[anymodel], f.read())
    objs_json = dump_json_as(list[anymodel], objs, indent=4)
    with open(objs_path) as f:
        objs_data = json.load(f)
    assert json.loads(objs_json) == objs_data
    for obj_data, obj in zip(objs_data, objs):
        assert json.loads(model_dump_json(obj)) == obj_data


@pytest.mark.parametrize("anymodel_name", ANYMODEL_NAMES)
def test_validate_dump_json_file(anymodel_name: str, shared_datadir: Path):
    anymodel = getattr(models, anymodel_name)
    objs_path = shared_datadir / f"{anymodel_name}.json"

    objs = validate_json_file_as(list[anymodel], objs_path)

    output_path = shared_datadir / f"__{objs_path.name}"
    dump_json_file_as(list[anymodel], objs, output_path)
    assert json.loads(output_path.read_text()) == json.loads(objs_path.read_text())
    output_path.unlink()
