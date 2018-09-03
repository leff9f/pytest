class Terminals:
    MANUFACTURE = "PHOENIX"
    UNIT = "шт"

    def __init__(self, part_num, short_desc, desc, tech_data, comm_data):
        self.part_num = part_num
        self.short_desc = short_desc
        self.desc = desc
        self.tech_data = tech_data
        self.comm_data = comm_data

    def type_num(self):
        text = str(self.short_desc)
        res = str(text).find(" - ")
        res1 = str(text).rfind(" - ")
        text = text[res + 3:res1]
        return text

    def cat_page(self):
        ind = int(self.comm_data.index('Страница каталога'))
        return str(self.comm_data[ind + 1])

    def pack_unit(self):
        ind = int(self.comm_data.index('Упаковочная единица '))
        return str(self.comm_data[ind + 1]).strip(' stk')

    def weight(self):
        ind = int(self.comm_data.index('Вес/шт. (без упаковки)'))
        if ind:
            weight = str(self.comm_data[ind + 1]).strip(' GRM')
            weight = weight.replace(',', '.')
            weight = float(weight)
            weight = int(weight)
            if weight < 10:
                return 0.01
            else:
                return weight/1000

    def width(self):
        if 'Ширина (a)' in self.tech_data:
            ind = int(self.tech_data.index('Ширина (a)'))
            return str(self.tech_data[ind + 1])
        elif 'Ширина' in self.tech_data:
            ind = int(self.tech_data.index('Ширина'))
            return str(self.tech_data[ind + 1])
        else:
            return ''

    def height(self):
        if 'Длина (b)' in self.tech_data:
            ind = int(self.tech_data.index('Длина (b)'))
            return str(self.tech_data[ind + 1])
        elif 'Длина' in self.tech_data:
            ind = int(self.tech_data.index('Длина'))
            return str(self.tech_data[ind + 1])
        else:
            return ''

    def depth(self):
        if 'Высота (c)' in self.tech_data:
            ind = int(self.tech_data.index('Высота (c)'))
            return str(self.tech_data[ind + 1])
        elif 'Высота' in self.tech_data:
            ind = int(self.tech_data.index('Высота'))
            return str(self.tech_data[ind + 1])
        else:
            return ''

    def graph_file(self):
        return str(self.part_num+'.jpg')

    def colour(self):
        if 'Цвет' in self.tech_data:
            ind = int(self.tech_data.index('Цвет'))
            return str(self.tech_data[ind + 1])
        else:
            return ''

    def material(self):
        if 'Материал' in self.tech_data:
            ind = int(self.tech_data.index('Материал'))
            return str(self.tech_data[ind + 1])
        elif 'Изоляционный материал' in self.tech_data:
            ind = int(self.tech_data.index('Изоляционный материал'))
            return str(self.tech_data[ind + 1])
        else:
            return ''

    def cross_sect(self):
        if 'Сечение гибкого проводника макс. ' in self.tech_data:
            ind = int(self.tech_data.index('Сечение гибкого проводника макс. '))
            return str(self.tech_data[ind + 1])
        elif 'Сечение гибкого проводника макс.' in self.tech_data:
            ind = int(self.tech_data.index('Сечение гибкого проводника макс.'))
            return str(self.tech_data[ind + 1])
        else:
            return ''

    def cross_min(self):
        if 'Сечение гибкого проводника мин. ' in self.tech_data:
            ind = int(self.tech_data.index('Сечение гибкого проводника мин. '))
            return str(self.tech_data[ind + 1])
        elif 'Сечение гибкого проводника мин.' in self.tech_data:
            ind = int(self.tech_data.index('Сечение гибкого проводника мин.'))
            return str(self.tech_data[ind + 1])
        else:
            return ''

    def cross_max(self):
        if 'Сечение гибкого проводника макс. ' in self.tech_data:
            ind = int(self.tech_data.index('Сечение гибкого проводника макс. '))
            return str(self.tech_data[ind + 1])
        if 'Сечение гибкого проводника макс.' in self.tech_data:
            ind = int(self.tech_data.index('Сечение гибкого проводника макс.'))
            return str(self.tech_data[ind + 1])
        else:
            return ''

    def current(self):
        if 'Номинальный ток IN' in self.tech_data:
            ind = int(self.tech_data.index('Номинальный ток IN'))
            return str(self.tech_data[ind + 1])
        else:
            return ''

    def voltage(self):
        if 'Номинальное напряжение UN' in self.tech_data:
            ind = int(self.tech_data.index('Номинальное напряжение UN'))
            return str(self.tech_data[ind + 1])
        else:
            return ''







