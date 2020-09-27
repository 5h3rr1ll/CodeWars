#!/usr/bin/env python
# -*- coding: utf-8 -*-

def cakes(recipe, available):
    lstRecipe = list(recipe)
    lstAvailable = list(available)
    allAvaiable = True
    possibelAmount = []

    for i in lstRecipe:
        if i in lstAvailable and available[i] >= recipe[i]:
            possibelAmount.append(available[i] // recipe[i])
        else:
            allAvaiable = False

    if allAvaiable == True:
        return min(possibelAmount)
    else:
        return 0



# test.describe('Testing Pete, the Baker')
# test.it('gives us the right number of cakes')

recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
# test.assert_equals(cakes(recipe, available), 2, 'Wrong result for example #1')
cakes(recipe, available)

recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available = {"sugar": 500, "flour": 2000, "milk": 2000}
# test.assert_equals(cakes(recipe, available), 0, 'Wrong result for example #2')
cakes(recipe, available)
