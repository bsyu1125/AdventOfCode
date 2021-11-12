def readAllInput():
    f = open("input", "r")
    return f.read().splitlines()

def buildGraph(inputs):
  graph = {}

  for input in inputs:
    splitInput = input.split()
    loc1 = splitInput[0]
    loc2 = splitInput[2]
    distance = int(splitInput[4])

    if loc1 not in graph:
      graph[loc1] = {loc2: distance}
    else:
      graph[loc1][loc2] = distance

    if loc2 not in graph:
      graph[loc2] = {loc1: distance}
    else:
      graph[loc2][loc1] = distance

  return graph

def getAllPaths(graph):
  paths = []
  for start in graph:
    getPathsWithStart(graph, [start], start, 0, paths)
  return paths

def getPathsWithStart(graph, path, currentNode, distance, paths):
  if len(path) == len(graph):
    return (distance, path)

  for nextNode in graph[currentNode]:
    if nextNode not in path:    
      result = getPathsWithStart(graph, path + [nextNode], nextNode, distance + graph[currentNode][nextNode], paths)
      if result is not None:
        paths.append(result)
    
if __name__ == "__main__":
  inputs = readAllInput()
  graph = buildGraph(inputs)
  paths = getAllPaths(graph)

  print(max([i[0] for i in paths]))

