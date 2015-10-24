#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Path markers
"""

from rebulk import Rebulk, Match

from rebulk.utils import find_all

PATH_MARKER = Rebulk()
PATH_MARKER.defaults(name="path", marker=True)


def mark_path(input_string):
    """
    Functional pattern to mark path elements.

    :param input_string:
    :return:
    """
    indices = list(find_all(input_string, '/'))
    indices += list(find_all(input_string, r'\\'))
    indices += [-1, len(input_string)]

    indices.sort()

    ret = []
    for i in range(0, len(indices) - 1):
        ret.append(Match(indices[i] + 1, indices[i + 1]))

    return ret


PATH_MARKER.functional(mark_path)