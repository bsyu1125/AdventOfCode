def readAllInput():
    f = open("input", "r")
    return f.read().splitlines()

def parseInput(allInputs):
    result = []
    for input in allInputs:
        splitedInput = input.split('x')

        result.append((int(splitedInput[0]), int(splitedInput[1]), int(splitedInput[2])))

    return result

def calculateTotalSquareFeet(allParsedInputs):

    result = 0

    for input in allParsedInputs:
        length = input[0]
        width = input[1]
        height = input[2]

        lengthWidth = length * width
        widthHeight = width * height
        heightLength = height * length

        smallestArea = min(lengthWidth, widthHeight, heightLength)

        result = result + (2*lengthWidth) + (2*widthHeight) + (2*heightLength) + smallestArea

    return result

def calculateTotalRibbonLength(allInputs):
    result = 0

    for input in allInputs:
        length = input[0]
        width = input[1]
        height = input[2]

        lengthWidth = length * 2 + width * 2
        widthHeight = width * 2 +  height * 2
        heightLength = height * 2 + length * 2

        smallestPermimeter = min(lengthWidth, widthHeight, heightLength)

        result = result + (length*width*height) + smallestPermimeter

    return result



if __name__ == "__main__":
    allInputs = readAllInput()
    parsedInput = parseInput(allInputs)
    
    totalSquareFeet = calculateTotalSquareFeet(parsedInput)

    totalRibbon = calculateTotalRibbonLength(parsedInput)
    print(totalRibbon)


