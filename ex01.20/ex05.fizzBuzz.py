def fizzBuzz(upTo):
    for num in range(1, upTo+1):
        if num % 3 == 0 and num % 5 == 0:
            print('FizzBuzz', end=' ')
        elif num % 5 == 0:
            print('Buzz', end=' ')
        elif num % 3 == 0:
            print('Fizz', end=' ')
        else:
            print(num, end=' ')

if __name__ == "__main__":
    fizzBuzz(35)
