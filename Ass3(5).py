x = input("ENTER THE STRING: ")
w=x.split()
for i in w:
    if len(i) % 2 == 0:
        print("EVEN LENGTH WORDS:", i)
