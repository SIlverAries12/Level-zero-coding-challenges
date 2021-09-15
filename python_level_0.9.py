def AreVowels(b):
    empty_string = ""
    vowels = ["a","e", "i", "o", "u"]
    for i in b.lower():                             
        if i in vowels:
            if i in empty_string:
                continue
            else:
                empty_string += str(i + ", ")
    empty_string = empty_string[0:-2]            
    print(f"Vowels: {empty_string}")

AreVowels("Amazing guy")