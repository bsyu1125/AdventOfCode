def readAllInput():
    f = open("input01.txt", "r")
    return f.read().splitlines()

def countNumIncrements(inputs: []):
  result = 0
  prev = int(inputs[0])
  for index in range(1, len(inputs)):
    current = int(inputs[index])
    if prev < current:
      result += 1
    
    prev = current
  return result

def countNumIncrementsPartTwo(inputs: []):
  result = 0

  measurement1 = int(inputs[0])
  measurement2 = int(inputs[1])
  measurement3 = int(inputs[2])

  for index in range(3, len(inputs)):
    currentMeasurement = int(inputs[index])
    previousWindow = measurement1 + measurement2 + measurement3
    currentWindow = measurement2 + measurement3 + currentMeasurement
    if previousWindow < currentWindow:
      result += 1

    measurement1 = measurement2
    measurement2 = measurement3
    measurement3 = currentMeasurement

  return result


if __name__ == "__main__":
  inputs = readAllInput()
  result = countNumIncrementsPartTwo(inputs)
  print(result)
