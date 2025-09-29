# # My solution -> It uses too big memory for calculation.
# def getChessSquareColor(column, row):
#     ROW00 = [0, 1, 0, 1, 0, 1, 0, 1]
#     ROW01 = [1, 0, 1, 0, 1, 0, 1, 0]
#     chessSquare = [
#         ROW00, ROW01, ROW00, ROW01,
#         ROW00, ROW01, ROW00, ROW01,
#     ]

#     if row > len(chessSquare) - 1 or column > len(chessSquare[0]) -1:
#         return ''
    
#     return 'white' if chessSquare[row][column] == 0 else 'black'

#     # for r in chessSquare:
#     #     for val in r:
#     #         colour = 'white' if val == 0 else 'black'
#     #         print(colour, end=' ')
#     #     print()

# Book solution
def getChessSquareColor(column, row):
    if row > 7 or column > 7 or row < 0 or column < 0:
        return ''
    
    return 'white' if column % 2 == row % 2 else 'black'


if __name__ == "__main__":
    print("== Start checking colour ==")
    assert getChessSquareColor(7, 7) == 'white'
    assert getChessSquareColor(1, 0) == 'black'
    assert getChessSquareColor(0, 0) == 'white'
    assert getChessSquareColor(1, 0) == 'black'
    assert getChessSquareColor(0, 1) == 'black'
    assert getChessSquareColor(7, 7) == 'white'
    assert getChessSquareColor(0, 8) == ''
    assert getChessSquareColor(2, 9) == ''
    assert getChessSquareColor(-1, 7) == ''
    assert getChessSquareColor(7, -1) == ''
    print("== Finish checking colour ==")
