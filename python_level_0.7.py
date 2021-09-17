def cel_to_feh(a):
    fahrenheit = round((a * (9/5)) + 32, 2)
    print(fahrenheit)

cel_to_feh(21)

def feh_to_cel(b):
    celsius = round((b - 32) * (5/9), 2)
    print(celsius)

feh_to_cel(68)