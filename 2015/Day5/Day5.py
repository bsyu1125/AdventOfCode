<<<<<<< Updated upstream
badStrings = ['ab', 'cd', 'pq', 'xy']
vowels = ['a', 'e', 'i', 'o', 'u']
=======
badStrings = ["ab", "cd", "pq", "xy"]
vowels = ["a", "e", "i", "o", "u"]
>>>>>>> Stashed changes

def readAllInput():
    f = open("input", "r")
    return f.read().splitlines()

<<<<<<< Updated upstream
def isNiceStringPart1(input: str):
  haveBadStrings = False
  vowelCount = 0
  twiceInRow = False

  if input[0] in vowels:
    vowelCount = 1

  for index in range(1, len(input)):
    prevIndex = index - 1
    currentLetter = input[index]
    prevLetter = input[prevIndex]

    # check bad strings
    if f"{prevLetter}{currentLetter}" in badStrings:
      haveBadStrings = True
      break

    if currentLetter in vowels:
      vowelCount = vowelCount + 1

    if not twiceInRow and prevLetter == currentLetter:
      twiceInRow = True

  return not haveBadStrings and twiceInRow and vowelCount >= 3

def isNiceStringPart2(input):

  hasLetterPair = False
  hasSandwichedLetter = False
  letterPairDict = {}

  for index in range(1, len(input)):
    currentLetter = input[index]
    prevLetter = input[index - 1]


    # check non overlapping pairs
    letterPair = f'{prevLetter}{currentLetter}'
    if letterPair in letterPairDict:
      letterPairIndexes = letterPairDict[letterPair]
      # check list of old letter pair indexes and if any exist that wasn't the one right before, there was a previous one
      if len(list(filter(lambda letterPairIndex: letterPairIndex != index - 1, letterPairIndexes))) > 0:
        hasLetterPair = True
    else:
      letterPairDict[letterPair] = [index]

    # check sandwiched letters
    if (index > 1):
      if input[index - 2] == currentLetter:
        hasSandwichedLetter = True
    
  return hasLetterPair and hasSandwichedLetter

if __name__ == "__main__":
  inputs = readAllInput()

  result = 0
  for input in inputs:
    if isNiceStringPart2(input):
      result = result + 1

  print(result)

=======
def countNiceStrings(allInputs):

    result = 0

    for input in allInputs:

        for badSubstrings in badStrings:
            if badSubstrings in input:
                break

        vowelCount = 0
        for vowel in vowels:
            if vowel in input:
                vowelCount = vowelCount + 1

        if vowelCount >= 3:
            result = result + 1

def isStringNice(input):
    

if __name__ == "__main__":
    allInputs = readAllInput()
>>>>>>> Stashed changes
