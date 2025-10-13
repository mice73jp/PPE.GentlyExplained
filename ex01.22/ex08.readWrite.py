def writeToFile(filename, message):
    with open(filename, 'wt') as fp:
        fp.write(message)


def appendToFile(filename, message):
    with open(filename, 'at') as fp:
        fp.write(message)


def readFromFile(filename):
    with open(filename, 'rt') as fp:
        if fp is None:
            return None
        return fp.read()

if __name__ == "__main__":
    writeToFile('greet.txt', 'Hello!\n')
    appendToFile('greet.txt', 'Goodbye!\n')
    assert readFromFile('greet.txt') == 'Hello!\nGoodbye!\n'