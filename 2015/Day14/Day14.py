import math

def readAllInput():
    f = open("input", "r")
    return f.read().splitlines()

def getMaxDistance(input, time):
    result = 0

    for line in input:
        splitLine = line.split(' ')
        speed = int(splitLine[3])
        flightTime = int(splitLine[6])
        restTime = int(splitLine[-2])

        distance = 0
        rounds = math.floor(time / (flightTime + restTime))
        remainder = time % (flightTime + restTime)
        distance = rounds * speed * flightTime
        print(distance)
        if remainder > flightTime:
            distance += speed * flightTime
        else:
            distance += speed * remainder

        print(distance)
        
        result = max(result, distance)

    return result

def getPoints(input, time):
    speedDict = {}

    for index in range(len(input)):
        line = input[index]
        splitLine = line.split(' ')
        speed = int(splitLine[3])
        flightTime = int(splitLine[6])
        restTime = int(splitLine[-2])

        speedDict[str(index)] = (speed, flightTime, restTime)

    pointTracker = [0] * len(speedDict)
    distanceTracker = [0] * len(speedDict)
    
    for currentSec in range(1, time + 1):
        for key in speedDict:
            speed = speedDict[key][0]
            flightTime = speedDict[key][1]
            restTime = speedDict[key][2]

            remainder = currentSec % (flightTime + restTime)

            distanceGained = 0
            if remainder > 0 and remainder <= flightTime:
                distanceGained = speed
            else:
                distanceGained = 0

            distanceTracker[int(key)] += distanceGained
            
        max_item = max(distanceTracker)
        index_list = [index for index in range(len(distanceTracker)) if distanceTracker[index] == max_item]
        for index in index_list:
            pointTracker[index] += 1

    return max(pointTracker)

if __name__ == "__main__":
    lines = readAllInput()
    result = getPoints(lines, 2503)
    print(result)
