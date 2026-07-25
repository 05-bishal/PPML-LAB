x=int(input("ENTER THE NO."))
for i in range(2,x):
    d=0
    for j in range(1,i+1):
        if i%j==0:
            d=d+1;
    if d==2:
        d=0
        x=i+2
        for k in range(1,x+1):
            if x%k==0:
                d=d+1
        if d==2:
            print("(%d,%d)"%(i,x))                
        