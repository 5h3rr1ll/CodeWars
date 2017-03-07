#! /usr/bin/env python
# -*- coding: utf-8 -*-

def add_binary(a,b):
    """Returns the binary code of two numbers without the leading 0b and different
    endings."""
    # the ":b" within the {} does that the result of a + b become converted into binary
    return "{:b}".format(a + b)

print(add_binary(1,1))
print(add_binary(0,1))
print(add_binary(1,0))
print(add_binary(2,2))
print(add_binary(51,12))
