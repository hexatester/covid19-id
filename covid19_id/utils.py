import cattr
from datetime import date, datetime
from dateutil.parser import parse as parse_datetime
from typing import Generic, TypeVar

from . import __version__

VInt = TypeVar("VInt", bound=int)


class ValueInt(Generic[VInt]):
    pass


def get_headers():
    return {
        "Connection": "keep-alive",
        "User-Agent": f"pypi.org/project/covid19-id/{__version__}",
    }


def register_hooks():
    cattr.register_structure_hook(date, lambda d, t: parse_datetime(d).date())
    cattr.register_structure_hook(datetime, lambda d, t: parse_datetime(d))
    cattr.register_structure_hook(ValueInt, lambda d, t: d["value"])
