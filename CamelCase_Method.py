def camel_case(string):
    if string == "":
        return ""
    else:
        string = string.strip()
        lstOfWords = string.split(" ")
        returnString = ""

        for word in lstOfWords:
            word =  word.strip(" ")
            returnString += word[0].upper()+word[1:]
    return(returnString)




camel_case("test case")
camel_case("camel case method")
camel_case("say hello ")
camel_case(" camel case word")
camel_case("")
