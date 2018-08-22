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
image_src = str(dirty_image_ad).split()
image_url_proc = image_src[3].lstrip("\"src=").rstrip("\"")
image_url_small = "https://www.phoenixcontact.com/"+image_url_proc
image_url_large = image_url_small.replace("small1", "large")
image_url_large = image_url_large.replace("int_01", "int_04")
#url = "https://www.phoenixcontact.com/assets/images_pr/product_photos/large/25176_1000_int_04.jpg"

print(image_url_large)