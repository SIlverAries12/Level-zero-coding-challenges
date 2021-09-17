def max_num(*args):

    biggest_num = args[0] 
    for i in args:
        if i > biggest_num:  
            biggest_num = i
    print(biggest_num)


max_num(7,19,57,63,2)  