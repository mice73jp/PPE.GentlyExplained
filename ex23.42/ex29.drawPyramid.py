def drawPyramid(height):
    if height < 1:
        return
    
    for rowNum in range(0, height):
        print(' ' * ((height - 1) - rowNum) + '*' * ((rowNum * 2) + 1))

if __name__ == '__main__':
    print("== Start draw Pyramid ==")
    drawPyramid(5)
    print("-" * 50)
    drawPyramid(8)
    print("== Finish draw Pyramid ==")
