
from os import read


def read_input():

  with open("input.txt") as f:
    data = [int(e) for e in f.read().split(',')]

  return data

def part1(crabs):

  crabs.sort()
  med = crabs[len(crabs)//2]

  cost = sum([abs(med-c) for c in crabs])

  return cost


def part2(crabs):

  small = min(crabs)
  big = max(crabs)
  crabs.sort()
  max_int = 9999999999999999999
  for i in range(small, big):
    s = sum([(abs(i-c)**2 + abs(i-c))//2 for c in crabs])
    if s < max_int:
      max_int = s 

  return max_int

if __name__ == "__main__":

  crabs = read_input()

  res1 = part1(crabs)
  print(res1)

  crabs = read_input()
  res2 = part2(crabs)
  print(res2)