def generate_number(N:float, M:int, prefix=None):
    """ Генерирует все числа (с лидирующими незначащими нулями)
    в N-ричной системе счисления (N<=10)
    длины M
    """
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        generate_number(N, M-1, prefix)
        prefix.pop()


def gen_bin(M, prefix=""):
    if M == 0:
        print(prefix)
        return
    gen_bin(M-1, prefix+"0")
    gen_bin(M-1, prefix+"1")
    gen_bin(M-1, prefix + "2")


#gen_bin(1)

generate_number(2, 2)
