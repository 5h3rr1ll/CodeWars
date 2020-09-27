import string


def moving_shift(s, shift):
    divider = int(len(s)/5)
    splitted_string = []
    counter = 1
    for index in range(0, len(s), divider):
        sd
        splitted_string.append(s[index:index + divider])
    lst = []
    return_string = ""
    for char in s:
        if char.islower():
            if string_length > shift:
                index = string.ascii_lowercase.index(char)
                try:
                    return_string += string.ascii_lowercase[index + shift]
                except Exception as e:
                    print(f"Shift: {shift}", "if char is lower", "Error:", e)
                shift += 1
            elif string_length < shift:
                try:
                    return_string += string.ascii_lowercase[shift % string_length]
                except Exception as e:
                    print(f"Shift: {shift}", "if char is lower", "Error:", e)
        elif char.isupper():
            index = string.ascii_uppercase.index(char)
            return_string += string.ascii_uppercase[index + shift]
            shift += 1
    print(return_string)
    return return_string
    # print("Länge: ",len(s),"Es bleiben über: ", len(s) % 4, "Geteilt durch 5: ", len(s)/5)


def demoving_shift(s, shift):
    pass


s = "I should have known that you would have a perfect answer for me!!!"
shift = 1

moving_shift(s, shift)
