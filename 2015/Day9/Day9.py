def readAllInput():
    f = open("input", "r")
    return f.read().splitlines()

    
if __name__ == "__main__":
  inputs = readAllInput()
  result = getEncodeAllStrings(inputs)
  print (result)

