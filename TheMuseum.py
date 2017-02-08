#! /usr/bin/env python
# -*- utf-8 -*-

def remove_smallest(numbers):
    if numbers == None:
        raise NotImplementedError("TODO: remove_smallest")
    else:
        numbers.remove(min(numbers))
    print(numbers)
    # del(min(numbers))


remove_smallest([1,2,3,4,5]) # [2,3,4,5]
remove_smallest([5,3,2,1,4]) # [5,3,2,4]
remove_smallest([2,2,1,2,1]) # [2,2,2,1]
