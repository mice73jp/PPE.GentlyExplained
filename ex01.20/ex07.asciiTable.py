def printASCIITable():
    for code_point in range(32, 126 + 1):
        print(code_point, chr(code_point))

if __name__ == "__main__":
    printASCIITable()