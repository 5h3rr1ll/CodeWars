#!/usr/bin/env python

def encrypt_this(text):
    lstOfWords = text.split(" ")
    returnString = ""
    if len(lstOfWords) < 1:
        return returnString
    else:
        for word in lstOfWords:
            if len(word) == 1:
                returnString += str(ord(word[0])) + " "
            elif len(word) == 2:
                returnString += str(ord(word[0])) + word[1] + " "
            elif len(word) == 3:
                returnString += str(ord(word[0])) + word[-1] + word[1] + " "
            elif len(word) > 3:
                returnString += str(ord(word[0])) + word[-1] + word[2:-1] + word[1] + " "
        return returnString.strip()


encrypt_this("")
encrypt_this("A wise old owl lived in an oak")
encrypt_this("The more he saw the less he spoke")
encrypt_this("The less he spoke the more he heard")
encrypt_this("Why can we not all be like that wise old bird")
encrypt_this("Thank you Piotr for all your help")
# encrypt_this("The more he saw the less he spoke")
