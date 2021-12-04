import itertools

def readAllInput():
    f = open("input", "r")
    return f.read().splitlines()

def makeGraph(input: list):
    result = {}

    for line in input:
        line = line.replace('.', '')
        splitLine = line.split(' ')
        start = splitLine[0]
        neighbor = splitLine[-1]
        gainOrLose = splitLine[2]
        happinessGain = int(splitLine[3]) if gainOrLose == 'gain' else int(splitLine[3]) * -1

        if start in result:
            result[start][neighbor] = happinessGain

        else:
            result[start] = {neighbor: happinessGain}

    return result

def makeGraphWithYou(input: list):
    result = {}

    for line in input:
        line = line.replace('.', '')
        splitLine = line.split(' ')
        start = splitLine[0]
        neighbor = splitLine[-1]
        gainOrLose = splitLine[2]
        happinessGain = int(splitLine[3]) if gainOrLose == 'gain' else int(splitLine[3]) * -1

        if start in result:
            result[start][neighbor] = happinessGain

        else:
            result[start] = {neighbor: happinessGain}
            result[start]['you'] = 0

        if 'you' in result:
            result['you'][start] = 0
        else:
            result['you'] = {start: 0}

    return result

def makeArrangements(input):
    result = []

    permutations = list(itertools.permutations(input[1:]))
    for permutation in permutations:
        permutationList = list(permutation)
        permutationList.append(input[0])
        result.append(permutationList)

    return result

def mostHappiness(graph):
    result = 0
    arrangements = makeArrangements(list(graph.keys()))
    for arrangement in arrangements:
        happinessForCurrentArrangement = 0
        for index in range(len(arrangement)):
            currentPerson = arrangement[index]
            leftPerson = arrangement[index - 1]


            if index == len(arrangement) - 1:
                rightPerson = arrangement[0]
            else:
                rightPerson = arrangement[index + 1]

            happinessLeft = graph[currentPerson][leftPerson]
            happinessRight = graph[currentPerson][rightPerson]
            happinessForCurrentPerson = happinessLeft + happinessRight
            happinessForCurrentArrangement += happinessForCurrentPerson
        
        result = max(happinessForCurrentArrangement, result)

    return result

if __name__ == "__main__":
    lines = readAllInput()
    graph = makeGraphWithYou(lines)
    print(graph)
    result = mostHappiness(graph)
    print(result)
    
