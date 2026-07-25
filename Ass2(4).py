x = int(input("ENTER A NUMBER: "))
if x <= 1:
    print("NOT A PERFECT NUMBER")
else:
    s=0
    for i in range(1, x):
        if x % i == 0:
            s += i
    if s==x:
        print("IT IS PERFECT NUMBER")
    else:
        print("NOT A PERFECT NUMBER")