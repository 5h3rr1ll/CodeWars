def camel_case(string):
    print(" ".join([ x.title() for x in string.split(" ") if string != ""]).strip())




camel_case("test case")
camel_case("camel case method")
camel_case("say hello ")
camel_case(" camel case word")
camel_case("")
