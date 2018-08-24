from Classes import Terminals
from data import data_num, open_last_num, data_search
from data import image_search, image_download, data_import
from data import save_num_sync, data_save


# подсчет числа заказных номеров подготовленных для запросов
part_num_length = data_num()

# импорт заказного номера для последующей обработки
part_num = data_import(open_last_num())

# запрос данных
i = 0
last_used_num = 1
while i < 1:
        last_used_num = open_last_num()+i
        part_num = data_import(last_used_num)
        data = data_search(part_num)
        img_src = image_search(part_num)
        image_download(img_src, part_num)
        t1 = Terminals(part_num, data[0], data[1], data[2], data[3])
        print(t1.pack_unit())

    #    data_save(int(i+1), 1, t1.part_num)
    #    data_save(i + 1, 2, t1.short_desc)
    #    data_save(i + 1, 3, t1.desc)
    #    data_save(i + 1, 4, t1.tech_data)
    #    data_save(i + 1, 5, str(t1.comm_data))

        i += 1
        j = 0

        print(i)
save_num_sync(str(last_used_num))
print('1')

# сохранение последнего считанного заказного номер в файле temp !!!НЕ ЗАБЫТЬ!!!
#save_num_sync(str(100))