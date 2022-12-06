#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a += (0, 0)[len(tuple_a):]
    tuple_b += (0, 0)[len(tuple_b):]
    tuple_a = tuple_a[:2]
    tuple_b = tuple_b[:2]
    return tuple(x + y for x, y in zip(tuple_a, tuple_b))
