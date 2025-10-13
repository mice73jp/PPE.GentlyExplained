import random

LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMBERS = '1234567890'
SPECIAL = '~!@#$%^&*()_+'
All_CHARS = LOWER_LETTERS + UPPER_LETTERS + NUMBERS + SPECIAL

def generatePassword(lenghtOfPassword):
    if lenghtOfPassword < 12:
        lenghtOfPassword = 12

    password = []
    password.append(LOWER_LETTERS[random.randint(0, len(LOWER_LETTERS) - 1)])
    password.append(UPPER_LETTERS[random.randint(0, len(UPPER_LETTERS) - 1)])
    password.append(NUMBERS[random.randint(0, len(NUMBERS) - 1)])
    password.append(SPECIAL[random.randint(0, len(SPECIAL) - 1)])

    for _ in range(lenghtOfPassword - 4):
        password.append(All_CHARS[random.randint(0, len(All_CHARS) - 1)])

    random.shuffle(password)
    print(password)
    return "".join(password)


if __name__ == '__main__':
    print("== Start create passwords ==")
    assert len(generatePassword(8)) == 12
    pw = generatePassword(14)
    assert len(pw) == 14
    hasLowercase = False
    hasUppercase = False
    hasNumber = False
    hasSpecial = False
    for character in pw:
        if character in LOWER_LETTERS:
            hasLowercase = True
        if character in UPPER_LETTERS:
            hasUppercase = True
        if character in NUMBERS:
            hasNumber = True
        if character in SPECIAL:
            hasSpecial = True
    assert hasLowercase and hasUppercase and hasNumber and hasSpecial
    print("== Finish create passwords ==")
