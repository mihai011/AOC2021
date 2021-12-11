def read_input():

  with open("input.txt") as f:
    data = f.read().split("\n")

  data = [[int(e) for e in line] for line in data]

  return data

def print_matrix(matrix):

  print("\n".join([''.join([str(i) for i in line]) for line in matrix]))


def part1(matrix, all_flash):

  steps = [(0,1), (1,0), (1,1), (0, -1), (-1, 0), (-1, -1), (-1,  1), (1, -1)]

  flashes = 0
  paces = 100
  if all_flash:
    paces = 1000000000

  for pace in range(paces):
    # print_matrix(matrix)
    # print()

    flashed = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    for i in range(len(matrix)):
      for j in range(len(matrix[0])):

        matrix[i][j] += 1 

        if matrix[i][j] > 9:
          flashed[i][j] = True
          flashes += 1
          matrix[i][j] = 0
          for s in steps:
            if i+s[0] >= 0 and i+s[0] < len(matrix) and j+s[1] >= 0 and j+s[1] < len(matrix[0]) and not flashed[i+s[0]][j+s[1]]:
              matrix[i+s[0]][j+s[1]] += 1
    
    still = True
    while still:
      still = False
      for i in range(len(matrix)):
        for j in range(len(matrix[0])):

          if matrix[i][j] > 9:
            flashed[i][j] = True
            flashes += 1
            matrix[i][j] = 0
            for s in steps:
              if i+s[0] >= 0 and i+s[0] < len(matrix) and j+s[1] >= 0 and j+s[1] < len(matrix[0]) and not flashed[i+s[0]][j+s[1]]:
                matrix[i+s[0]][j+s[1]] += 1
    
    if all_flash:
      if all([all(line) for line in flashed]):
        return pace
    
          
      for i in range(len(matrix)):
        for j in range(len(matrix[0])):
          if matrix[i][j] > 9:
            still = True
            break
    

    

    # print_matrix(matrix)
    # print()
  
  return flashes


if __name__ == "__main__":

  data = read_input()
  res1 = part1(data, False)
  print(res1)

  res2 = part1(data, True)
  print(res2)
