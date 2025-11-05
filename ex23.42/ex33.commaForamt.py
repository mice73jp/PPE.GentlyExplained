# # My solution - 1
# def commaFormat(number):
#     DIGIT = {
#         0: '0', 1: '1', 2:'2', 3:'3', 4:'4',
#         5: '5', 6: '6', 7:'7', 8:'8', 9:'9'
#     }

#     fraction_str = str(number).split('.')

#     integer_num = int(fraction_str[0])
#     numberStr = ''
#     numCnt = 0
#     while integer_num > 0:
#         if numCnt == 3:
#             numCnt = 0
#             numberStr = ',' + numberStr

#         remain = integer_num % 10
#         numberStr = DIGIT[remain] + numberStr
#         numCnt += 1
#         integer_num //= 10

#     if len(fraction_str) == 2:
#         numberStr += '.' + fraction_str[1]

#     return numberStr

# Book solution
def commaFormat(number):
    number_part = str(number)
    fractioin_part = ''
    if '.' in number_part:
        fractioin_part = number_part[number_part.index('.'):]
        number_part = number_part[:number_part.index('.')]
    else:
        fractioin_part = ''

    commaNumber = ''
    triple_part = ''
    for pos in range(len(number_part) - 1, -1, -1):
        if len(triple_part) == 3:
            commaNumber = ',' + triple_part + commaNumber
            triple_part = ''
        triple_part = number_part[pos] + triple_part

    if triple_part != '':
        commaNumber = triple_part + commaNumber

    return commaNumber + fractioin_part


if __name__ == '__main__':
    print("== Start convert integer into comma format ==")
    assert commaFormat(1) == '1'
    assert commaFormat(10) == '10'
    assert commaFormat(100) == '100'
    assert commaFormat(1000) == '1,000'
    assert commaFormat(10000) == '10,000'
    assert commaFormat(100000) == '100,000'
    assert commaFormat(1000000) == '1,000,000'
    assert commaFormat(1234567890) == '1,234,567,890'
    assert commaFormat(1000.123456) == '1,000.123456'
    print("== Finish convert integer into comma format ==")
