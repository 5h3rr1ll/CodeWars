#! /usr/bin/env python
# -*- coding: utf-8 -*-

def row_sum_odd_numbers(n):
    #need this to store a list of numbers which are odd
    lstOfOdds = []

    #to store the number which tells me how many objects my list should have
    counter = 0

    """ Pretty sure you can solce this for with fibbonacci, but I wans't able to do
    it with fibbonacci, so this is my way to figure out, how many objects you will
    need if your function get a valiu like 5 as an argument"""
    for i in range(n+1):
        counter += i

    number = 0

    """As long as the list is shorter than the numbers of objectet needed it won't
    stopp to increase number and check if it even or odd"""
    while len(lstOfOdds) <= (counter-1):
        if number % 2 != 0:
            lstOfOdds += [number]
            number += 1
        else:
            number += 1
    """ This step is about slicing. Slicing the list reverse."""
    return(sum(lstOfOdds[:-(n+1):-1]))
