def isLeapYear(year):
    return year % 4 == 0 and ( year % 100 != 0 or year % 400 == 0 )


def isValidDate(year, month, day):
    numYear = int(year)
    numMonth = int(month)
    numDay = int(day)
    
    if numYear <= 0 and numMonth <= 0 and numDay <= 0:
        return False

    if numMonth < 1 or numMonth > 12:
        return False
    
    if numDay < 1 or numDay > 31:
        return False
    
    if numMonth in [4, 6, 9, 11] and numDay == 31:
        return False
    elif numMonth == 2 and not isLeapYear(numYear) and numDay > 28:
        return False
    elif numMonth == 2 and isLeapYear(numYear) and numDay > 29:
        return False
    
    return True

if __name__ == '__main__':
    print("== Start checking date ==")
    assert isValidDate(1999, 12, 31) == True
    assert isValidDate(2000, 2, 29) == True
    assert isValidDate(2001, 2, 29) == False
    assert isValidDate(2029, 13, 1) == False
    assert isValidDate(1000000, 1, 1) == True
    assert isValidDate(2015, 4, 31) == False
    assert isValidDate(1970, 5, 99) == False
    assert isValidDate(1981, 0, 3) == False
    assert isValidDate(1666, 4, 0) == False

    import datetime
    d = datetime.date(1970, 1, 1)
    oneDay = datetime.timedelta(days=1)
    for i in range(1000000):
        assert isValidDate(d.year, d.month, d.day) == True
        d += oneDay
    print("== Finish checking date ==")
