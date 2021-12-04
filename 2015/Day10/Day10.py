def readInput():
    f = open("input", "r")
    return f.readline()

def lookAndSay(input):
    numCount = 0
    currentNum = input[0]
    stringList = []

    for index,value in enumerate(input):
        
        if value == currentNum:
            numCount += 1
        else:
            stringList.append(str(numCount))
            stringList.append(str(currentNum))
            currentNum = value
            numCount = 1

        if index == len(input) - 1:
            stringList.append(str(numCount))
            stringList.append(str(currentNum))

    return "".join(stringList)

if __name__ == "__main__":
    input = readInput()

    result = input
    for counter in range(50):
        print(counter)
        result = lookAndSay(result)

    print(len(result))