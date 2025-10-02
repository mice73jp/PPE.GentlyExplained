def calculateSum(numbers):
    result = 0
    for num in numbers:
        result += num
    return result


def calculateProduct(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result


if __name__ == '__main__':
    print("== Start getting sum & product ==")
    assert calculateSum([]) == 0
    assert calculateSum([2, 4, 6, 8, 10]) == 30
    assert calculateProduct([]) == 1
    assert calculateProduct([2, 4, 6, 8, 10]) == 3840
    print("== Finish getting sum & product ==")