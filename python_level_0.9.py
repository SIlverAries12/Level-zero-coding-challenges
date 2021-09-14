def AreVowels(b):
    empty_string = ""
    vowels = ["a","e", "i", "o", "u"]
    for i in b.lower():                             # .lower() for dealing with capital letters
        if i in vowels:
            if i in empty_string:
                continue
            else:
                empty_string += str(i + ", ")
    empty_string = empty_string[0:-2]               # used tring slicing to remove the last ", " after the loop ends
    return print(f"Vowels: {empty_string}")

AreVowels("Amazing guy")