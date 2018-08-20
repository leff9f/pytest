class ResPar:
    name = ""
    kind = ""
    color = ""
    value = 100.00
    var = 'text'

    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

fc = ResPar()
fc.name = "toyota"; fc.kind = "sedan"; fc.color = "blue"
print(fc.description())

