a = ["X..",
    "XX.",
    "XO."]
b = str(a[0])
c = str(a[1])
d = str(a[2])
e = []
if b[0] == b[1] == b[2]:
    e.append(b[0])
if c[0] == c[1] == c[2]:
    e.append(c[0])
if d[0] == d[1] == d[2]:
    e.append(d[0])
if b[0] == c[0] == d[0]:
    e.append(b[0])
if b[1] == c[1] == d[1]:
    e.append(b[1])
if b[2] == c[2] == d[2]:
    e.append(b[2])
if b[0] == c[1] == d[2]:
    e.append(b[0])
if b[2] == c[1] == d[0]:
    e.append(b[2])

if len(e) == 0:
    return "D"
if len(e) == 1:
    if e == ".":
        return "D"
    return e[0]
if len(e) > 1:
    for i in

print(e)

