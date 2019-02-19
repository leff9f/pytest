def safe_pawns(pawns: set) -> int:
    chpawns = set()
    chpawns1 = set()
    chpawns2 = set()
    for i in pawns:
        x = ord(i[0])
        y = ord(i[1])
        chpawns.add(str(x)+str(y))
        chpawns1.add(str(x-1)+str(y+1))
        chpawns2.add(str(x+1) + str(y+1))
    return len(chpawns & chpawns1 | chpawns & chpawns2)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")


