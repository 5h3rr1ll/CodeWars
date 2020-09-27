#!/usr/bin/env python
import random

list = []
oddList = [1,2,3,4,5]
evenList = range(10000)

def binSearch3(list,value,index=0):
    if len(list) == 0:
        # print("False")
        return False
    else:
        midpoint = int(len(list)//2)
        # print("midpoint:",midpoint,"index:",index)
        if list[midpoint]==value:
            index = index + midpoint
            # print("True")
            return True
        else:
            if value < list[midpoint]:
                if midpoint > index:
                    index = midpoint - index
                else:
                    index = index - midpoint
                return binSearch3(list[:midpoint],value,index)
            else:
                if midpoint > index:
                    index = midpoint + index
                else:
                    index = index + midpoint
                return binSearch3(list[midpoint:],value,index)


if __name__ == "__main__":
    binSearch3(oddList, random.randint(0, 1000000) )
    binSearch3(evenList,random.randint(0, 1000000))
