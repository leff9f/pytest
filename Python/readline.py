f=open('strt.py')
while True:
    line = f.readline()
    if not line: break
    print(line.upper(), end='')
f.close()

f1=open('for.py')
print(next(f1))
