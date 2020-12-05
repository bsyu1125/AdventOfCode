def readAllInput():
    f = open("input", "r")
    return f.read().splitlines()

"""
They use binary to count seats, we use binary to figure out what the seat id!

Do a bitwise shift to the left
F, L says they use upper half -> add a 1
B, R says they use lower half -> add a 0

Using his example (but only the seats): RLR
R means to take the upper half, keeping columns 4 through 7.
L means to take the lower half, keeping columns 4 through 5.
The final R keeps the upper of the two, column 5.
Meaning RLR -> 101 (in binary) -> 5 (in decimal)
"""
def calculateID(input: str):
    result = 0
    for character in input:

        # shift bits over
        result = result << 1

        # upper half
        if character == 'B' or character == 'R':
            result = result|1

        else:
            result = result|0

    return result

def calculateAllInputs(allInputs):
    return list(map(lambda input: calculateID(input), allInputs))

"""
Find your seat!
We know its a full flight -> your seat will be the id that is missing from the list
We're not on sitting on the very front or back of the flight -> we know the range of what we're looking for

Range = [maxId - number of Ids, maxId]

iterate through the range and see what doens't exist from the list of all ids
"""
def findYourSeatId(allIds):
    totalNum = len(allIds)
    maxId = max(allIds)

    minId = maxId - totalNum

    for index in range (minId, maxId):
        if index not in allIds:
            return index
    return 0

if __name__ == "__main__":
    allInputs = readAllInput()
    allIDs = calculateAllInputs(allInputs)
    
    answerPart1 = max(allIDs)
    print (answerPart1)

    answerPart2 = findYourSeatId(allIDs)
    print(answerPart2)
