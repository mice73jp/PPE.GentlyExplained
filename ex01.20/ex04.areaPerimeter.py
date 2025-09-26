def area(width, length):
    if width < 0 or length < 0:
        raise ValueError
    return width * length

def perimeter(width, length):
    if width < 0 or length < 0:
        raise ValueError
    return 2 * ( width + length )

def volume(width, length, height):
    if any( one < 0 for one in [width, length, height]):
        raise ValueError

    return width * length * height

def surfaceArea(width, length, height):
    if any( one < 0 for one in [width, length, height]):
        raise ValueError

    return ((width * length) + (width * height) + (length * height)) * 2

if __name__ == "__main__":
    print("== Start checking area, perimeter, volume, surfaceArea ==")
    assert area(10, 10) == 100
    assert area(0, 9999) == 0
    assert area(5, 8) == 40
    assert perimeter(10, 10) == 40
    assert perimeter(0, 9999) == 19998
    assert perimeter(5, 8) == 26
    assert volume(10, 10, 10) == 1000
    assert volume(9999, 0, 9999) == 0
    assert volume(5, 8, 10) == 400
    assert surfaceArea(10, 10, 10) == 600
    assert surfaceArea(9999, 0, 9999) == 199960002
    assert surfaceArea(5, 8, 10) == 340
    # assert surfaceArea(5, 8, -10) == -340
    print("== Finish checking area, perimeter, volume, surfaceArea ==")