#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pydantic.version import VERSION as PYDANTIC_VERSION

PYDANTIC_V2 = PYDANTIC_VERSION.startswith("2.")
