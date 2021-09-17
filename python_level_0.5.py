import math

def area (a,b,c):
   s = 0.5*(a + b + c)
   output = math.sqrt(s*((s-a)*(s-b)*(s-c)))
   print(str(output))

area(3, 4, 5) 