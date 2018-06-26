import random
a = 0
while a < 3:
    r = random.randint(0, 2)
    usinp = input("0 - Rock, 1 - Scissors, 2 - Paper, 3 and more - Exit:\n")
    if usinp.isdigit():
        a = int(usinp)
        if a == 0:
            if r == 0:
                print("rock vs rock")
            elif r == 1:
                print("rock vs scissors")
            elif r == 2:
                print("rock vs paper")
        elif a == 1:
            if r == 0:
                print("scissors vs rock")
            elif r == 1:
                print("scissors vs scissors")
            elif r == 2:
                print("scissors vs paper")
        elif a == 2:
            if r == 0:
                print("paper vs rock")
            elif r == 1:
                print("paper vs scissors")
            elif r == 2:
                print("paper vs paper")
        else:
            print("bye")
        if a==r:
            print("draw")
        if a == 1 and r == 2 or a == 2 and r == 0 or a == 0 and r == 1:
            print("you win")
        elif a<3 and a != r:
            print("you loose")
    else:
        print("not num")

