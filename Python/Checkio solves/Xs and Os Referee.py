from typing import List

def checkio(game_result: List[str]) -> str:
    b = str(game_result[0])
    c = str(game_result[1])
    d = str(game_result[2])
    e = []
    if b[0] == b[1] == b[2]:
        e.append(b[0])
    if c[0] == c[1] == c[2]:
        e.append(c[0])
    if d[0] == d[1] == d[2]:
        e.append(d[0])
    if b[0] == c[0] == d[0]:
        e.append(b[0])
    if b[1] == c[1] == d[1]:
        e.append(b[1])
    if b[2] == c[2] == d[2]:
        e.append(b[2])
    if b[0] == c[1] == d[2]:
        e.append(b[0])
    if b[2] == c[1] == d[0]:
        e.append(b[2])

    if len(e) == 0:
        return 'D'
    if len(e) == 1:
        if e[0] == '.':
            return 'D'
        if e[0] == 'X':
            return 'X'
        if e[0] == 'O':
            return 'O'
    if len(e) > 1:
        if e.count('.') != 0:
            e.remove('.')
        if e.count('O') == 0 and e.count('X') != 0:
            return 'X'
        if e.count('X') == 0 and e.count('O') != 0:
            return 'O'
        if e.count('O') != 0 and e.count('X') != 0:
            return 'D'
        return 'D'

if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")