import requests
from bs4 import BeautifulSoup

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
        }

r = requests.get('https://www.phoenixcontact.com/online/portal/ru/?uri=pxc-oc-itemdetail:pid=3210268&library=ruru&pcck=P-22-03-01-02&tab=2&selectedCategory=ALL', headers=headers)
r.status_code
rr = r.text


# копируем считанные данные в текстовый файл, для последующей обработки
txt_file = open('txt', 'w', encoding='utf-8')
txt_file.write(rr)
txt_file.close()

# загружаем данные в парсер
soup = BeautifulSoup(rr, "html.parser")
# считываем данные
dirty_desc = soup.find_all("div", class_="pxc-prod-detail-txt")
dirty_short_desc = soup.h1
dirty_tables = soup.find("table", class_="pxc-tbl")

print(dirty_tables)
soup.clear()
# убираем лишний текст
desc = str(dirty_tables)
soup = BeautifulSoup(desc, "html.parser")
desc = soup.get_text()
desc1 = desc.split("\n")
desc2 = []

for a in desc1:
    if a != '':
        desc2.append(a)

b = 0
for a in desc2:
    b += 1
    if a == 'Количество ярусов':
        num_of_lev = desc2[b]
        print(num_of_lev)

print(desc2)