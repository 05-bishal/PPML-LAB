num = []
print("Enter 10 integers:")
for i in range(5):
    t=int(input("Enter The Numbers"))
    num.append(t)
for j in range(len(num)-1):
    for k in range(len(num)-j-1):
        if num[k]>num[k+1]:
            num[k],num[k+1]=num[k+1],num[k]
print("Smallest No.",num[1])
print("Largest No.",num[-2])
 