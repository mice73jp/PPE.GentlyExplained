def drawBorder(width, height):
    if width < 2 or height < 2:
        return

    mid = width - 2
    print('+' + '-' * mid + '+')
    for _ in range(height - 2):
        print('|' + ' ' * mid + '|')
    print('+' + '-' * mid + '+')


if __name__ == '__main__':
    print("== Start draw rectangle ==")
    drawBorder(16, 4)
    print("="* 50)
    drawBorder(10, 4)
    print("="* 50)
    drawBorder(2, 2)
    print("== Finish draw rectangle ==")