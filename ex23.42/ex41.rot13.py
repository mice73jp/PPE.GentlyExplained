# # My solution - 1
# def rot13(seed_str):
#     transTable = {
#         'A' : 'N','B' : 'O','C' : 'P','D' : 'Q','E' : 'R','F' : 'S','G' : 'T','H' : 'U','I' : 'V','J' : 'W','K' : 'X','L' : 'Y','M' : 'Z',
#         'N' : 'A','O' : 'B','P' : 'C','Q' : 'D','R' : 'E','S' : 'F','T' : 'G','U' : 'H','V' : 'I','W' : 'J','X' : 'K','Y' : 'L','Z' : 'M',
#         'a' : 'n','b' : 'o','c' : 'p','d' : 'q','e' : 'r','f' : 's','g' : 't','h' : 'u','i' : 'v','j' : 'w','k' : 'x','l' : 'y','m' : 'z',
#         'n' : 'a','o' : 'b','p' : 'c','q' : 'd','r' : 'e','s' : 'f','t' : 'g','u' : 'h','v' : 'i','w' : 'j','x' : 'k','y' : 'l','z' : 'm'
#     }

#     ret_str = ''
#     for idx in range(len(seed_str)):
#         ret_str += transTable[seed_str[idx]] if seed_str[idx] in transTable else seed_str[idx]

#     return ret_str

# Book solution
def rot13(seed_str):
    ret_str = ''

    for char in seed_str:
        if char.isalpha():
            bias_value = 13 if ord(char.upper()) < ord('N') else -13
            char = chr(ord(char) + bias_value)
        ret_str += char

    return ret_str


if __name__ == '__main__':
    print("== Start rot13 encrypt ==")
    assert rot13('Hello, world!') == 'Uryyb, jbeyq!'
    assert rot13('Uryyb, jbeyq!') == 'Hello, world!'
    assert rot13(rot13('Hello, world!')) == 'Hello, world!'
    assert rot13('abcdefghijklmnopqrstuvwxyz') == 'nopqrstuvwxyzabcdefghijklm'
    assert rot13('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'NOPQRSTUVWXYZABCDEFGHIJKLM'
    print("== Finish rot13 encrypt ==")
