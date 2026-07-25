import math
x=int(input("Enter the 1st side"))
y=int(input("Enter the 2nd side"))      
z=int(input("Enter the 3rd side"))
a=float((x+y+z)/2)
b=math.sqrt(a*(a-x)*(a-y)*(a-z))
print("The Area is:",b)      
