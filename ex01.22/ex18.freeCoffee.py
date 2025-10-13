# # My solution
# def getCostOfCoffee(numberOfCoffees, pricePerCoffee):
#     NUM_COFFEE_STAMP = 8
#     shouldPayingCoffee = 0
#     paidCount = 0

#     for _ in range(numberOfCoffees):
#         if paidCount == NUM_COFFEE_STAMP:
#             paidCount = 0
#             continue
#         paidCount += 1
#         shouldPayingCoffee += 1
        
#     return shouldPayingCoffee * pricePerCoffee

# # Book solutioin - 1
# def getCostOfCoffee(numberOfCoffees, pricePerCoffee):
#     NUM_COFFEE_STAMP = 8
#     paidCount = 0
#     totalPrice = 0

#     while numberOfCoffees > 0:
#         numberOfCoffees -= 1
#         if paidCount == NUM_COFFEE_STAMP:
#             paidCount = 0
#         else:
#             paidCount += 1
#             totalPrice += pricePerCoffee

#     return totalPrice

# Book solution - 2
def getCostOfCoffee(numberOfCoffees, pricePerCoffee):
    NUM_COFFEE_SET = 9
    numberOfFreeCoffees = numberOfCoffees // NUM_COFFEE_SET
    numberOfPaidCoffees = numberOfCoffees - numberOfFreeCoffees

    return numberOfPaidCoffees * pricePerCoffee



if __name__ == '__main__':
    print("== Start getting total cost of coffee ==")
    assert getCostOfCoffee(7, 2.50) == 17.50
    assert getCostOfCoffee(8, 2.50) == 20
    assert getCostOfCoffee(9, 2.50) == 20
    assert getCostOfCoffee(10, 2.50) == 22.50

    for i in range(1, 4):
        assert getCostOfCoffee(0, i) == 0
        assert getCostOfCoffee(8, i) == 8 * i
        assert getCostOfCoffee(9, i) == 8 * i
        assert getCostOfCoffee(18, i) == 16 * i
        assert getCostOfCoffee(19, i) == 17 * i
        assert getCostOfCoffee(30, i) == 27 * i
    print("== Finish getting total cost of coffee ==")