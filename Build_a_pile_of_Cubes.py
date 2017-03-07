#! /usr/bin/env python
# -*- coding: utf-8 -*-

def find_nb(m):
    cube = 1
    volume = 0
    while volume < m:
        volume += cube**3
        if volume == m:
            return cube
        else:
            cube += 1
    return -1



print(find_nb(135440716410000))
# find_nb(24723578342962)
# find_nb(135440716410000)
# find_nb(40539911473216)
# find_nb(26825883955641)
