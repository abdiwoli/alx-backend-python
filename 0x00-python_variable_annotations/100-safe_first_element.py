#!/usr/bin/env python3
""" advanced tasks """
from typing import Iterable, Sequence, List, Tuple, Any, Union

NoneType = type(None)


def safe_first_element(lst: Sequence[Any]) -> Union[Any, NoneType]:
    """ add anation to paramaters"""
    if lst:
        return lst[0]
    else:
        return None
