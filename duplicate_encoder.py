def duplicate_encode(word):
    print("".join(["(" if word.lower().count(char.lower()) == 1 else ")" for char in word]))
    return "".join(["(" if word.lower().count(char.lower()) == 1 else ")" for char in word])


duplicate_encode("din")  # ,"((("
duplicate_encode("recede")  # ,"()()()"
duplicate_encode("Success")  # ,")())())","should ignore case")
duplicate_encode("(( @")  # ,"))(("
