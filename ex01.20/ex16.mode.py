# # My solution 1
# def mode(numbers:list):
#     if len(numbers) == 0:
#         return None
    
#     encount = {}
#     for num in numbers:
#         encount[num] = encount.get(num, 0) + 1

#     mode = None
#     count = 0
#     for num, cnt in encount.items():
#         if count == 0 or count < cnt:
#             mode = num
#             count = cnt

#     return mode


# Book solution
def mode(numbers:list):
    if len(numbers) == 0:
        return None
    
    encount = {}
    mode = None
    count = 0
    for num in numbers:
        encount[num] = encount.get(num, 0) + 1

        if count < encount[num]:
            mode = num
            count = encount[num]

    return mode


if __name__ == '__main__':
    print("== Start getting mode ==")
    assert mode([]) == None
    assert mode([1, 2, 3, 4, 4]) == 4
    assert mode([1, 1, 2, 3, 4]) == 1

    import random
    random.seed(42)
    testData = [1, 2, 3, 4, 4]
    for i in range(1000):
        random.shuffle(testData)
        assert mode(testData) == 4
    print("== Finish getting mode ==")
