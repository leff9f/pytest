import requests
from bs4 import BeautifulSoup
from Classes import *
from data import *

# подсчет числа заказных номеров подготовленных для запросов
part_num_length = data_num()

# описание заголовка для запроса
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
        }

# импорт заказного номера для последующей обработки
part_num = open_num_sync()

# запрос данных
#a = data_search(part_num)
b = image_search(part_num)
print(b)

t1 = Terminals("text", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

print(t1.desc)

# сохранение последнего считанного заказного номер в файле temp !!!НЕ ЗАБЫТЬ!!!
#save_num_sync(str(100))