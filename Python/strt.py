import param #импорт параметров из файла param, но необходимо указывать param.переменная
import re
from param import num2 #конкретное указание на переменную, которую требуется использовать в текущем файле

match=re.match('Hello[ \t]*(.*)world', 'Hello   python world')
print (match.group(1))
num3=100
print(param.num1+num2)

L = [123, 'ttt', 456]
print(len(L))
L = L+[5]
print(len(L))
print(L)

L.insert(0,'sdsad')
print(L)
M=[121,1]
M.sort() #сортировка
M.reverse() #реверс
print(M)
