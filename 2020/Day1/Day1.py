def readAllInput():
    f = open("input", "r")
    return f.read().splitlines()

def solve(allInputs):
    for input in allInputs:
        target = 2020 - int(input)
        """
        if (str(target) in allInputs):
            return target * int(input)
        """
        for secondNumber in allInputs:
            target2 = target - int(secondNumber)

            if (str(target2) in allInputs):
                return target2 * int(secondNumber) * int(input)

    return 0

if __name__ == "__main__":
    allInputs = readAllInput()

    result = solve(allInputs)
    print(result)
