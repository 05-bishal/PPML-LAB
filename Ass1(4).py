import math
a=int(input("Enter The Coefficient a"))
b=int(input("Enter The Coefficient b"))
c=int(input("Enter The Coefficient c"))
d=math.sqrt((b*b)-(4*a*c))
x=float((-b)+d)/(2*a)
y=float((-b)-d)/(2*a)
print("The 1st Root is",x)
print("The 2nd Root is",y)
