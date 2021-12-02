def readAllInput():
    f = open("input02.txt", "r")
    return f.read().splitlines()

def partOne(inputs: []):
  xPosition = 0
  yPosition = 0

  for input in inputs:
    inputSplit = input.split()
    command = inputSplit[0]
    position = int(inputSplit[1])

    if command == 'forward':
      xPosition += position
    elif command == 'down':
      yPosition += position
    elif command == 'up':
      yPosition -= position
    else:
      xPosition -= position
  
  return xPosition * yPosition

def partTwo(inputs: []):
  xPosition = 0
  aim = 0
  depth = 0

  for input in inputs:
    inputSplit = input.split()
    command = inputSplit[0]
    position = int(inputSplit[1])

    if command == 'forward':
      xPosition += position
      depth += (position * aim)
    elif command == 'down':
      aim += position
    elif command == 'up':
      aim -= position
  
  return xPosition * depth

if __name__ == "__main__":
  inputs = readAllInput()
  result = partTwo(inputs)
  print(result)
