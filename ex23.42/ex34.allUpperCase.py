def getUppercase(input_str):
    charDict = {
        'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g':'G', 'h': 'H', 'i': 'I', 'j': 'J', 'k':'K',
        'l': 'L', 'm': 'M', 'n':'N', 'o':'O', 'p': 'P', 'q': 'Q', 'r': 'R', 's':'S', 't':'T', 'u':'U', 'v': 'V', 'w':'W',
        'x': 'X', 'y':'Y', 'z':'Z'
    }

    output_str = ''
    for oneChar in input_str:
        # This one line is same as below if-else statement.
        # output_str += charDict.get(oneChar, oneChar)
        if oneChar in charDict:
            output_str += charDict[oneChar]
        else:
            output_str += oneChar

    return output_str


if __name__ == '__main__':
    print("== Start convert upper case ==")
    assert getUppercase('Hello') == 'HELLO'
    assert getUppercase('hello') == 'HELLO'
    assert getUppercase('HELLO') == 'HELLO'
    assert getUppercase('Hello, world!') == 'HELLO, WORLD!'
    assert getUppercase('goodbye 123!') == 'GOODBYE 123!'
    assert getUppercase('12345') == '12345'
    assert getUppercase('') == ''
    print("== Finish convert upper case ==")
