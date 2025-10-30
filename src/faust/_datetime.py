import datetime
from typing import Union

from mymodels._compat import PYDANTIC_V2

if PYDANTIC_V2:
  from pydantic.v1.datetime_parse import parse_datetime
else:
  from pydantic.datetime_parse import parse_datetime

StrBytesIntFloat = Union[str, bytes, int, float]


def datetime_isoformat_z(dt: datetime.datetime) -> str:
  """Convert a datetime object to ISO formatted string in Zulu time."""
  return as_datetime_z(dt).isoformat(timespec="microseconds").replace("+00:00", "Z")


def as_datetime_z(obj: Union[datetime.datetime, StrBytesIntFloat]) -> datetime.datetime:
  """Convert obj to UTC offset-aware datetime object."""
  dt = parse_datetime(obj)
  if dt.tzinfo == datetime.timezone.utc:
    return dt
  return (
    dt.replace(tzinfo=datetime.timezone.utc)
    if not dt.tzinfo
    else dt.astimezone(tz=datetime.timezone.utc)
  )
