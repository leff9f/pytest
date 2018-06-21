
def func(s,d):
    res = []
    for i in s:
        if i in d:
            res.append(i)
    return res


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

d = func(a, b)

print('good: '+str(d))