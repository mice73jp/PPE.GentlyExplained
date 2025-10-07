# %4 == 0 -> 2016, 2020, 2024
# %100 != 0 -> 2100, 2200, 2300
# %400 == 0 -> 2000, 2400
def isLeapYear(year):
    return year % 4 == 0 and ( year % 100 != 0 or year % 400 == 0 )

if __name__ == '__main__':
    print("== Start checking leap year ==")
    assert isLeapYear(1999) == False
    assert isLeapYear(2000) == True
    assert isLeapYear(2001) == False
    assert isLeapYear(2004) == True
    assert isLeapYear(2100) == False
    assert isLeapYear(2400) == True
    print("== Finish checking leap year ==")
