def readInput():
    f = open("input", "r")
    return f.readline()

def calculateHousesWithAtLeastOnePresent(input):

    sizeArray = len(input) * 2
    grid = [[0] * sizeArray for _ in range(sizeArray)]

    currentRowIndex = len(input) - 1
    currentColIndex = len(input) - 1

    grid[currentRowIndex][currentColIndex] = 1

    for direction in input:
        nextRowIndex = currentRowIndex
        nextColIndex = currentColIndex

        if direction == '^':
            nextRowIndex = nextRowIndex - 1
        elif direction == '>':
            nextColIndex = nextColIndex + 1
        elif direction == '<':
            nextColIndex = nextColIndex - 1
        else:
            nextRowIndex = nextRowIndex + 1

        grid[nextRowIndex][nextColIndex] = grid[nextRowIndex][nextColIndex] + 1

        currentRowIndex = nextRowIndex
        currentColIndex = nextColIndex


    houseCount = 0
    for row in grid:
        for col in row:
            if col > 0:
                houseCount = houseCount + 1

    return houseCount

def calculateHousesWithAtLeastOnePresentRobotSanta(input):

    sizeArray = len(input) * 2
    grid = [[0] * sizeArray for _ in range(sizeArray)]

    currentRowIndex = len(input) - 1
    currentColIndex = len(input) - 1

    roboRowIndex = currentRowIndex
    roboColIndex = currentColIndex

    santaRowIndex = currentRowIndex
    santaColIndex = currentColIndex

    grid[currentRowIndex][currentColIndex] = 1

    for index in range(len(input)):

        if index % 2:
            currentRowIndex = roboRowIndex
            currentColIndex = roboColIndex
        else:
            currentRowIndex = santaRowIndex
            currentColIndex = santaColIndex

            
        nextRowIndex = currentRowIndex
        nextColIndex = currentColIndex

        direction = input[index]
        if direction == '^':
            nextRowIndex = nextRowIndex - 1
        elif direction == '>':
            nextColIndex = nextColIndex + 1
        elif direction == '<':
            nextColIndex = nextColIndex - 1
        else:
            nextRowIndex = nextRowIndex + 1

        grid[nextRowIndex][nextColIndex] = grid[nextRowIndex][nextColIndex] + 1

        if index % 2:
            roboRowIndex = nextRowIndex
            roboColIndex = nextColIndex
        else:
            santaRowIndex = nextRowIndex
            santaColIndex = nextColIndex

    houseCount = 0
    for row in grid:
        for col in row:
            if col > 0:
                houseCount = houseCount + 1

    return houseCount



if __name__ == "__main__":
    input = readInput()

    """
    housesWithAtLeastOnePresent = calculateHousesWithAtLeastOnePresent(input)
    print(housesWithAtLeastOnePresent)
    """

    result = calculateHousesWithAtLeastOnePresentRobotSanta(input)
    print(result)