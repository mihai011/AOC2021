  # import itertools package
import itertools
from itertools import permutations


digits = {'0':{'a', 'b', 'c', 'e', 'f', 'g'}, \
          '1':{'c', 'f'}, \
          '2':{'a', 'c', 'd', 'e', 'g'}, \
          '3':{'a', 'c', 'd', 'f', 'g'}, \
          '4':{'b', 'c', 'd', 'f'}, \
          '5':{'a', 'b', 'd', 'f', 'g'}, \
          '6':{'a', 'b', 'd', 'e', 'f', 'g'}, 
          '7':{'a', 'c', 'f'}, \
          '8':{'a', 'b', 'c', 'd', 'e', 'f', 'g'}, \
          '9':{'a', 'b', 'c', 'd', 'f', 'g'}}

unique = {'1':2, '4':4, '7':3, '8':7}

def contains(a, b):

  for i in a:
    if i not in b:
      return False

  return True

def read_input():

  with open("input.txt") as f:
    data = f.read().split("\n")

  rows = [d.split(" | ") for d in data]
  rows = [([set(n) for n in d[0].split(" ")],[set(n) for n in d[1].split(" ")]) for d in rows]

  return rows

  
def part2(rows):

  total_sum = 0

  for row in rows:
    certs = {}
    for a in row[0]:
      for key in unique.keys():
        if len(a) == unique[key]:
          certs[key] = a 

    for a in row[0]:
      if len(a) == 6:
        if contains(certs['4'], a):
          certs['9'] = a
        elif contains(certs['1'], a):
          certs['0'] = a
        else:
          certs['6'] = a

    for a in row[0]:
      if len(a) == 5:
        if contains(certs['1'], a):
          certs['3'] = a
        elif contains(a, certs['9']):
          certs['5'] = a
        else:
          certs['2'] = a
          

    total = ''
    for s in row[1]:
      for e in certs:
        if certs[e] == s:
          total += e

    total_sum += int(total)

  return total_sum
    

def part1(rows):

  total = 0

  for row in rows:
    for a in row[1]:
      for key in unique.keys():
        if len(a) == unique[key]:
          total+=1
    
  return total


if __name__ == "__main__":

  rows = read_input()
  res1 = part1(rows)
  print(res1)

  res2 = part2(rows)
  print(res2)
