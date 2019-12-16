import sys
import csv


def parsing():
    with f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
            diamlength(row)

vr = "23062 Саморез гипс-дерево 3,5x55 (промо) 5000 шт."


def diamlength(var):
    var = str(var).replace('х', '*')
    var = str(var).replace('x', '*')
    var = str(var).replace(',', '.')
    k=-1
    result=''
    for i in var:
        if i.isdigit():
            var = var[var.index(i):]
            pos = str(var).find('*')
            if pos < 6:
                for j in var:
                    if str(j) == '*':
                        k = var.index(j)
                        result = var[:var.index(j)]
                    if not str(j).isdigit() and str(j) != '*' and str(j) != '.' and k!=-1:
                        result = result + '*' + var[k+1:var.index(j)]
                        return print(result)



"""def diamlength1(var):
    for i in var:
        if i.isdigit():
            var = var[var.index(i):]
            pos = str(var).find('*')
            if pos < 6:
                for j in var:
                    if str(j).isalpha() and str(j) != 'х' and str(j) != 'x':
                        return print(var[:var.index(j)])"""

if __name__ == '__main__':
    for arg in sys.argv[1:]:
        try:
            f = open(arg, 'r', encoding='utf-8', errors='ignore')
        except OSError:
            print('cannot open', arg)
        else:
            parsing()


            f.close()