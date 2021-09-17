def common_words(a, b):
    in_common = ""
    for i in a.lower():
        for x in b.lower():
            if i == x:
                if i in in_common:
                    continue
                else:
                    in_common += str(i + ", ")
            
    in_common = in_common[0: -2]        
    print(f"Common letters: {in_common}")

common_words("umbrella","bradley")