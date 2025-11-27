def collatz(seed_number):
    sequence = []
    if seed_number == 0:
        return sequence

    sequence.append(seed_number)
    while seed_number > 1: 
        if seed_number % 2 == 0:
            seed_number //= 2
        else:
            seed_number = ( seed_number * 3 ) + 1
        sequence.append(seed_number)

    return sequence


if __name__ == '__main__':
    print("== Start make collatz sequence ==")
    assert collatz(0) == []
    assert collatz(10) == [10, 5, 16, 8, 4, 2, 1]
    assert collatz(11) == [11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    assert collatz(12) == [12, 6, 3, 10, 5, 16, 8, 4, 2, 1]
    assert len(collatz(256)) == 9
    assert len(collatz(257)) == 123

    import random
    random.seed(42)
    for i in range(1000):
        startingNum = random.randint(1, 10000)
        seq = collatz(startingNum)
        assert seq[0] == startingNum  # 시작 수를 포함하는지 확인
        assert seq[-1] == 1           # 마지막 정수가 1인지 확인
    print("== Finish make collatz sequence ==")
