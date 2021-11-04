def readAllInput():
    f = open("input", "r")
    return f.read().splitlines()

def getAllCharactersCode(inputs):
  result = 0
  for input in inputs:
    result += getCharactersCode(input)
  return result

def getCharactersCode(input):
  quoteStrippedInput = input[1:-1]

  charInMem = 0
  index = 0
  while index < len(quoteStrippedInput):
    currentChar = quoteStrippedInput[index]
    if currentChar != '\\':
      charInMem += 1
      index += 1
    else:
      nextChar = quoteStrippedInput[index + 1]
      if nextChar == 'x':
        index += 4
        charInMem += 1
      else:
        index += 2
        charInMem += 1

  return len(input) - charInMem

def getEncodeAllStrings(inputs):
  result = 0
  for input in inputs:
    result += getEncodeString(input)
  return result

def getEncodeString(input):
  numQuoteOccurr = input.count('"')
  numSlashOccurr = input.count("\\")

  totalEncodeLength = len(input) + numQuoteOccurr + numSlashOccurr + 2
  return totalEncodeLength - len(input)
  

if __name__ == "__main__":
  inputs = readAllInput()
  result = getEncodeAllStrings(inputs)
  print (result)

