def safe_pawns(pawns: set):
    N = len(pawns)
    for i in range(0, N):
        for j in range(1, N-i):
            print(pawns)
            #if ord(i[0]) == ord(j[0])-1 or int(i[1]) == int(j[1])-1 and ord(i[0]) == ord(j[0])+1 or int(i[1]) == int(j[1])-1:
            print('1')


safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"})
#safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"})
