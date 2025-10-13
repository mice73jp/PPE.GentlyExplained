from random import randint

def rollDice(numberOfDice):
    total = 0
    for _ in range(numberOfDice):
        total += randint(1,6)

    return total

if __name__ == '__main__':
    print("== Start total of roll dice(s) ==")
    assert rollDice(0) == 0
    assert rollDice(1000) != rollDice(1000)
    for i in range(1000):
        assert 1 <= rollDice(1) <= 6
        assert 2 <= rollDice(2) <= 12
        assert 3 <= rollDice(3) <= 18
        assert 100 <= rollDice(100) <= 600
    print("== Finish total of roll dice(s) ==")
