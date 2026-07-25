x=int(input("ENTER THE MARKS IN PERCENTAGE"))
if (x>=90) and (x<=100):
    print("GRADE O")
elif (x>=80) and (x<90):
    print("GRADE E")
elif (x>=70) and (x<80):  
    print("GRADE A")
elif (x>=60) and (x<70):     
    print("GRADE B")
elif (x>=50) and (x<60):  
    print("GRADE C") 
elif (x>=40) and (x<50):          
    print("GRADE D")   
elif (x<40):
    print("FAIL")
else:
    print("ERROR!!")