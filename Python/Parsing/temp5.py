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
        dirty_tech_data = soup.find_all("table", class_="pxc-tbl")
       # len(soup.find_all("table", class_="pxc-tbl")) can count num of tables, and split them
       # test = soup.find_all("table", class_="pxc-tbl")[0]

        soup.clear()
        # выгружаем текст
        desc = str(dirty_desc)
        soup = BeautifulSoup(desc, "html.parser")
        desc = soup.get_text()
        desc = desc.split("\n")
        # выгружаем текст
        short_desc = str(dirty_short_desc)
        soup = BeautifulSoup(short_desc, "html.parser")
        short_desc = soup.get_text()
        # выгружаем текст
        tech_data = str(dirty_tech_data)
        soup = BeautifulSoup(tech_data, "html.parser")
        tech_data = soup.get_text()
        tech_data = tech_data.split("\n")
        tech_data1 = []
        # пересобираем текстовые данные
        for a in tech_data:
            if a != '' and a != '[' and a != ']' and a !=', ':
                tech_data1.append(a)

        # загружаем данные в парсер
        soup = BeautifulSoup(s_text, "html.parser")
        # считываем данные
        dirty_comm_data = soup.find("table", class_="pxc-tbl")
        soup.clear()
        # выгружаем текст
        comm_data = str(dirty_comm_data)
        soup = BeautifulSoup(comm_data, "html.parser")
        comm_data = soup.get_text()
        comm_data = comm_data.split("\n")
        comm_data1 = []
        # пересобираем текстовые данные
        for a in comm_data:
            if a != '':
                comm_data1.append(a)

        return desc[1], short_desc, tech_data1, comm_data1

def tech_data(i):


print(data_search('2320908'))