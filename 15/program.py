from os import read
from numpy import inf
import sys
from queue import PriorityQueue

from networkx import DiGraph
from networkx import shortest_path

import numpy as np

def inc(x):

  if x == 9:
    return 1
  return x + 1

def increment_map(map):
  return [[inc(x) for x in line] for line in map]

def part1_and_2(part_2):

  with open("input.txt") as f:
    data = [[int(x) for x in line] for line in f.read().split("\n")]

  if part_2:
    first_row = [data]
    for _ in range(4):
      first_row.append(increment_map(first_row[-1]))
    first_row = np.concatenate(first_row, axis=1)
    rows = [first_row]
    for _ in range(4):
      rows.append(increment_map(rows[-1]))
    data = np.concatenate(rows)

  g = DiGraph()
  max_y_pos = len(data)-1
  max_x_pos = len(data[0])-1

  for i in range(len(data)):
    for j in range(len(data[0])):
      for p in [(1, 0), (-1, 0) , (0, 1), (0,-1)]:
        if i+p[0] >=0 and i+p[0] < len(data) and j+p[1] >=0 and j+p[1] < len(data[0]):
          
          g.add_edge((i,j), (i+p[0], j+p[1]), weight=data[i+p[0]][j+p[1]])

  shortest = shortest_path(g, (0, 0), (max_y_pos,max_x_pos), weight="weight")
  result = 0
  for i in range(len(shortest)-1):
      result += g[shortest[i]][shortest[i+1]]["weight"]
  return result

  


if __name__ == "__main__":

  res1 = part1_and_2(False)
  print(res1)

  res2 = part1_and_2(True)
  print(res2)