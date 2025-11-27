def mergeTwoLists(forth, back):
    mergedList = []
    fidx, bidx, flen, blen = 0, 0, len(forth), len(back)
    
    while fidx < flen or bidx < blen:
        if fidx == flen:
            mergedList.append(back[bidx])
            bidx += 1
        elif bidx == blen:
            mergedList.append(forth[fidx])
            fidx += 1
        elif forth[fidx] < back[bidx]:
            mergedList.append(forth[fidx])
            fidx += 1
        else:
            mergedList.append(back[bidx])
            bidx += 1

    return mergedList


if __name__ == '__main__':
    print("== Start make merged two lists ==")
    assert mergeTwoLists([1, 3, 6], [5, 7, 8, 9]) == [1, 3, 5, 6, 7, 8, 9]
    assert mergeTwoLists([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]
    assert mergeTwoLists([4, 5], [1, 2, 3]) == [1, 2, 3, 4, 5]
    assert mergeTwoLists([2, 2, 2], [2, 2, 2]) == [2, 2, 2, 2, 2, 2]
    assert mergeTwoLists([1, 2, 3], []) == [1, 2, 3]
    assert mergeTwoLists([], [1, 2, 3]) == [1, 2, 3]    
    print("== Finish make merged two lists ==")
