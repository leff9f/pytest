import os
A = os.listdir("d:/Downloads/data/")
j = 0
k = 0
for i in A:
    j += 1
    #print(j)
    f = open("d:/Downloads/data/"+i, 'r', encoding='utf-8', errors='ignore')
    data = f.read()
    f.close()
    A = "541074210571"

    if data.find(A) != -1:
        k+=1
        print(data[data.find(A)-100:data.find(A)+500])
print(k)
print(data)

