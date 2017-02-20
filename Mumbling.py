#! /usr/bin/env python
# -*- coding: utf-8 -*-

def accum(s):
    down = len(s)
    string = ""
    for i in s:
        string += i * (len(s) + 1 - down) + "-"
        string = string.title()
        down -= 1
    string = string[:-1]
    print(string)

accum("ZpglnRxqenU")
