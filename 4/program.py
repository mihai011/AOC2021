import sys 

def make_board(string_board):

  board = []
  for line in string_board.split("\n"):
    if line!='':
      board.append([int(number.strip()) for number  in line.split(" ") if number != ''])

  return board

def get_numbers(board):

  numbers = []
  for line in board:
    for number in line:
      if type(number) == int:
        numbers.append(number)

  return numbers


def read_input(file):

  with open(file)as f:
    numbers = f.readline()
    numbers = [int(number) for number in numbers.split(",")]

    boards = f.read()
    string_boards = boards.split("\n\n")

    boards = []
    for string_board in string_boards:
      boards.append(make_board(string_board))

    return numbers, boards

def check_board(board):

  return any(all(True if number == True and type(number)==bool else False for number in line ) for line in board) or \
        any(all(True if number == True and type(number)==bool else False for number in line ) for line in zip(*board))

def part1():

  numbers, boards = read_input("input.txt")
  user_numbers = []

  for number in numbers:
    user_numbers.append(number)
    for board in boards:
      for line in board:
        for i in range(len(line)):
          if line[i] == number:
            line[i] = True
            if check_board(board):
              remaining_numbers = get_numbers(board)
              return sum(remaining_numbers) * user_numbers[-1]

def part2():

  numbers, boards = read_input("input.txt")
  user_numbers = []

  won_boards = []

  for number in numbers:
    user_numbers.append(number)
    for board in range(len(boards)):
      for line in boards[board]:
        for i in range(len(line)):
          if line[i] == number:
            line[i] = True
            if check_board(boards[board]) and board not in won_boards:
              won_boards.append(board)
            if len(won_boards) == len(boards):
              remaining_numbers = get_numbers(boards[board])
              return sum(remaining_numbers) * user_numbers[-1]



if __name__ == "__main__":

  res1 = part1()
  print(res1)
  res2 = part2()
  print(res2)
  

  
              
      

