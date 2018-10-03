def gen_bin(M, prefix=""):
    if M == 0:
        print(prefix)
        return
    gen_bin(M-1, prefix+"0")
    gen_bin(M-1, prefix+"1")
    gen_bin(M-1, prefix + "2")


gen_bin(3)