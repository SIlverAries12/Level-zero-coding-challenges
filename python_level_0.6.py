def max_num(*args):

    biggestNum = args[0] 
    for i in args:
        if i > biggestNum:  
            biggestNum = i
    print(biggestNum)


max_num(7,19,57,63,2)  