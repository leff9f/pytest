import requests
from bs4 import BeautifulSoup

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
        }

r=requests.get('https://www.phoenixcontact.com/online/portal/ru/?uri=pxc-oc-itemdetail:pid=2320908&library=ruru&pcck=P-22-03-01-02&tab=1&selectedCategory=ALL', headers=headers)
rr=r.text
#print(rr)

txtfile=open('txt', 'w', encoding='utf-8')
txtfile.write(rr)
txtfile.close()

soup = BeautifulSoup(rr, "html.parser") #загружаем данные в парсер
stxt = soup.find_all("div", class_="pxc-prod-detail-txt")
soup.clear()

sxt=str(stxt)
soup = BeautifulSoup(sxt, "html.parser")
sxtclear=soup.get_text()
print(sxtclear)










