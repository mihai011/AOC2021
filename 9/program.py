import numpy

def read_input():

  with open("input.txt")  as f:
    data = f.read().split("\n")

  data = [[int(i) for i in row] for row in data]

  return data

def part2(matrix):

  minimums = []
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      adj = []
      if i-1 >= 0:
        adj.append(matrix[i-1][j])
      if i+1 < len(matrix):
        adj.append(matrix[i+1][j])
      if j-1 >= 0:
        adj.append(matrix[i][j-1])
      if j+1 < len(matrix[0]):
        adj.append(matrix[i][j+1])

      minimum = min(adj)
      if minimum > matrix[i][j]:
        minimums.append((i,j))

  sizes = []
  for m in minimums:

    step = [m]
    basin = [m]

    while len(step) != 0:
      new_step = []
      for s in step:
        if s[0]-1 >= 0 and matrix[s[0]-1][s[1]] < 9 and (s[0]-1,s[1]) not in basin+new_step:
          new_step.append((s[0]-1,s[1]))

        if s[0]+1 < len(matrix) and matrix[s[0]+1][s[1]] < 9 and (s[0]+1,s[1]) not in basin+new_step:
          new_step.append((s[0]+1,s[1]))
          
        if s[1]-1 >= 0 and matrix[s[0]][s[1]-1] < 9 and (s[0],s[1]-1) not in basin+new_step:
          new_step.append((s[0],s[1]-1))
         
        if s[1]+1 < len(matrix[0]) and matrix[s[0]][s[1]+1] < 9 and (s[0],s[1]+1) not in basin+new_step:
          new_step.append((s[0],s[1]+1))

      step = new_step
      basin.extend(new_step)

    sizes.append(len(basin))
  sizes.sort()
  print(sizes[-3:])
  return numpy.prod(sizes[-3:])
    

    
          

def part1(matrix):

  minimums = []
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      adj = []
      if i-1 >= 0:
        adj.append(matrix[i-1][j])
      if i+1 < len(matrix):
        adj.append(matrix[i+1][j])
      if j-1 >= 0:
        adj.append(matrix[i][j-1])
      if j+1 < len(matrix[0]):
        adj.append(matrix[i][j+1])

      minimum = min(adj)
      if minimum > matrix[i][j]:
        minimums.append(matrix[i][j])

  risks = [i+1 for i in minimums]

  return sum(risks)
      

if __name__=="__main__":

  matrix = read_input()

  res1 = part1(matrix)  
  print(res1)

  res2 = part2(matrix)  
  print(res2)