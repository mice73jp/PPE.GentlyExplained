# # My solution - 1
# def getTitleCase(message):
#     title_case = ''
#     titleOn = True

#     # 'A' 65 / 'Z' 90  / 'a' 97 / 'z' 122  difference 32
#     for oneChar in message:
#         if oneChar.isalpha():
#             if titleOn:
#                 titleOn = False
#                 if (ord(oneChar) >= ord('a') and ord(oneChar) <= ord('z')):
#                     title_case += chr(ord(oneChar) - 32)
#                 else:
#                     title_case += oneChar
#             elif (ord(oneChar) >= ord('A') and ord(oneChar) <= ord('Z')):
#                 title_case += chr(ord(oneChar) + 32)
#             else:
#                 title_case += oneChar   
#         else:
#             titleOn = True
#             title_case += oneChar

#     return title_case

# Book solution
def getTitleCase(text):
    titledText = ''

    for idx in range(len(text)):
        if idx == 0 or ( text[idx].isalpha() and not text[idx -1].isalpha()):
            titledText += text[idx].upper()
        else:
            titledText += text[idx].lower()

    return titledText

if __name__ == '__main__':
    print("== Start convert title case ==")

    assert getTitleCase('Hello, world!') == 'Hello, World!'
    assert getTitleCase('HELLO') == 'Hello'
    assert getTitleCase('hello') == 'Hello'
    assert getTitleCase('hElLo') == 'Hello'
    assert getTitleCase('') == ''
    assert getTitleCase('abc123xyz') == 'Abc123Xyz'
    assert getTitleCase('cat dog RAT') == 'Cat Dog Rat'
    assert getTitleCase('cat,dog,RAT') == 'Cat,Dog,Rat'

    import random
    random.seed(42)
    chars = list('abcdefghijklmnopqrstuvwxyz1234567890 ,.')
    for i in range(1000):
        random.shuffle(chars)
        assert getTitleCase(''.join(chars)) == ''.join(chars).title()

    print("== Finish convert title case ==")
