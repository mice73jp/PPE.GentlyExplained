# My solution
def reverseString(src_string):
    reverse_string = ''
    for idx in range(len(src_string)-1, -1, -1):
        reverse_string += src_string[idx]

    return reverse_string


# Book solution
def reverseString2(src_string):
    pass

if __name__ == '__main__':
    print("== Start reverse string ==")
    assert reverseString('Hello') == 'olleH'
    assert reverseString('') == ''
    assert reverseString('aaazzz') == 'zzzaaa'
    assert reverseString('xxxx') == 'xxxx'
    print("== Finish reverse string ==")
