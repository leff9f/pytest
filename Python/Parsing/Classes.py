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


"""
    def out(self, cp, pu, u,
         wg, wd, h, d, ia, c, m,
         cs, cmin, cmax, cur, vol):
        self.type_num = self.short_desc
        
        self.cat_page = cp
        self.pack_unit = pu
        self.unit = u
        self.weight = wg
        self.width = wd
        self.height = h
        self.depth = d
        self.img_add = ia
        self.colour = c
        self.material = m
        self.cross_sect = cs
        self.cross_min = cmin
        self.cross_max = cmax
        self.current = cur
        self.voltage = vol
"""







