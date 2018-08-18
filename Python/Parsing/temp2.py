import requests
from bs4 import BeautifulSoup

# описание заголовка для запроса
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
}
# запрос данных
im = requests.get('https://www.phoenixcontact.com/online/portal/ru/?uri=pxc-oc-itemdetail:pid=' + '3044076' +
                  '&library=ruru&pcck=P-22-03-01-02&tab=1&selectedCategory=ALL', headers=headers)
if im.status_code == requests.codes.ok:
    # считываем текстовые данные
    im_text = im.text
    # загружаем данные в парсер
    soup = BeautifulSoup(im_text, "html.parser")
    # считываем данные
    dirty_image_ad = soup.find_all("img", class_="pxc-img")
    # выгружаем текст
    image_ad = str(dirty_image_ad)
    soup = BeautifulSoup(image_ad, "html.parser")
    image_ad = soup.get_text()

    print(dirty_image_ad)