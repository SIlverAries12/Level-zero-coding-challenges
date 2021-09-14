

def max_num(*args):

    biggestNum = args[0] # assuming the first value is the biggest
    for i in args:
        if i > biggestNum:  # compare subsequent number with previous number and updates if number is bigger
            biggestNum = i
    return print(biggestNum)


max_num(7,19,57,63,2)  