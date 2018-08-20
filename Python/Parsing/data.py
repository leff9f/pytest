def data_import(i):
    from openpyxl import load_workbook
    import os

    wb = load_workbook(os.path.abspath("d:\OceanWork\PhoenixCo parsing\Terminals.xlsx"), read_only=True)  # open file
    sheet_terminals = wb['terminals']  # select work sheet

    d = sheet_terminals.max_row

    if i <= d:
        return sheet_terminals['G' + str(i)].value
    else:
        return "None"


def data_save(i, j, k):
    from openpyxl import load_workbook
    import os

    wb = load_workbook(os.path.abspath("d:\OceanWork\PhoenixCo parsing\Terminals.xlsx"))  # open file
    sheet = wb["ROPTerminals"]  # select work sheet
    sheet.cell(row=i, column=j).value = k
    wb.save(filename="d:\OceanWork\PhoenixCo parsing\Terminals.xlsx")


def data_num():
    from openpyxl import load_workbook
    import os

    wb = load_workbook(os.path.abspath("d:\OceanWork\PhoenixCo parsing\Terminals.xlsx"), read_only=True)  # open file
    sheet_terminals = wb['terminals']  # select work sheet

    i = sheet_terminals.max_row
    return i


def open_num_sync():
    temp_file = open('temp')
    last_used_num = temp_file.read()
    temp_file.close()
    return data_import(int(last_used_num))


def save_num_sync(last_used_num):
    temp_file = open('temp', 'w')
    temp_file.write(last_used_num)
    temp_file.close()


def data_search(i):
    import requests
    from bs4 import BeautifulSoup

    # описание заголовка для запроса
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
        }

    # запрос данных
    r = requests.get('https://www.phoenixcontact.com/online/portal/ru/?uri=pxc-oc-itemdetail:pid='+i+
                     '&library=ruru&pcck=P-22-03-01-02&tab=2&selectedCategory=ALL', headers=headers)
    s = requests.get('https://www.phoenixcontact.com/online/portal/ru/?uri=pxc-oc-itemdetail:pid='+i+
                     '&library=ruru&pcck=P-22-03-01-02&tab=1&selectedCategory=ALL', headers=headers)

    if r.status_code == requests.codes.ok and s.status_code == requests.codes.ok:
        # считываем текстовые данные
        r_text = r.text
        s_text = s.text
        # загружаем данные в парсер
        soup = BeautifulSoup(r_text, "html.parser")
        # считываем данные
        dirty_desc = soup.find_all("div", class_="pxc-prod-detail-txt")
        dirty_short_desc = soup.h1
        dirty_tech_data = soup.find("table", class_="pxc-tbl")
        soup.clear()
        # выгружаем текст
        desc = str(dirty_desc)
        soup = BeautifulSoup(desc, "html.parser")
        desc = soup.get_text()
        # выгружаем текст
        short_desc = str(dirty_short_desc)
        soup = BeautifulSoup(short_desc, "html.parser")
        short_desc = soup.get_text()
        # выгружаем текст
        tech_data = str(dirty_tech_data)
        soup = BeautifulSoup(tech_data, "html.parser")
        tech_data = soup.get_text()
        tech_data1 = tech_data.split("\n")
        tech_data2 = []
        # пересобираем текстовые данные
        for a in tech_data1:
            if a != '':
                tech_data2.append(a)

        # загружаем данные в парсер
        soup = BeautifulSoup(s_text, "html.parser")
        # считываем данные
        dirty_comm_data = soup.find("table", class_="pxc-tbl")
        soup.clear()
        # выгружаем текст
        comm_data = str(dirty_comm_data)
        soup = BeautifulSoup(comm_data, "html.parser")
        comm_data = soup.get_text()
        comm_data1 = comm_data.split("\n")
        comm_data2 = []
        # пересобираем текстовые данные
        for a in comm_data1:
            if a != '':
                comm_data2.append(a)

        return desc, short_desc, tech_data2, comm_data2


def image_search(i):
    import requests
    from bs4 import BeautifulSoup

    # описание заголовка для запроса
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    }
    # запрос данных
    im = requests.get('https://www.phoenixcontact.com/online/portal/ru/?uri=pxc-oc-itemdetail:pid='+i+
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

        return image_ad

#    url = "https://www.phoenixcontact.com/assets/images_pr/product_photos/large/25176_1000_int_04.jpg"
#    response = requests.get(url, headers=headers)
#    if response.status_code == 200:
#        with open(".sample.jpg", 'wb') as f:
#            f.write(response.content)
