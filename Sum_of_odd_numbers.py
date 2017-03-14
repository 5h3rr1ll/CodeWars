#! /usr/bin/env python
# -*- coding: utf-8 -*-

def row_sum_odd_numbers(n):
    '''Die eingegebene Zahl gibt die Reihe in einem Dreieck wieder, das aus ung-
    aden Zahlen besteht. In Jeder Reihe kommt eine Undgerade Zahl hinzu. In Reihe
    1 ist also eine ungerade Zahl, in Reihe 2, zwei ungeraden Zahlen usw. Die Zahlen
    einer Reihe werde addiert und von der Funktion zurückgegeben.'''

    #Zu erstest benötige ich eine Liste die mir die Zahlen für jede Reiehe zusammenfasst

    lstOfOdds = []

    counter = 0

    for i in range(n+1):
        counter += i

    number = 0

    while len(lstOfOdds) <= (counter-1):

        if number % 2 != 0:

            lstOfOdds += [number]
            number += 1
        else:

            number += 1
            
    return(sum(lstOfOdds[:-(n+1):-1]))


row_sum_odd_numbers(3)
