"""
-------------------------------------
# -*- coding: utf-8 -*-
# @File    : _vector_cal.py
# @Software: PyCharm
-------------------------------------
"""


def to_vec_sub(p1, p2):
    return [p1[0] - p2[0], p1[1] - p2[1]]


def to_vec_add(p1, p2):
    return [p1[0] + p2[0], p1[1] + p2[1]]


def to_vec_times(c, p):
    return [p[0] * c, p[1] * c]


def to_vec_dot(p1, p2):
    return p1[0] * p2[0] + p1[1] * p2[1]
