# # My solution - 1
# def printHandshakes(people:list):
#     count = 0
#     while len(people) > 1:
#         person = people[0]
#         people.remove(person)
#         for other in people:
#             print(person, "shakes hands with", other)
#             count += 1

#     return count


def printHandshakes(people:list):
    numberOfHandShakes = 0
    for left in range(0, len(people) - 1):
        for right in range(left + 1, len(people)):
            print(people[left], "shakes hands with", people[right])
            numberOfHandShakes += 1

    return numberOfHandShakes


if __name__ == '__main__':
    print("== Start combination of hand shakes ==")
    assert printHandshakes(['Alice', 'Bob']) == 1
    assert printHandshakes(['Alice', 'Bob', 'Carol']) == 3
    assert printHandshakes(['Alice', 'Bob', 'Carol', 'David']) == 6
    print("== Finish combination of hand shakes ==")