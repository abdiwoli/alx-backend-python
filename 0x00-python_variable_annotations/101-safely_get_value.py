#!/usr/bin/env python3
"""task 11 of the projrct"""
from typing import Any, Mapping, TypeVar, Union
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Doxumentation for safely"""
    if key in dct:
        return dct[key]
    else:
        return default
