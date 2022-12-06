#!/usr/bin/python3
with open("input.txt") as f:
  string = f.read()

def parse(letter, _string):
  print(f"parsing {letter} in {_string}")
  if len(_string) == 1:
    if letter not in _string:
      return True
    else:
      return False
  if letter in _string:
    return False
  if letter not in _string:
    return parse(_string[:1], _string[1:])
  
LENGTH = 14

for idx in range(0, len(string)):
  print(f"idx: {idx}")
  result = parse(string[idx], string[idx + 1: idx + LENGTH])
  if result == True:
    print(f"{idx + LENGTH} {result}")
    break
    
