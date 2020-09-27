def valid_parentheses(string):
    counter = 0

    for letter in string:
        if letter == "(":
            counter += 1
        elif letter == ")":
            counter -= 1
        if counter < 0:
            return False

    return counter == 0


valid_parentheses("  (") #,False)
valid_parentheses(")test") #,False)
valid_parentheses("") #,True)
valid_parentheses("hi())(") #,False)
valid_parentheses("hi(hi)()") #,True)
