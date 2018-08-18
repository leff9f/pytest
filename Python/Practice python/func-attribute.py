def tester(start):
    def nested(label):
        print(label, nested.st)
        nested.st += 1
    nested.st = start
    return nested

F = tester(0)
F("first")
F("second")
