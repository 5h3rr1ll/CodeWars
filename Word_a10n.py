string = "elephant-ride"


def foo(string):
    try:
        if len(string) >= 4:
            new_word = ""
            new_word += string[0]
            new_word += str(len(string)-2)
            new_word += string[-1]
            return new_word
        else:
            return string
    except Exception as e:
        print(str(e), "Input String:", string)


def abbreviate(string):
    string = string
    lst = []
    lst2 = []
    if not string.isalpha():
        print("in if not")
        for c in string:
            if not c.isalpha():
                lst.append(string[:string.index(c)])
                lst.append(c)
                string = string[string.index(c)+1:]
                if string.isalpha():
                    print("In Break", string)
                    lst.append(string)
                    break
        print(lst)
        for e in lst:
            lst2.append(foo(e))
        return_string = "".join(lst2)
        print(f"Return String: {return_string}")
        return return_string
    else:
        return foo(string)


abbreviate(string)

# lst = []
# lst2 = []
#
#
# def bar(string):
#     for c in string:
#         if not c.isalpha():
#             lst.append(string[:string.index(c)])
#             string = string[string.index(c)+1:]
#             lst.append(c)
#
#
# bar(string2)
# for i in lst:
#     lst2.append(foo(i))
#
# new = "".join(lst2)
#
# print(lst)
# print(lst2)
# print(new)
