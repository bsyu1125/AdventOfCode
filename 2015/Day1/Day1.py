def readInput():
    f = open("input", "r")
    return f.readline()

"""
For every left there should be a right
Just count the left and that multiplied by 2 subtracted by the length of the input should be our result
"""
def countFloors(input):
    numLeftParnthesis = input.count('(')
    return (numLeftParnthesis * 2) - len(input)

"""
Iterate through the input
For every left, increment one. For every right, decrement one.
If it hits under 0, then we hit the basement
"""
def getBasementPosition(input):
    numFloor = 0
    for index in range(len(input)):
        character = input[index]

        if character == '(':
            numFloor = numFloor + 1
        else:
            numFloor = numFloor - 1

        if numFloor < 0:
            return index+1


if __name__ == "__main__":
    input = readInput()

    result = countFloors(input)
    print(result)

    basementPosition = getBasementPosition(input)
    print (basementPosition)
