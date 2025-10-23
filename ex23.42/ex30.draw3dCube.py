def drawBox(size):
    if size < 1:
        return
    
    print(' ' * (size + 1) + '+' + '-' * (size * 2) + '+')
    
    for weight in range(size, 0, -1):
        print(' ' * weight + '/' + ' ' * (size * 2) + '/' + ' ' * (size - weight) + '|')
    
    print('+' + '-' * (size * 2) + '+' + ' ' * size + '+')

    for weight in range(size, 0, -1):
        print('|' + ' ' * (size * 2) + '|' + ' ' * (weight - 1) + '/')
    
    print('+' + '-' * (size * 2) + '+')

if __name__ == '__main__':
    print("== Start draw 3D cube ==")
    for i in range(1, 6):
        drawBox(i)
        print("#"* 50)
    print("== Finish draw 3D cube ==")