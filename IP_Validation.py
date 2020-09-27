#!/usr/bin/env python

def is_valid_IP(strng):
    splitt = strng.split(".")
    onlyNum = []

    if splitt == "":
        return False
    else:
        for x in splitt:
            if x.isnumeric() and int(x) <= 255:
                onlyNum.append(x)
            else:
                return False

    for number in onlyNum:
        if len(number) > 1 and int(number[0]) == 0:
            return False
        elif len(onlyNum) < 4 or len(onlyNum) >= 5 :
            return False
        elif int(onlyNum[0]) == 0 and int(onlyNum[1]) == 0 and  int(onlyNum[2]) == 0 and  int(onlyNum[3]) == 0:
            return True

# is_valid_IP('1.2.3.4.5')

is_valid_IP('12.255.56.1')
is_valid_IP('')
is_valid_IP('abc.def.ghi.jkl')
is_valid_IP('123.456.789.0')
is_valid_IP('12.34.56')
is_valid_IP('12.34.56 .1')
is_valid_IP('12.34.56.-1')
is_valid_IP('123.045.067.089')
is_valid_IP('127.1.1.0')
is_valid_IP('0.0.0.0')
is_valid_IP('0.34.82.53')
is_valid_IP('192.168.1.300')
