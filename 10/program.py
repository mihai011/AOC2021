

def read_input():

  with open("input.txt") as f:
    data = f.read().split("\n")

  return data

def part2(data):

  total = 0
  incomplete = []

  for line in data:
    stack = []
    corrupted = False
    for c in line:
      if len(stack) == 0:
        stack.append(c)
      if stack[-1] == "{" and c == "}":
        stack.pop()
        continue
      if stack[-1] == "[" and c == "]":
        stack.pop()
        continue
      if stack[-1] == "(" and c == ")":
        stack.pop()
        continue
      if stack[-1] == "<" and c == ">":
        stack.pop()
        continue
      if c == ")":
        corrupted = True
        break
      if c == "]":
        corrupted = True
        break
      if c == "}":
        corrupted = True
        break
      if c == ">":
        corrupted = True
        break
      stack.append(c)
    
    if corrupted:
      continue
    incomplete.append(line)

  stacks = []
  for line in incomplete:
    stack = []
    for c in line:
      if len(stack) == 0:
        stack.append(c)
        continue
      if stack[-1] == "{" and c == "}":
        stack.pop()
        continue
      if stack[-1] == "[" and c == "]":
        stack.pop()
        continue
      if stack[-1] == "(" and c == ")":
        stack.pop()
        continue
      if stack[-1] == "<" and c == ">":
        stack.pop()
        continue
      stack.append(c)

    stacks.append(stack)

  scores = []
  for line in stacks:
    score = 0
    line = line[::-1]
    for c in line:
      if c == "(":
        score = score*5 + 1
      if c == "[":
        score = score*5 + 2
      if c == "{":
        score = score*5 + 3
      if c == "<":
        score = score*5 + 4

    scores.append(score)
  
  scores.sort()
  return scores[len(scores)//2]

      


  return total

def part1(data):

  total = 0

  for line in data:
    stack = []
    for c in line:
      if len(stack) == 0:
        stack.append(c)
      if stack[-1] == "{" and c == "}":
        stack.pop()
        continue
      if stack[-1] == "[" and c == "]":
        stack.pop()
        continue
      if stack[-1] == "(" and c == ")":
        stack.pop()
        continue
      if stack[-1] == "<" and c == ">":
        stack.pop()
        continue
      if c == ")":
        total += 3
        break
      if c == "]":
        total += 57
        break
      if c == "}":
        total += 1197
        break
      if c == ">":
        total += 25137
        break
      stack.append(c)

  return total
      

if __name__ == "__main__":

  data = read_input()
  res1 = part1(data)
  print(res1)

  res2 = part2(data)
  print(res2)
