import copy
import math

def readAllInput():
    f = open("input09.txt", "r")
    return f.read().splitlines()

def convertToNums(inputs):

  result = []

  for input in inputs:
    rowResult = []
    for character in input:
      rowResult.append(int(character))
    result.append(rowResult)

  return result

def partOne(inputs):  
  result = 0

  for rowIndex in range(len(inputs)):
    for colIndex in range(len(inputs[rowIndex])):
      numLowPoints = 0
      currentHeight = inputs[rowIndex][colIndex]
      numMissingSides = 0

      # if we're not at the left most side, we can look to the left
      if colIndex != 0:
        if currentHeight < inputs[rowIndex][colIndex - 1]:
          numLowPoints += 1
      else:
        numMissingSides += 1

      # if we're not at the right most side, we can look to the right
      if colIndex != len(inputs[rowIndex]) - 1:
        if currentHeight < inputs[rowIndex][colIndex + 1]:
          numLowPoints += 1
      else:
        numMissingSides += 1

      # if we're not at the top most side, we can look up
      if rowIndex != 0:
        if currentHeight < inputs[rowIndex - 1][colIndex]:
          numLowPoints += 1
      else:
        numMissingSides += 1

      # if we're not at the bottom most side, we can look down
      if rowIndex != len(inputs) - 1:
        if currentHeight < inputs[rowIndex + 1][colIndex]:
          numLowPoints += 1
      else:
        numMissingSides += 1

      if numLowPoints == 4 - numMissingSides:
          result += (currentHeight + 1)   
  
  return result

def getCoordinateOfLows(inputs):  
  result = []

  for rowIndex in range(len(inputs)):
    for colIndex in range(len(inputs[rowIndex])):
      numLowPoints = 0
      currentHeight = inputs[rowIndex][colIndex]
      numMissingSides = 0

      # if we're not at the left most side, we can look to the left
      if colIndex != 0:
        if currentHeight < inputs[rowIndex][colIndex - 1]:
          numLowPoints += 1
      else:
        numMissingSides += 1

      # if we're not at the right most side, we can look to the right
      if colIndex != len(inputs[rowIndex]) - 1:
        if currentHeight < inputs[rowIndex][colIndex + 1]:
          numLowPoints += 1
      else:
        numMissingSides += 1

      # if we're not at the top most side, we can look up
      if rowIndex != 0:
        if currentHeight < inputs[rowIndex - 1][colIndex]:
          numLowPoints += 1
      else:
        numMissingSides += 1

      # if we're not at the bottom most side, we can look down
      if rowIndex != len(inputs) - 1:
        if currentHeight < inputs[rowIndex + 1][colIndex]:
          numLowPoints += 1
      else:
        numMissingSides += 1

      if numLowPoints == 4 - numMissingSides:
          result.append((rowIndex, colIndex))
  
  return result

def createGraph(inputs):
  graph = {}
  for rowIndex in range(len(inputs)):
    graph[rowIndex] = {}
    for colIndex in range(len(inputs[rowIndex])):
      graph[rowIndex][colIndex] = [inputs[rowIndex][colIndex], False]
  return graph

def partTwo(originalGraph, coordinateOfLows):
  basinSizes = []
  for coordinateOfLow in coordinateOfLows:
    graph = copy.deepcopy(originalGraph)

    basinSize = getBasinSize(graph, coordinateOfLow, 1)
    basinSizes.append(basinSize)

  result = sorted(basinSizes, reverse=True)[:3]

  return math.prod(result)

def getBasinSize(graph, coordinateOfLow, result):
  rowIndex = coordinateOfLow[0]
  colIndex = coordinateOfLow[1]
  graph[rowIndex][colIndex][1] = True

  # if we're not at the left most side, we can look to the left
  if colIndex != 0:
    newCoordinate = graph[rowIndex][colIndex - 1]
    if newCoordinate[0] != 9 and newCoordinate[1] != True:
      result = getBasinSize(graph, (rowIndex, colIndex - 1), result + 1)

  # if we're not at the right most side, we can look to the right
  if colIndex != len(inputs[rowIndex]) - 1:
    newCoordinate = graph[rowIndex][colIndex + 1]
    if newCoordinate[0] != 9 and newCoordinate[1] != True:
      result = getBasinSize(graph, (rowIndex, colIndex + 1), result + 1)

  # if we're not at the top most side, we can look up
  if rowIndex != 0:
    newCoordinate = graph[rowIndex - 1][colIndex]
    if newCoordinate[0] != 9 and newCoordinate[1] != True:
      result = getBasinSize(graph, (rowIndex - 1, colIndex), result + 1)

  # if we're not at the bottom most side, we can look down
  if rowIndex != len(inputs) - 1:
    newCoordinate = graph[rowIndex + 1][colIndex]
    if newCoordinate[0] != 9 and newCoordinate[1] != True:
      result = getBasinSize(graph, (rowIndex + 1, colIndex), result + 1)

  return result

if __name__ == "__main__":
  rawInput = readAllInput()
  inputs = convertToNums(rawInput)
  coordinatesOfLows = getCoordinateOfLows(inputs)
  graph = createGraph(inputs)  
  result = partTwo(graph, coordinatesOfLows)

  print(result)
