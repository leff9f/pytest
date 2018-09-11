from Classes import Terminals
from data import data_num, open_last_num, data_search
from data import image_search, image_download, data_import
from data import save_num_sync, data_save, input_check
from data import data_collect
import time
from multiprocessing import Pool

if __name__ == '__main__':
        # counting data length
        part_num_length = data_num()
        print('number of data: '+str(part_num_length))
        print('last used num: '+str(open_last_num()))
        # input num of calculation data
        x = input_check()
        # calculation time
        tic = time.time()
        # import part num for calculation
        part_num = data_import(open_last_num())
        # request and write data
        i = 0
        # using last_used_num as default
        last_used_num = open_last_num()
        while i < int(x):
                last_used_num += 1
                part_num = data_import(last_used_num)
                # data address
                r_address = ('https://www.phoenixcontact.com/online/portal/ru/?uri=pxc-oc-itemdetail:pid='
                             + str(part_num) +
                             '&library=ruru&pcck=P-22-03-01-02&tab=2&selectedCategory=ALL')
                s_address = ('https://www.phoenixcontact.com/online/portal/ru/?uri=pxc-oc-itemdetail:pid='
                             + str(part_num) +
                             '&library=ruru&pcck=P-22-03-01-02&tab=1&selectedCategory=ALL')
                # request data, multiprocessing pool
                p = Pool(2)
                req_map = p.map(data_collect, [r_address, s_address])
                if req_map[0] != '0' and req_map[1] != '0':
                        r = req_map[0]
                        s = req_map[1]
                        # search and return data
                        data = data_search(r, s)
                        if data != '0':
                                img_src = image_search(part_num)
                                if img_src != '':
                                        image_download(img_src, part_num)
                                t1 = Terminals(part_num, data[0], data[1], data[2], data[3])
                                tac1 = time.time()
                                print('calculation time: ' + str(int(tac1 - tic)) + ' seconds')
                                # sorted list of data for saving in excel
                                TextSum = [t1.part_num, t1.type_num(), t1.desc, t1.MANUFACTURE, t1.MANUFACTURE, t1.part_num,
                                           t1.cat_page(), t1.pack_unit(), t1.UNIT, t1.weight(), t1.width(), t1.height(),
                                           t1.depth(), t1.graph_file(), t1.colour(), t1.material(), t1.cross_sect(),
                                           t1.cross_min(), t1.cross_max(), t1.current(), t1.voltage()]
                                data_save(last_used_num, TextSum)
                                tac2 = time.time()
                                print('calculation time: '+str(int(tac2 - tic))+' seconds')
                        else:
                                print('no data at page')
                        print('iteration: '+str(i))
                        save_num_sync(str(last_used_num))
                else:
                        print('wrong part num, page not found')
                p.close()
                i += 1
        input("bye")



