# # My solution
# def bubbleSort(numbers):
#     for endIdx in range(len(numbers), 1, -1):
#         for startIdx in range(endIdx - 1):
#             if numbers[startIdx] > numbers[startIdx + 1]:
#                 numbers[startIdx], numbers[startIdx + 1] = numbers[startIdx + 1], numbers[startIdx]
#     return numbers

# Book solution
def bubbleSort(numbers):
    for startIdx in range(len(numbers) - 1):
        for endIdx in range(startIdx, len(numbers)):
            if numbers[startIdx] > numbers[endIdx]:
                numbers[startIdx], numbers[endIdx] = numbers[endIdx], numbers[startIdx]

    return numbers


if __name__ == '__main__':
    print("== Start bubble sort ==")
    assert bubbleSort([2, 0, 4, 1, 3]) == [0, 1, 2, 3, 4]
    assert bubbleSort([2, 2, 2, 2]) == [2, 2, 2, 2]
    print("== Finish bubble sort ==")