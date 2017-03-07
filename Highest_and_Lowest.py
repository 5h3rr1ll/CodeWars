#! /usr/bin/env python
# -*- coding: utf-8 -*-

def high_and_low(numbers):
    lst2 = []
    numbers = numbers.split(" ")
    for i in numbers:
        i = int(i)
        lst2.append(i)
        print(lst2)
    return "{} {}".format(max(lst2), min(lst2))

# print(high_and_low("1 2 3 4 5"))  # return "5 1"
# print(high_and_low("1 2 -3 4 5")) # return "5 -3"
print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6")) # return "9 -5"
