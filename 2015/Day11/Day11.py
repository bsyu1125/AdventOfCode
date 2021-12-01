def readInput():
    f = open("input", "r")
    return f.readline()

def getNextPassword(input: str):
  result = input
  while not isPasswordValid(result):
    result = incrementPassword(result)
  return result

def isPasswordValid(input: str):
  # no i, o, l's
  if any(badChar in input for badChar in ['i', 'o', 'l'] ):
    return False
  
  numPairs = 0
  skipNextBecauseOverlapPair = False
  increasingStraightCount = 0
  hasIncreasingStraightCount = False

  for index in range(1, len(input)):
    prevChar = input[index-1]
    currentChar = input[index]

    # increasing straight
    if not hasIncreasingStraightCount:
      if ord(prevChar) == ord(currentChar) - 1:
        increasingStraightCount += 1
      else:
        increasingStraightCount = 0
      
      if increasingStraightCount >= 2:
        hasIncreasingStraightCount = True

    # two different non-overlapping pairs
    if numPairs >= 2 or skipNextBecauseOverlapPair:
      skipNextBecauseOverlapPair = False
      continue
    else:
      if prevChar == currentChar:
        numPairs += 1
        skipNextBecauseOverlapPair = True

  # print(f'num pairs {numPairs}')
  # print(f'has increasing straight {hasIncreasingStraightCount}')

  return numPairs >= 2 and hasIncreasingStraightCount

def incrementPassword(input: str):
  index = -1
  while True:
    currentChar = input[index]

    if currentChar == 'i' or currentChar == 'o' or currentChar == 'l':
      input = incrementIOL(input)
    if currentChar == 'z':      
      input = replaceCharAtIndex(input, index, 'a')
      index -= 1
    else:
      input = replaceCharAtIndex(input, index, chr(ord(currentChar) + 1))
      index = 0
    
      if index >= 0:
        break

  return input

def incrementIOL(input: str):
  print (input)

  for index in range(len(input)):
    currentChar = input[index]
    if currentChar == 'i' or currentChar == 'o' or currentChar == 'l':
      input = replaceCharAtIndex(input, index, chr(ord(currentChar) + 1))
      index += 1
      while index < len(input):
        input = replaceCharAtIndex(input, index, 'a')
        index += 1

  return input


def replaceCharAtIndex(input: str, index: int, replaceChar: str):
  newList = list(input)
  newList[index] = replaceChar
  return "".join(newList)


if __name__ == "__main__":
  input = readInput()
  # input = incrementIOL(input)
  result = getNextPassword(input)
  print(result)