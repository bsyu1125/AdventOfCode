def readAllInput():
    f = open("input04.txt", "r")
    return f.read().splitlines()

def getBingoNumbers(inputs: []):
  return inputs[0].split(',')

def getBingoCards(inputs: []):
  result = []

  bingoCard = []

  for inputIndex in range(2, len(inputs)):
    if len(inputs[inputIndex]) == 0:
      result.append(bingoCard)
      bingoCard = []
    else:
      bingoCard.append(inputs[inputIndex].split())

  result.append(bingoCard)

  return result

def isBingoCardWinning(card: []):
  for row in card:
    if row 

def partOne(numbers: [], cards: []):  

  print(numbers)
  print(cards)

  return 


if __name__ == "__main__":
  inputs = readAllInput()
  numbers = getBingoNumbers(inputs)
  cards = getBingoCards(inputs)
  result = partOne(numbers, cards)
  print(result)
