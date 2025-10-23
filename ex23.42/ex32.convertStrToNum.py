def convertStrToInt(stringNum):
    numStr = {
        '0': 0, '1': 1, '2':2, '3':3, '4':4,
        '5': 5, '6': 6, '7':7, '8':8, '9':9,
    }

    sign = 1
    numVal = 0
    for ch in stringNum:
        if ch == '-':
            sign = -1
            continue
        numVal = ( numVal * 10 ) + numStr[ch]

    return sign * numVal


if __name__ == '__main__':
    print("== Start convert string number into integer ==")
    for i in range(-10000, 10000):
        assert convertStrToInt(str(i)) == i
    print("== Finish convert string number into integer ==")
