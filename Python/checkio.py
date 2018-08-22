txt = "aaAaaaaaaa1a"
txt1 = "A1213pokl"
text = "bAse730onE"

upper = False
lower = False
if len(txt) >= 10 and len(txt) <=64 and not txt.isalpha() and not txt.isdigit():
    for i in txt:
        if i.isupper():
            upper = True
        if i.islower():
            lower = True
if upper and lower:
    print("sad")
