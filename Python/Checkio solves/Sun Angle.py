def sun_angle(time):
    #replace this for solution
    #180grad - 12hours or 720minuts
    time_conv = int(time[0:2])*60+int(time[3:5])
    if time_conv < 360 or time_conv > 1080:
        return "I don't see the sun!"
    return (time_conv-360)*180/720

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")