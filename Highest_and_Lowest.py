#! /usr/bin/env python
# -*- coding: utf-8 -*-

def high_and_low(numbers):
    '''returns you the highest and the lowest number out of a string'''
    #needed this variable to store the values as integer
    lst2 = []
    #to get rid of the empty spaces
    numbers = numbers.split(" ")
    for i in numbers:
        '''safe the string numbers as an int, otherwise I don't get the real max,
        min of the numbers'''
        i = int(i)
        lst2.append(i)
    # Without the string.format() I always got tuples
    return "{} {}".format(max(lst2), min(lst2))

print(high_and_low("1 2 3 4 5"))  # return "5 1"
print(high_and_low("1 2 -3 4 5")) # return "5 -3"
print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6")) # return "542 -214"
