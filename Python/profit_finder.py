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
    text = "СумДоход"


    tmp = (data[data.find("Документ")-1:data.find("/Документ")-1])
    tmp.find('СведНП НаимОрг=')
    exit()


#    if data.find(text) != -1:
#        k+=1
#        print(data[data.find(text)-100:data.find(text)+500])
#print(k)
#print(data)

