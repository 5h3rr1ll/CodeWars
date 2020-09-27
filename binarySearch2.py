#!/usr/bin/env python

import sys
from math import floor, ceil

value = int(sys.argv[1])
valueOddOrEven = sys.argv[2]

list = []
oddList = [1,2,3,4,5]
evenList = [1,2,3,4,5,6,7,8,9,10]


if valueOddOrEven == "o":
    list = oddList
else:
    list = evenList

counter = 0
#the operator tells you if the last action went left direction (subtraction) in
#the right direction (addition) It starts with operator 1 cause the index is settings
#to zero and if the algorithm it's at the first try the result must be index=1
def binSearch2(list, value = value, index=0,operator=1):
    global counter
    print("Start function:","List:",list,"Index:",index,"Operator:",operator,"Counter:",counter)
    #checks if list has a odd amount of objects, goes into if-tree if True
    if len(list) % 2 != 0:
        print("list has ODD number of objects")
        #this case is should only be true when the searched value is in the
        #MIDDLE of the List
        if list[floor(len(list)/2)] == value:
            print("it'fits, but is it plus or minus?")
            counter += 1
            if operator == 1:
                print("it's Plus!")
                index = index + floor(len(list)/2)
                print("fertig 1a","Index:",index,"Counter:",counter,"Operator:",operator)
            else:
                print("it's minus")
                index = index - floor(len(list)/2)
                print("fertig 1b","Index:",index,"Counter:",counter,"Operator:",operator)
        elif list[floor(len(list)/2)] > value:
            print("Middel Value is BIGGER than the searched one!")
            counter += 1
            #it's important that the new list becomes created after the index became
            #set otherwise the index is based on the new list and not on the current
            #one
            index = index + ceil(len(list)/2)
            list = list[:floor(len(list)/2)]
            operator = 0
            binSearch2(list,value,index,operator)
        else:
            print("Middle Value is SMALLER then searched value")
            counter += 1
            index = floor(len(list)/2) + 1
            list = list[floor(len(list)/2+1):]
            operator = 1
            binSearch2(list,value,index,operator)
    #else case for list with EVEN number of objects
    else:
        print("list has EVEN number of objects")
        #figurs out it the right value of the two middle values is bigger than
        #search value, so we need to search in the left half of the list
        if list[int(len(list)/2)] == value:
            print("Right Value of the middle is bigger than searched value!")
            #this only should be true if the LEFT of the two middle values
            #is the searched one
            if list[int(len(list)/2)] == value:
                print("Yeah! Fits! But + or - ?")
                counter += 1
                if operator == 1:
                    print("It's +")
                    index = index + int(len(list)/2)
                    print("fertig 2a","Index:",index,"Counter:",counter)
                else:
                    print("It's -")
                    index = index - int(len(list)/2)
                    print("fertig 2b","Index:",index,"Counter:",counter)
        #Here we will work with the RIGHT half of the list.
        elif list[int(len(list)/2)-1] == value:
            #this only should be true if the RIGHT of the two middle values
            #is the searched one
            if operator == 1:
                index = index + int(len(list)/2)-1
                print("fertig 3a","Index:",index,"Counter:",counter)
            else:
                index = index - int(len(list)/2)
                print("fertig 3b","Index:",index,"Counter:",counter)
        elif list[int(len(list)/2)] > value:
            print("We need to work on with the LEFT HALF of the list")
            counter += 1
            index = int(len(list)/2-1)
            operator = 0
            binSearch2(list[:list[int(len(list)/2)-1]],value,index,operator)
        elif list[int(len(list)/2)-1] < value:
            print("We need to work on with the RIGHT HALF of the list")
            counter += 1
            index = index + int(len(list)/2)
            binSearch2(list[int(len(list)/2):],value,index,operator)
        else:
            print("Tja!")


if __name__ == "__main__":
    binSearch2(list)
