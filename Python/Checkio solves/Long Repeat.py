def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    # your code here
    x = 1
    y = 0
    if len(line) > 1:
        for i in range(0, len(line)-1):
            if line[i] == line[i+1]:
                x += 1
            else:
                x = 1
            if x > y:
                y = x
        return y
    else:
        return 0

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')