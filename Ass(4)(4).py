def fun():
    a=0
    b=1
    print("THE SERIES:",a,b,end=' ')
    for i in range(13):
        c=a+b
        a=b
        b=c
        print(c,end=' ')    
fun()
