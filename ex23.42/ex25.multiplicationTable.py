def multiplicationTable():
    print("  |  1  2  3  4  5  6  7  8  9 10")
    print("--+------------------------------")
    for col in range(1, 11):
        # print(f"{col:>2}|", end='')
        print(str(col).rjust(2, ' ') + '|', end='')
        for row in range(1, 11):
            # print(f" {col * row:>2}", end='')
            print(' ' + str(col * row).rjust(2, ' '), end='')
        print("")


if __name__ == '__main__':
    print("== Start showing multiplication table ==")
    multiplicationTable()
    print("== Finsih showing multiplication table ==")
