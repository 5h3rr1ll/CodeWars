namen = [ {'name': 'Bart'}]

def namelist(names):

    string = ""
    b = ""

    for i in range(len(names)):
        b = names[i]
        b = b["name"]

        if i == len(names)-1 and len(names) > 1:
            string += " & " + b
        elif len(names) == 1:
            return b
        elif i == len(names)-2:
            string += b
        else:
            string += b + ", "

    print(string)
    return string

namelist(namen)
