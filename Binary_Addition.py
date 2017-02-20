#! /usr/bin/env python
# -*- coding: utf-8 -*-

def positive_sum(arr):
    res = 0

    for x in arr:
        if x > 0:
            res += x
            print(res)

positive_sum([1,2,3,4,5])
