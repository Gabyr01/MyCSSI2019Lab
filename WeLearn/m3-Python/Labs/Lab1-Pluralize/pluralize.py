
def pluralize(word):
    if word[-3:]=="ife":
        print(word[:-3] + "ives")
    elif word[-2:] == "sh" or word[-2:] == "ch":
        print(  word + "es")
    elif word[-2:] == "us":
        print(word[:-2] + "i")
    elif word[-2:]=="ay" or word[-2:]=="oy" or word[-2:]=="ey" or word[-2:]=="uy":
        print(word + "s")
    elif( word[-1:]=="y"):
     print(word[:-1] + "ies")
    else:
        print word+'s'

    #else:
    #     return word

pluralize('cat')
    #print(word[:-1] + 's')
