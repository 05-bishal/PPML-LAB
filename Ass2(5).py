x = input("ENTER THE STRING: ")
t = x.lower()
r = t[::-1]
print("REVERSED STRING:", r)

v = 0
c = 0
for i in r:
    if i in "aeiou":
        v += 1
    elif i.isalpha():
        c += 1

print("NO. OF VOWELS:", v)
print("NO. OF CONSONANTS:", c)

