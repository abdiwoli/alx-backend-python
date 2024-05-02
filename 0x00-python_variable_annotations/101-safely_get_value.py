#!/usr/bin/env python3
""" 101-safely_get_value.py """
from typing import Iterable, Sequence
from typing import List, Tuple, Any, Union, Mapping, TypeVar


def safely_get_value(dct: Mapping, key: Any, default: Union[TypeVar(
        'T'), None] = None) -> Union[TypeVar('T'), type(None)]:
    """ function saveley get value """
    if key in dct:
        return dct[key]
    else:
        return default
