#!/usr/bin/env python3
# -*- coding: utf-8 -*-

### Standard packages ###
from typing import Literal

VALIDATOR: Literal["msgspec", "pydantic-v1", "pydantic-v2"] | None = None
try:
  from pydantic.version import VERSION

  if VERSION.startswith("2."):
    VALIDATOR = "pydantic-v2"
  else:
    VALIDATOR = "pydantic-v1"
except ImportError:
  VALIDATOR = "msgspec"


__all__: tuple[str, ...] = ("VALIDATOR",)
