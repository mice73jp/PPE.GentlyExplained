import random

# My solution
def shuffle(values):
    for idx in range(len(values)):
        target_idx = random.randint(0, len(values)-1)
        values[idx], values[target_idx] = values[target_idx], values[idx]

    return values


if __name__ == '__main__':
    print("== Start shuffle numbers ==")

    random.seed(42)
    for i in range(10):  # 이 테스트를 10번 수행합니다:
        testData1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        shuffle(testData1)
        assert len(testData1) == 10  # 값의 개수가 변경되지 않았는지 확인합니다:
        assert testData1 != [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # 순서가 변경되었는지 확인합니다:
        assert sorted(testData1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # 다시 정렬했을 때 모든 원래 값들이 있는지 확인합니다:

    testData2 = []
    shuffle(testData2)
    assert testData2 == []  # 빈 리스트를 섞으면 빈 상태로 유지되는지 확인합니다:
    print("== Finish shuffle numbers ==")