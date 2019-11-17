def frequency_sort(items):
    lst = []
    lstint = []
    lstres = []
    for i in items:
        if lst.count(i) <= 0:
            lst.append(i)
    for j in lst:
        lstint.append(str(j)*items.count(j))
    print(lstint)
    for k in range(1, len(lstint)):
        for m in range(0, len(lstint)-k):
            if len(lstint[m]) < len(lstint[m+1]):
                lstint[m], lstint[m+1] = lstint[m+1], lstint[m]
    for n in lstint:
        for o in n:
            lstres.append(o)
    print(lstres)



frequency_sort([4, 6, 2, 2, 6, 3, 3, 3, 4, 4, 4])
#frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])
#frequency_sort([17, 99, 42])
frequency_sort([])
frequency_sort([1])


"""
def frequency_sort(items):
    b = len(items)
    lst = [0]*len(items)
    c = 0
    for i in items[0:b]:
        if items.count(i) > c:
            lst.append(i)
        c = items.count(i)
    print(lst)
"""
