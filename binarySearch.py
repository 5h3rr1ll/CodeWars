#!/usr/bin/env python

import sys

userInput = int(sys.argv[1])

list = [1,2,3,4,5,6,7,8,9,10]

counter = 0

def binSearch(list, searchNum = userInput,index=0,operator=None):
    print("Index Top",index)
    global counter
    prin(list)
    #sorts the list in case it's not sorted
    sortLst = list.sort()
    #index of the middle of the list
    mid = int(len(list)/2)

    if list[mid] == searchNum:
        print("In 1th If","- List mid:",mid,"New Index:",index,"Search:",searchNum,"- New list:",list[:mid])
        counter += 1
        if index == 0:
            print("Counter:",counter,"Postion:",mid, "Final Index:",index)
            return list.index(list[mid])
        if operator == 0:
            print("operator:",operator)
            index = index - mid
            print("Index:",index)
        else:
            print("operator:",operator)
            index = index  + mid
            print("Index:",index)
        print("Counter:",counter,"Postion:",mid, "Final Index:",index)
        return list.index(list[mid])
    elif list[mid] > searchNum:
        counter += 1
        print("In 2nd If","- List mid:",mid,"New Index:",index,"- New list:",list[:mid])
        if mid < index:
            mid, index = index, mid
            print("Switched mid and index! Mid is now:",mid,"Index:",index)
        binSearch(list[:mid],searchNum,index= mid-index, operator=0)
    elif list[mid] < searchNum:
        counter += 1
        print("In 3rd If","- List mid:",mid,"New Index:",index,"- New list:",list[mid:])
        binSearch(list[mid:],searchNum,index=mid+index, operator=1)


if __name__ == "__main__":
    binSearch(list)
