# # My solution - 1
# def convertIntToStr(integerNum):
#     numberStr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-']
#     if integerNum == 0:
#         return numberStr[integerNum]

#     integerStr = ''
#     if integerNum < 0:
#         integerStr += numberStr[-1]
#         integerNum *= -1
    
#     divider = 1
#     while integerNum // divider != 0:
#         divider *= 10
    
#     divider //= 10
#     while divider >= 1:
#         quotient = integerNum // divider
#         integerStr += numberStr[quotient]
#         integerNum = integerNum % divider
#         divider //= 10
    
#     return integerStr

# My solution - 2
def convertIntToStr(integerNum):
    digit = {
        0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 
        5: '5', 6: '6', 7: '7', 8: '8', 9: '9'
    }

    if integerNum == 0:
        return digit[integerNum]
    
    sign = ''
    if integerNum < 0:
        integerNum *= -1
        sign = '-'

    numberStr = ''
    while integerNum >= 1:
        remain = integerNum % 10
        integerNum //= 10
        numberStr = digit[remain] + numberStr

    return  sign + numberStr


if __name__ == '__main__':
    print("== Start convert integer number into string ==")
    for i in range(-10000, 10000):
        assert convertIntToStr(i) == str(i)
    print("== Finish convert integer number into string ==")
    
