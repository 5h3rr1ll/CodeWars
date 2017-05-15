#! /usr/bin/env python
# -*- coding: utf-8 -*-


def sort_by_length(arr):

    """ Ziel: Die Strings sollen der Länge der Strings nach sortiert werden. Folgende
    Punkte müssen also geprüft werden: 1. Wie lang sind die geweiligen Strings?
    2. Welchen Index hat der jeweilige String? Danach wird die Sortioerung mit dem
    kürzesten String begeonnen."""

    wordLst = arr
    listIndex = []
    newLst = []
    n = 0
    word = ""
    for word in arr:
        lenWord = len(word)
        index =
        listIndex.append(len(word))

    for word in arr:
        pop = wordLst.pop(listIndex.index(min(listIndex)))
        index = listIndex.index(pop)
        arr = arr[index]
        print(arr)
        # word = arr[pop]
        # newLst.append(word)
        # # n += 1

    print("Jap!")
    return(newLst)

# sort_by_length(["beg", "life", "i", "to"]) # "i", "to", "beg", "life"],
# sort_by_length(["", "moderately", "brains", "pizza"])
# sort_by_length(["dog", "food", "a", "of"])
# sort_by_length(["", "dictionary", "eloquent", "bees"])
sort_by_length(["a longer sentence", "the longest sentence", "a short sentence"])

# tests = [
#     [["i", "to", "beg", "life"], ["beg", "life", "i", "to"]],
#     [["", "pizza", "brains", "moderately"], ["", "moderately", "brains", "pizza"]],
#     [["short", "longer", "longest"], ["longer", "longest", "short"]],
#     [["a", "of", "dog", "food"], ["dog", "food", "a", "of"]],
#     [["", "bees", "eloquent", "dictionary"], ["", "dictionary", "eloquent", "bees"]],
#     [["a short sentence", "a longer sentence", "the longest sentence"], ["a longer sentence", "the longest sentence", "a short sentence"]],
# ]
