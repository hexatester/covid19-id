from typing import Generic

from covid19_id.utils import ValueInt, get_headers, register_hooks


def test_utils():
    assert issubclass(ValueInt, Generic)
    assert callable(get_headers)
    assert callable(register_hooks)
