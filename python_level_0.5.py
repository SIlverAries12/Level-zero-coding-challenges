
def area (a,b,c):
   s = 0.5*(a + b + c)
   output = (s*((s-a)*(s-b)*(s-c))) ** 0.5
   print(str(output))

area(3, 4, 5) 