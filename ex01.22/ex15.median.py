def median(numbers:list):
    if len(numbers) == 0:
        return None

    numbers.sort()

    if len(numbers) % 2 == 0:
        half_pos = len(numbers) // 2
        return (numbers[half_pos - 1] + numbers[half_pos]) / 2
    else:
        return numbers[len(numbers) // 2]

if __name__ == '__main__':
    print("== Start getting median ==")
    assert median([]) == None
    assert median([1, 2, 3]) == 2
    assert median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]) == 5.5
    assert median([3, 7, 10, 4, 1, 9, 6, 2, 8]) == 6

    import random
    random.seed(42)
    testData = [3, 7, 10, 4, 1, 9, 6, 2, 8]
    for i in range(1000):
        random.shuffle(testData)
        assert median(testData) == 6
    print("== Finish getting median ==")