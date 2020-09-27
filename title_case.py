def title_case(title=None, minor_words=None):
    lst = []
    if title == "":
        return ""
    elif minor_words == None:
        lst = [word.title() for word in title.split()]
        return " ".join(lst)
    else:
        split_string = [word.lower() for word in title.split()]
        split_exceptions =[word.lower() for word in minor_words.split()]
        counter = 0

        for  word in split_string:
            if counter == 0:
                lst.append(word.title())
                counter = 1
            else:
                if word in split_exceptions:
                    lst.append(word.lower())
                else:
                    lst.append(word.title())

        return " ".join(lst)

title_case('a clash of KINGS', 'a an the of') # should return: 'A Clash of Kings'
title_case('THE WIND IN THE WILLOWS', 'The In') # should return: 'The Wind in the Willows'
title_case('the quick brown fox') # should return: 'The Quick Brown Fox'
