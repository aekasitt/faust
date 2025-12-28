#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from faust._compat import VALIDATOR

if VALIDATOR == "pydantic-v1":
  from faust._pydantic_v1.strict.models import *  # noqa: F403
elif VALIDATOR == "pydantic-v2":
  from faust._pydantic_v2.strict.models import *  # noqa: F403
