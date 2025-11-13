# # My solution
# def reverseString(src_string):
#     reverse_string = ''
#     for idx in range(len(src_string)-1, -1, -1):
#         reverse_string += src_string[idx]

#     return reverse_string


# idx & opposite_idx
# 0 - 9
# 1 - 8
# 2 - 7
# 3 - 6
# 4 - 5

# Book solution
def reverseString(src_string):
    working_src = list(src_string)

    for idx in range(len(working_src) // 2):
        opposite_idx = len(working_src) - 1 - idx
        working_src[idx], working_src[opposite_idx] = working_src[opposite_idx], working_src[idx]

    return ''.join(working_src)


if __name__ == '__main__':
    print("== Start reverse string ==")
    assert reverseString('Hello') == 'olleH'
    assert reverseString('') == ''
    assert reverseString('aaazzz') == 'zzzaaa'
    assert reverseString('xxxx') == 'xxxx'
    print("== Finish reverse string ==")
