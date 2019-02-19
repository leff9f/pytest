import urllib.request

link=urllib.request.urlopen('https://www.rittal.com/ru-ru/product/show/variantdetail.action?categoryPath=/PG0001/PG0168KLIMA1/PGR1932KLIMA1/PG0201KLIMA1/PRO0299KLIMA&productID=3237100')

lines=link.readlines()
link.close()

for i in range(len(lines)):
   lines[i]=lines[i].decode('utf-8')

for i in range(len(lines)):
    #Убираем все лишнее
    lines[i] = lines[i].replace('\t\t\t<li>', '')
    lines[i] = lines[i].replace('\"', '')
    lines[i] = lines[i].replace('<a href=', '')
    lines[i] = lines[i].replace('target=_blank>', '')
    lines[i] = lines[i].replace('</a></li>', '')
    lines[i] = lines[i].replace('</ul>', '')
    lines[i] = lines[i].replace("\r\n", '')
    lines[i] = lines[i].replace("\n", '')

print(lines)




