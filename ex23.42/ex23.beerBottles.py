def countBeerBottles():
    for numBeerBottles in range(99, 1, -1):
        print(numBeerBottles, "of beer on the wall,")
        print(numBeerBottles, "bottles of beer,\nTake one down,\nPass it around,")
        if numBeerBottles - 1 == 1:
            print("1 bottle of beer on the wall,")
        else:
            print(numBeerBottles - 1, "bottles of beer on the wall,")
        print('')
    print("1 bottle of beer on the wall,\n1 bottle of beer,\nTake one down,\nPass it around,\nNo more bottles of beer on the wall!")


if __name__ == '__main__':
    print("== Start how many bottles there are ==")
    countBeerBottles()
    print("== Finsih how many bottles there are ==")
