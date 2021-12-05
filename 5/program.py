
def make_input():

  with open("input.txt") as f:
    data = f.read().split("\n")
    data = [row.split("->") for row in data]
    data = [(row[0].split(","), row[1].split(",")) for row in data]
    data = [((int(row[0][0]), int(row[0][1])),(int(row[1][0]), int(row[1][1]))) for row in data]
    
    max_x = max(max([row[0][0] for row in data]), max([row[1][0] for row in data]))
    max_y = max(max([row[0][1] for row in data]), max([row[1][1] for row in data]))

    board = [[0 for _ in range(max_x+1)] for _ in range(max_y+1)]

    return data, board


def print_board(board):

  board = "\n".join([''.join([str(e) for e in row]) for row in board])
  print(board)


def part1(intervals, board):

  for interval in intervals:
    if interval[0][0] == interval[1][0] or interval[0][1] == interval[1][1]:
      if interval[0][0] != interval[1][0]:
        if interval[0][0] < interval[1][0]:
          for i in range(interval[0][0], interval[1][0]+1):
            board[interval[0][1]][i] += 1
        else:
          for i in range(interval[1][0], interval[0][0]+1):
            board[interval[0][1]][i] += 1
      else:
        if interval[0][1] < interval[1][1]:
          for i in range(interval[0][1], interval[1][1]+1):
            board[i][interval[0][0]] += 1
        else:
          for i in range(interval[1][1], interval[0][1]+1):
            board[i][interval[0][0]] += 1
  
  # print_board(board)

  return sum(len([element for element in row if element > 1]) for row in board)


def part2(intervals, board):

  for interval in intervals:
    if (interval[0][0] == interval[1][0] and interval[0][1] != interval[1][1]) or \
      (interval[0][0] != interval[1][0] and interval[0][1] == interval[1][1]):
      if interval[0][0] != interval[1][0]:
        if interval[0][0] < interval[1][0]:
          for i in range(interval[0][0], interval[1][0]+1):
            board[interval[0][1]][i] += 1
        else:
          for i in range(interval[1][0], interval[0][0]+1):
            board[interval[0][1]][i] += 1
      else:
        if interval[0][1] < interval[1][1]:
          for i in range(interval[0][1], interval[1][1]+1):
            board[i][interval[0][0]] += 1
        else:
          for i in range(interval[1][1], interval[0][1]+1):
            board[i][interval[0][0]] += 1

    if abs(interval[0][1]-interval[1][1]) == abs(interval[0][0]-interval[1][0]):
      if interval[0][0] == interval[0][1] and interval[1][0] == interval[1][1]:
        if interval[0][0] > interval[1][0]:
          for i in range(interval[0][0] - interval[1][0]+1):
            board[interval[0][0]-i][interval[0][1]-i] += 1
        else:
          for i in range(interval[1][0] - interval[0][0]+1):
            board[interval[0][0]+i][interval[0][1]+i] += 1
      else:
        if interval[0][0] > interval[1][0] and interval[0][1] > interval[1][1]:
          for i in range(interval[0][0] - interval[1][0]+1):
            board[interval[0][1]-i][interval[0][0]-i] += 1
        if interval[0][0] > interval[1][0] and interval[0][1] < interval[1][1]:
          for i in range(interval[0][0] - interval[1][0]+1):
            board[interval[0][1]+i][interval[0][0]-i] += 1
        if interval[0][0] < interval[1][0] and interval[0][1] > interval[1][1]:
          for i in range(interval[1][0] - interval[0][0]+1):
            board[interval[0][1]-i][interval[0][0]+i] += 1
        if interval[0][0] < interval[1][0] and interval[0][1] < interval[1][1]:
          for i in range(interval[1][0] - interval[0][0]+1):
            
            board[interval[0][1]+i][interval[0][0]+i] += 1

  # print_board(board)

  return sum(len([element for element in row if element > 1]) for row in board)


if __name__ == "__main__":

  intervals, board = make_input()
  res1 = part1(intervals, board)
  print(res1)
  
  intervals, board = make_input()
  res1 = part2(intervals, board)
  print(res1)