
def read_input():

  with open("input.txt") as f:
    data = f.read().split("\n\n")

  coordinates = [(int(e.split(',')[0]), int(e.split(',')[1])) for e in data[0].split("\n")]
  folds = [(e.split("=")[0][-1], int(e.split("=")[1])) for e in data[1].split("\n")]

  return coordinates, folds

def print_paper(paper):

  print("\n".join(["".join([c[0] for c in line]) for line in paper]))
  print()

def count_dots(paper):

  return sum([line.count(["#"]) for line in paper])

def make_fold(paper, fold):

  if fold[0] == "x":
    
    distance = len(paper[0]) - fold[1]

    for d in range(1, distance + 1):
      for i in range(len(paper)):
        if paper[i][fold[1]-d+1] != ["#"]:
          paper[i][fold[1]-d+1] = paper[i][fold[1]+d-1]

    paper = [line[:fold[1]] for line in paper]

  if fold[0] == "y":

    distance = len(paper) - fold[1]

    for d in range(1, distance+1):
      for i in range(len(paper[0])):
        if paper[fold[1]-d+1][i] != ["#"]:
          paper[fold[1]-d+1][i] = paper[fold[1]+d-1][i]

    paper = paper[:fold[1]]

  return paper

def part1(coordinates, folds):

  max_x = max([c[0] for c in coordinates])
  max_y = max([c[1] for c in coordinates])
  paper = [[['.'] for x in range(max_x+1)] for y in range(max_y+1)]
  
  for c in coordinates:
    paper[c[1]][c[0]] = ["#"]

  # print_paper(paper)
  for fold in folds:
    paper = make_fold(paper, fold)
  print_paper(paper)

  return count_dots(paper)


if __name__ == "__main__":

  coordinates , folds = read_input()
  # print(coordinates, folds)

  res1 = part1(coordinates, folds[:1])
  print(res1)

  res1 = part1(coordinates, folds)