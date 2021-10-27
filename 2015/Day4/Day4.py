import hashlib

def readInput():
    f = open("input", "r")
    return f.readline()

def sockStuffer(input: str):

  hashResult = ''
  answer = 0

  while hashResult[:6] != '000000':
    answer = answer + 1
    hashInput = input + str(answer)
    hashResult = hashlib.md5(hashInput.encode()).hexdigest()

  return answer

if __name__ == "__main__":
  input = readInput()
  result = sockStuffer(input)
  print(result)