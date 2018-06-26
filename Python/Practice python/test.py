def tlth(rnd_num, input_num):
    if rnd_num == input_num:
        return print("you win")
    elif rnd_num > input_num:
        return "too low"
    elif rnd_num < input_num:
        return "too high"

rnd=10
inp=10

tlth(rnd, inp)

