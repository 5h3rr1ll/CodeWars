#! /usr/bin/env python
# -*- coding: utf-8 -*-

def accum(s):
    down = len(s)
    for i in s:
        print(i * 5, sep = "-", end = "")
        down -= 1

accum("ZpglnRxqenU")
