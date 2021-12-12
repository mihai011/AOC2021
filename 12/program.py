
from collections import defaultdict


def read_input():

  with open("input.txt") as f:
    data = f.read().split("\n")
    data = [line.split("-") for line in data]

  return data

paths = 0


def make_path_util(u, d, visited, graph, path):

  global paths

  #  Mark the current node as visited and store in path
  if u.islower():
    visited[u]= True
  path.append(u)

  # If current vertex is same as destination, then print
  # current path[]
  if u == d:
      paths += 1
  else:
      # If current vertex is not destination
      # Recur for all the vertices adjacent to this vertex
      for i in graph[u]:
          if visited[i] == False:
              make_path_util(i, d, visited, graph,  path)
                
  # Remove current vertex from path[] and mark it as unvisited
  path.pop()
  if u.islower():
    visited[u]= False

def make_path(s, dest, data):

  graph = defaultdict(list)
  visited = {}

  for d in data:
    graph[d[0]].append(d[1])
    graph[d[1]].append(d[0])
    visited[d[0]] = False
    visited[d[1]] = False


  # Create an array to store paths
  path = []

  # Call the recursive helper function to print all paths
  make_path_util(s, dest, visited, graph, path)

def part1(data):

  make_path("start", "end", data)

def check_path(path):

  total = 0
  visits = {}
  for e in path:
    if e.islower():
      if e not in ["start", "end"]:
        if e not in visits:
          visits[e] = 1
        else:
          visits[e] += 1

  multiple_vists=[]
  for k,v in visits.items():
    if v > 1:
      multiple_vists.append(k)

  if len(multiple_vists) > 1:
    return False
  return True

    
def make_path_util2(u, d, visited, graph, path):

  global paths

  #  Mark the current node as visited and store in path
  if u.islower() and visited[u] < 2:
    visited[u] += 1
  path.append(u)

  # If current vertex is same as destination, then print
  # current path[]
  if u == d:
    if check_path(path):
      paths += 1
      # print(paths)
  else:
      # If current vertex is not destination
      # Recur for all the vertices adjacent to this vertex
      for i in graph[u]:
        if visited[i] < 2 and i != 'start' and check_path(path):
          make_path_util2(i, d, visited, graph,  path)
                
  # Remove current vertex from path[] and mark it as unvisited
  path.pop()
  if u.islower():
    visited[u] -= 1 

def make_path2(s, dest, data):

  graph = defaultdict(list)
  visited = {}

  for d in data:
    graph[d[0]].append(d[1])
    graph[d[1]].append(d[0])
    visited[d[0]] = 0
    visited[d[1]] = 0

  # Create an array to store paths
  path = []

  # Call the recursive helper function to print all paths
  make_path_util2(s, dest, visited, graph, path)

def part2(data):

  make_path2("start", "end", data)


if __name__ == "__main__":

  data = read_input()

  part1(data)
  print(paths)
  paths = 0

  part2(data)
  print(paths)

