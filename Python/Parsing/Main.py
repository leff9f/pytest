from Classes import Terminals
from data import data_num, open_last_num, data_search
from data import image_search, image_download, data_import
from data import save_num_sync, data_save, input_check
import time

# подсчет числа заказных номеров подготовленных для запросов
part_num_length = data_num()
print('number of data: '+str(part_num_length))
print('last used num: '+str(open_last_num()))

# ввод числа считываемых данных
x = input_check()

# время выполнения
tic = [time.time()]

# импорт заказного номера для последующей обработки
part_num = data_import(open_last_num())

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
                tic.append(time.time())
                print('calculation time: ' + str(int(tic[i + 1] - tic[0])) + ' seconds')
                TextSum = [t1.part_num, t1.type_num(), t1.desc, t1.MANUFACTURE, t1.MANUFACTURE, t1.part_num,
                           t1.cat_page(), t1.pack_unit(), t1.UNIT, t1.weight(), t1.width(), t1.height(),
                           t1.depth(), t1.graph_file(), t1.colour(), t1.material(), t1.cross_sect(),
                           t1.cross_min(), t1.cross_max(), t1.current(), t1.voltage()]
                save_num_sync(str(last_used_num))
                print(TextSum)
                tic.append(time.time())
                print('calculation time: '+str(int(tic[i+2] - tic[0]))+' seconds')
        else:
                print('no data, something wrong')
        print('iteration: '+str(i))
        i += 1

# сохранение последнего считанного заказного номер в файле temp
input('bye')

