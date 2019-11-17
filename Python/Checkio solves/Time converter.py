def time_converter(time):
    if int(time[0:2]) > 12:
        return (str(int(time[0:2])-12))+str(time[2:5])+" p.m."
    elif int(time[0:2]) == 12:
        return str(time)+" p.m."
    elif int(time[0:2]) == 0:
        return (str(int(time[0:2])+12))+str(time[2:5])+" a.m."
    return str(int(time[0:2]))+str(time[2:5])+" a.m."

if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('00:30') == '12:30 a.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")

