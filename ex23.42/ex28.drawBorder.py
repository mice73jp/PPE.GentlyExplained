def drawBorder(width, height):
    if width < 2 or height < 2:
        return

    def drawTop(width):
        print('+', end='')
        print('-' * (width - 2), end='')
        print('+')

    drawTop(width)
    for _ in range(height - 2):
        print('|', end='')
        for _ in range(width - 2):
            print(' ', end='')
        print('|')
    drawTop(width)


if __name__ == '__main__':
    print("== Start draw rectangle ==")
    drawBorder(16, 4)
    print("="* 50)
    drawBorder(10, 4)
    print("="* 50)
    drawBorder(2, 2)
    print("== Finish draw rectangle ==")