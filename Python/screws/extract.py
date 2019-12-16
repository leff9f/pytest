"""test parsing
"""
import sys
import csv

__version__ = '0.1'
__author__ = 'leff9f'

"""
1. сделать проверку что длина больше диаметра
6.3x5.5x105
"""

id = []
length = []
diameter = []
color = []
goods = []
vvv = ["Саморез для сэндвич-панелей 6,3/5,5х130, цинк", "23021 Саморезы д/сэндвич панелей 6,3х5,5х105"]


def parsing():
    """read data and calling secondary functions
            Returns:
                index (list), goods (list): for further processing
    """
    data = f.read()
    split_input_data(data)
    color_find(goods)
    diameter_length_find(goods)
    check()
    saving_result()


def split_input_data(var: str):
    """Split data for separation indexes and main data.
        Args:
            var (str): Data without id.
        Returns:
            index (list), goods (list): for further processing
    """
    var = var.split('\n')[1:]
    for i in var:
        id.append(i[:str(i).find(',')])
        goods.append(i[str(i).find(',')+2:])


def color_find(var: list):
    """Cleaning data and find colors.
            Args:
                var (list): Data without id.
            Returns:
                color (list)
    """
    for i in var:
        tr = False
        k = ''
        i = str(i).replace('RAL ', 'RAL-')
        for j in i.split():
            if j[0:2].isalpha() and j[4:7].isdigit():
                k = j[:8]
                break
            if j.find("цвет") != -1:
                tr = True
                continue
            if tr:
                if j.isupper():
                    continue
                k = j.replace(',', '')
                k = k.replace('"', '')
                tr = False
        color.append(k)


def diameter_length_find(var: list):
    """Cleaning data and finding diameter and length.
    Args:
        var (list): data without id.
    Returns:
        diameter (list), length (list)
    """
    res = []
    for i in var:
        i = str(i).replace('х', '*')
        i = str(i).replace('x', '*')
        i = str(i).replace(',', '.')
        i = str(i).replace('* ', '*')
        i = str(i).replace(' *', '*')
        i = str(i).replace('.*', ' ')
        zn = []
        for j in i.split():
            if j.find("*") != -1 and j[:1].isdigit():
                zn.append(j)
        if len(zn) == 1:
            res.append(zn[0])
        else:
            res.append("*")

    for i in res:
        if i == "*":
            diameter.append("")
        else:
            if str(i).find("/") != -1 and str(i).find("/") < str(i).find("*"):
                diameter.append(float(i[:str(i).find("/")]))
            else:
                diameter.append(float(i[:str(i).find("*")]))

    for i in res:
        if i == "*":
            length.append('')
        else:
            k = 0
            tr = True

            if str(i[str(i).find("*") + 1:]).count("*") == 1:
                i = str(i).replace('*', '/', 1)

            for j in str(i[str(i).find("*")+1:]):
                if not j.isdigit() and j != '.':
                    tr = False
                if tr:
                    k += 1
            length.append(i[str(i).find("*")+1:str(i).find("*")+1+k])


def check():
    """checking length is bigger than diameter and correct
    """
    for i in range(len(length)):
        if length[i] != '' and diameter[i] != '':
            if float(length[i]) < float(diameter[i]):
                length[i], diameter[i] = diameter[i], length[i]


def saving_result():
    """structuring and writing data in csv file
    """
    with open('out-attributes.csv', 'w', newline='\n') as csvfile:
        fieldnames = ['id', 'length', 'diameter', 'color']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(len(id)):
            writer.writerow({'id': id[i], 'length': length[i], 'diameter': diameter[i], 'color': color[i]})


if __name__ == '__main__':
    for arg in sys.argv[1:]:
        try:
            f = open(arg, 'r', encoding='utf-8', errors='ignore')
        except OSError:
            print('cannot open', arg)
        else:
            parsing()
            f.close()

