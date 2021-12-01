import json

import sys
sys.setrecursionlimit(100000)

def readInput():
    f = open("input", "r")
    return f.readline()

def findSum(input: str):
  result = 0

  jsonObj = json.loads(input)
  print(jsonObj)

  if type(jsonObj) == dict:
    result += getSumDictionary(jsonObj)
  else:
    result += getSumList(jsonObj)

  return result

def getSumDictionary(input):
  result = 0
  print ('type dict')
  for key in input:
    value = input[key]
    if type(value) == int:
      result += value
    elif type(value) == dict:
      result += getSumDictionary(value)
    elif type(value) == list:
      result += getSumList(value)
    elif value == "red":
      return 0

  return result

def getSumList(input):
  result = 0

  print('type list')
  print(f'input {input}')
  for item in input:
    if type(item) == int:
      result += item
    elif type(item) == dict:
      result += getSumDictionary(item)
    elif type(item) == list:
      result += getSumList(item)
  return result

if __name__ == "__main__":
  input = readInput()

  result = findSum(input)
  print(result)