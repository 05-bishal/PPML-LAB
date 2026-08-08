L1=[]
L2=[]
for i in range(5):
    x=int(input("Enter The Element"))
    L1.append(x)
print("original",L1)
for j in range(5):
    L2.append(L1[j])
    if L1[j]%2!=0:
        L2[j]=L2[j]+5
print("Increased Value",L2)        