import pprint
def readAllInput():
    f = open("input", "r")
    return f.read().splitlines()

def makeGraph(lines):
  graph = {}

  for line in lines:
    splitByArrow = line.split("->")
    
    leftSideOfArrow = splitByArrow[0].strip()
    graphKey = splitByArrow[1].strip()

    leftSideOfArrowList = leftSideOfArrow.split()
    node = {}

    print(leftSideOfArrowList)

    if len(leftSideOfArrowList) == 1:
      if leftSideOfArrowList[0].strip().isnumeric():
        node['value'] = leftSideOfArrowList[0].strip()
      else:
        node['dependencies'] = [leftSideOfArrowList[0].strip()]
    elif 'NOT' in leftSideOfArrowList:
      node['operation'] = 'NOT'
      node['dependencies'] = [leftSideOfArrowList[1].strip()]
    else:
      node['operation'] = leftSideOfArrowList[1].strip()
      node['dependencies'] = [leftSideOfArrowList[0].strip(), leftSideOfArrowList[2].strip()]
    
    graph[graphKey] = node

  return graph

def findSignal(graph, input):
  return findSignalRecursive(graph, input)

def findSignalRecursive(graph, input):
  print(f"going to {input}")

  if input.isnumeric():
     return int(input)

  if 'value' in graph[input]:
    return int(graph[input]['value'])

  if 'operation' in graph[input]:

    operation = graph[input]['operation']

    if operation == 'NOT':
      return ~(findSignalRecursive(graph, graph[input]['dependencies'][0]))
    elif operation == 'AND':
      dependency1 = findSignalRecursive(graph, graph[input]['dependencies'][0])
      dependency2 = findSignalRecursive(graph, graph[input]['dependencies'][1])
      result = dependency1 & dependency2
      graph[input]['value'] = result
      return result
    elif operation == 'OR':
      dependency1 = findSignalRecursive(graph, graph[input]['dependencies'][0])
      dependency2 = findSignalRecursive(graph, graph[input]['dependencies'][1])
      result = dependency1 | dependency2
      graph[input]['value'] = result
      return result
    elif operation == 'LSHIFT':
      dependency1 = findSignalRecursive(graph, graph[input]['dependencies'][0])
      dependency2 = int(graph[input]['dependencies'][1])
      result = dependency1 << dependency2
      graph[input]['value'] = result
      return result
    elif operation == 'RSHIFT':
      dependency1 = findSignalRecursive(graph, graph[input]['dependencies'][0])
      dependency2 = int(graph[input]['dependencies'][1])
      result = dependency1 >> dependency2
      graph[input]['value'] = result
      return result
  else:
      result = findSignalRecursive(graph, graph[input]['dependencies'][0])
      graph[input]['value'] = result
      return result


if __name__ == "__main__":
  inputs = readAllInput()
  graph = makeGraph(inputs)
  pprint.pprint(graph)

  result = findSignal(graph, 'a')
  print (result)

