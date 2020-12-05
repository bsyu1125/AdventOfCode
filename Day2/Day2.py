def readAllInput():
    f = open("input", "r")
    return f.read().splitlines()

def parseInput(allInputs):
    result = []
    for input in allInputs:
        password = input.split(':')[1].strip()
        min = input.split('-')[0].strip()
        max = input.split(' ')[0].split('-')[1].strip()
        passwordCriteria = input.split(':')[0].split(' ')[1].strip()

        result.append((min, max, passwordCriteria, password))

    return result

def numValidPasswords(parsedInputs):
    result = 0

    for parsedInput in parsedInputs:
        min = parsedInput[0]
        max = parsedInput[1]
        passwordCriteria = parsedInput[2]
        password = parsedInput[3]

        numCriteria = password.count(passwordCriteria)

        if int(min) <= numCriteria <= int(max):
            result = result + 1

    return result

def partTwoValidPasswords(parsedInputs):
    result = 0

    for parsedInput in parsedInputs:
        position1= int(parsedInput[0]) - 1
        position2 = int(parsedInput[1]) - 1
        passwordCriteria = parsedInput[2]
        password = parsedInput[3]

        if (password[position2] == passwordCriteria) ^ (password[position1] == passwordCriteria):
            result = result + 1

    return result

if __name__ == "__main__":
    allInputs = readAllInput()
    parsedInput = parseInput(allInputs)
    
    """ Part 1
    numValidPassword = numValidPasswords(parsedInput)
    print (numValidPassword)
    """

    partTwoValidPassword = partTwoValidPasswords(parsedInput)
    print (partTwoValidPassword)


    