x=int(input("enter the number:"))
f=1
if x<1:
    print("INVALID INPUT")
else:
    for i in range(1,x+1):
        f=f*i
print("THE FACTORIAL IS:",f)        
