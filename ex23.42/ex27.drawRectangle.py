# My solution - 1
def drawRectangle(width, height):
    if width < 1 or height < 1:
        return
    
    for _ in range(height):
        for _ in range(width):
            print("#", end='')
        print('')


# # My solution - 2
# def drawRectangle(width, height):
#     if width < 1 or height < 1:
#         return
#
#     for _ in range(height):
#         print('#' * width)


if __name__ == '__main__':
    print("== Start draw rectangle ==")
    drawRectangle(16, 4)
    print("="* 50)
    drawRectangle(10, 4)
    print("== Finish draw rectangle ==")