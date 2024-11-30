import datetime
import json
from pathlib import Path

import pytest

import mymodels.models as mc
from mymodels.tools import (
    dump_json_as,
    model_dump,
    model_dump_json,
    validate_as,
    validate_json_as,
)


class DateTimeModel(mc.BaseModel):
    dt: datetime.datetime


ANYMODEL_NAMES = [
    "AnyClass129",
    "AnyClass124",
    "AnyClass128",
    "AnyClass130",
    "AnyClass132",
]


@pytest.mark.parametrize("anymodel_name", ANYMODEL_NAMES)
def test_validate_dump(anymodel_name: type[mc.Class35], shared_datadir: Path):
    anymodel = getattr(mc, anymodel_name)
    objs_path = shared_datadir / f"{anymodel_name}.json"
    with open(objs_path) as f:
        objs_data = json.load(f)
    objs: list[mc.Class35] = validate_as(list[anymodel], objs_data)
    for obj_data, obj in zip(objs_data, objs):
        assert obj.model_type == obj.__class__.__name__
        serialized_dict = model_dump(obj)
        assert serialized_dict == obj_data


@pytest.mark.parametrize("anymodel_name", ANYMODEL_NAMES)
def test_validate_dump_json(anymodel_name: type[mc.Class35], shared_datadir: Path):
    anymodel = getattr(mc, anymodel_name)
    objs_path = shared_datadir / f"{anymodel_name}.json"
    with open(objs_path) as f:
        objs = validate_json_as(list[anymodel], f.read())
    objs_json = dump_json_as(list[anymodel], objs, indent=4)
    with open(objs_path) as f:
        objs_data = json.load(f)
    assert json.loads(objs_json) == objs_data
    for obj_data, obj in zip(objs_data, objs):
        assert json.loads(model_dump_json(obj)) == obj_data
