'''firstword = str(input("Input first word: "))
Secondword = str(input("Input second word: "))'''

def CommonWords(a, b):
    InCommon = ""
    for i in a.lower():
        for x in b.lower():
            if i == x:
                if i in InCommon:
                    continue
                else:
                    InCommon += str(i + ", ")
            
            
    return print(f"Common letters: {InCommon}")

CommonWords("umbrella","bradley")