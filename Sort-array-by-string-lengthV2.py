#! /usr/bin/env python
# -*- coding: utf-8 -*-


def sort_by_length(arr):
	# sorted is a build-in-funktion, which takes key-word-arguments. the first argument
    # is the object you would like to iterate thru, the second a "key" you want to use as base for your sort.
    # the last arguement, which i didn't use, is to do it reverse or not, whit a bool so True or False.
    return sorted(arr, key=len)
