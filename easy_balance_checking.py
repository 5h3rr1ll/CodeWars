#!/usr/bin/env python
import re
from statistics import mean

def balance(book):
    p = re.compile(r"(\w+.\w+)")
    lst = p.findall(book)
    lst2 = []
    lst3 = []
    original_balance = 0.00

    for i in lst:
        lst2.append(i.split(" "))

    print(lst2)

    for i in lst2:
        for x in i:
            lst3.append(x)

    print(lst3)

    if lst3[0][0].isalnum():
        original_balance = lst3.pop(0)
        original_balance = format(float(original_balance),".2f")
        original_balance_minus = float(original_balance)
        single_shoping_values =[]
        returnString = "Original Balance: "
        returnString += "%s\r\n"%(original_balance)

        while len(lst3):
            returnString += lst3.pop(0)+" "
            returnString += lst3.pop(0)+" "
            single_shoping_values.append(float(format(float(lst3[0]),".2f")))
            original_balance_minus -= float(lst3[0])
            single_value = lst3.pop(0)
            single_valueF = format(float(single_value),".2f")
            returnString += single_valueF + " Balance %.2f\r\n"%(original_balance_minus)

        returnString += "Total expense  %.2f\r\nAverage expense  %.2f" % (sum(single_shoping_values),mean(single_shoping_values))
        return(returnString)

b1 = """1000.00!=

125 Market !=:125.45
126 Hardware =34.95
127 Video! 7.45
128 Book :14.32
129 Gasoline ::16.10
"""


b2="""1233.00
125 Hardware;! 24.8?;
123 Flowers 93.5
127 Meat 120.90
120 Picture 34.00
124 Gasoline 11.00
123 Photos;! 71.4?;
122 Picture 93.5
132 Tyres;! 19.00,?;
129 Stamps 13.6
129 Fruits{} 17.6
129 Market;! 128.00?;
121 Gasoline;! 13.6?;"""


balance(b1)
# balance(b2)
