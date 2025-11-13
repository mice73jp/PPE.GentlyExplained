# # My solution
# def makeChange(amount):
#     change_values = {25: 'quarters', 10: 'dimes', 5: 'nickels', 1:'pennies'}
#     change = {}

#     for value in change_values:
#         share = amount // value
#         if share > 0:
#             change[change_values[value]] = share        
#         amount %= value

#     return change

# Book solution
def makeChange(amount):
    change = {}
    if amount >= 25:
        change['quarters'] = amount // 25
        amount %= 25
    if amount >= 10:
        change['dimes'] = amount // 10
        amount %= 10
    if amount >= 5:
        change['nickels'] = amount // 5
        amount %= 5
    if amount >= 1:
        change['pennies'] = amount

    return change


if __name__ == '__main__':
    print("== Start make change ==")
    assert makeChange(30) == {'quarters': 1, 'nickels': 1}
    assert makeChange(10) == {'dimes': 1}
    assert makeChange(57) == {'quarters': 2, 'nickels': 1, 'pennies': 2}
    assert makeChange(100) == {'quarters': 4}
    assert makeChange(125) == {'quarters': 5}
    print("== Finish make change ==")