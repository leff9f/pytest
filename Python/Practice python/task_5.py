#searching a palindrom
a = [5, 10, 15, 20, 20, 15, 10, 5]
b = [5, 15, 20, 40, 30, 15, 5]
c = len(b)
d = 1
for i in b[:c//2]:
    if i == b[c-d]:
        print("palindrom")
    else:
        print("not palindrom")
    d += 1

