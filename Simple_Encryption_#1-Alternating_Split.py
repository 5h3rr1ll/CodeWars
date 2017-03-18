#! /usr/bin/env python
# -*- coding: utf-8 -*-


def decrypt(encrypted_text, n):
    """ This function encrypts the string like follows: It devides the string into
    two parts of the same size. Then it interates thru the two hafls and adds index
    0 until n to a variable. In the end it returns the varibale with the decrypted
    string. """

        if encrypted_text == None or encrypted_text == []:
            print(encrypted_text)
        elif n <= 0:
            print(encrypted_text)
        elif encrypted_text.endswith('!'):
            text = encrypted_text[:-1]
            text2 = ""
            for t in range(n):
                for i in range(len(text)//(2)):
                    text2 += text[len(text)//(2):][i]
                    text2 += text[:len(text)//(2)][i]
                text = text2
                text2 = ""
            return(text + "!")
        else:
            text = encrypted_text
            a = ""
            for t in range(n):
                for i in range(len(text)//(2)):
                    a += text[len(text)//(2):][i]
                    a += text[:len(text)//(2)][i]
            return(a)

def encrypt(text, n):
    """ This function encrypts a string by adding first every second object of the
    string to a new variable and the every not second object and this so often you
    tell it to do it with n ."""

    if text == None or text == []:
        print(text)
    elif n <= 0:
        print(text)
    else:
        text = text[:-1]
        a = ""
        for t in range(n):
            for i in text[1::2]:
                a += i
            for i in text[::2]:
                a += i
            text = a
            a = ""
        print(text+"!")


encrypt("This is a test!", 0)
encrypt("This is a test!", 1)
encrypt("This is a test!", 2)
encrypt("This is a test!", 3)
encrypt("This is a test!", 4)
encrypt("This is a test!", -1)
encrypt("This kata is very interesting!", 1)

decrypt("This is a test!", 0)
decrypt("hsi  etTi sats!", 1)
decrypt("s eT ashi tist!", 2)
decrypt(" Tah itse sits!", 3)
decrypt("This is a test!", 4)
decrypt("This is a test!", -1)
decrypt("hskt svr neetn!Ti aai eyitrsig", 1)

encrypt("", 0)
decrypt("", 0)
encrypt(None, 0)
decrypt(None, 0)
