import random

def tlth(rnd_num, input_num):
    if rnd_num == input_num:
        return print("you win")
    elif rnd_num > input_num:
        return print("too low")
    elif rnd_num < input_num:
        return print("too high")

rnd = random.randint(1, 9)
a = 1
while a == 1:
    inp = input("Input a num from 1 to 9 for game, start for restart or exit for end\n")
    if inp.isdigit():
        tlth(rnd, int(inp))
    elif inp == "exit":
        a = 0
        print("bye")
    elif inp == "start":
        rnd = random.randint(1, 9)
    else:
        print("wrong input")