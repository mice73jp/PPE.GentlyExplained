# My solution
def getSmallest(numbers):
    if len(numbers) == 0:
        return None
    
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num

    return smallest


if __name__ == '__main__':
    print("== Start finding smallest number ==")
    assert getSmallest([1, 2, 3]) == 1
    assert getSmallest([3, 2, 1]) == 1
    assert getSmallest([28, 25, 42, 2, 28]) == 2
    assert getSmallest([1]) == 1
    assert getSmallest([]) == None
    print("== Finish finding smallest number ==")
