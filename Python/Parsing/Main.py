from Classes import Terminals
from data import data_num, open_last_num, data_search
from data import image_search, image_download, data_import
from data import save_num_sync, data_save, input_check
import time

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

# запрос и запись данных
i = 0
last_used_num = 1
while i < int(x):
        last_used_num = open_last_num()+i
        part_num = data_import(last_used_num)
        data = data_search(part_num)
        img_src = image_search(part_num)
        if data != '0':
                if img_src != '':
                        image_download(img_src, part_num)
                t1 = Terminals(part_num, data[0], data[1], data[2], data[3])
                data_save(i + 2, 1, t1.part_num)
                data_save(i + 2, 2, t1.type_num())
                data_save(i + 2, 3, t1.desc)
                data_save(i + 2, 4, t1.MANUFACTURE)
                data_save(i + 2, 5, t1.MANUFACTURE)
                data_save(i + 2, 6, t1.part_num)
                data_save(i + 2, 7, t1.cat_page())
                data_save(i + 2, 8, t1.pack_unit())
                data_save(i + 2, 9, t1.UNIT)
                data_save(i + 2, 10, t1.weight())
                data_save(i + 2, 11, t1.width())
                data_save(i + 2, 12, t1.height())
                data_save(i + 2, 13, t1.depth())
                data_save(i + 2, 14, t1.graph_file())
                data_save(i + 2, 15, t1.colour())
                data_save(i + 2, 16, t1.material())
                data_save(i + 2, 17, t1.cross_sect())
                data_save(i + 2, 18, t1.cross_min())
                data_save(i + 2, 19, t1.cross_max())
                data_save(i + 2, 20, t1.current())
                data_save(i + 2, 21, t1.voltage())
                save_num_sync(str(last_used_num))
                print(t1.part_num)
                tic.append(time.time())
                print('calculation time: '+str(int(tic[i+1] - tic[0]))+' seconds')
        else:
                print('no data, something wrong')
        print('iteration: '+str(i))
        i += 1

# сохранение последнего считанного заказного номер в файле temp

input('bye')

