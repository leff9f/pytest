from Classes import Terminals
from data import data_num, open_last_num, data_search
from data import image_search, image_download, data_import
from data import save_num_sync, data_save, input_check
from data import data_collect
import time
from multiprocessing import Pool

if __name__ == '__main__':
    # время выполнения
    tic = [time.time()]

    # подсчет числа заказных номеров подготовленных для запросов
    part_num_length = data_num()
    print('number of data: '+str(part_num_length))
    print('last used num: '+str(open_last_num()))
    # импорт заказного номера для последующей обработки
    part_num = data_import(open_last_num())

    # ввод числа считываемых данных
    x = input_check()

    r_address = ('https://www.phoenixcontact.com/online/portal/ru/?uri=pxc-oc-itemdetail:pid=' + '0818108' +
                         '&library=ruru&pcck=P-22-03-01-02&tab=2&selectedCategory=ALL')
    s_address = ('https://www.phoenixcontact.com/online/portal/ru/?uri=pxc-oc-itemdetail:pid=' + '0818108' +
                         '&library=ruru&pcck=P-22-03-01-02&tab=1&selectedCategory=ALL')
    # запрос данных

    p = Pool(2)
    req_map = p.map(data_collect, [r_address, s_address])
    r = req_map[0]
    s = req_map[1]
    print('goood')
    data = data_search(r, s)
    print(data)

