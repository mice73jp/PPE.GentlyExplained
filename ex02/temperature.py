def convertToCelsius(fah):
    # 섭씨 = (화씨 - 32) × (5 / 9)
    return (fah - 32) * (5 / 9)
    
def convertToFahrenheit(cel):
    # 화씨 = 섭씨 × (9 / 5) + 32
    return (cel * ( 9 / 5 )) + 32

if __name__ == "__main__":
    print("checking")
    assert convertToCelsius(0) == -17.77777777777778
    assert convertToCelsius(180) == 82.22222222222223
    assert convertToFahrenheit(0) == 32
    assert convertToFahrenheit(100) == 212
    assert convertToCelsius(convertToFahrenheit(15)) == 15
    assert convertToCelsius(convertToFahrenheit(42)) == 42.00000000000001
    print("No errors")
