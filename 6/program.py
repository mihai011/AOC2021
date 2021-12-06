
def read_input():

  with open("input.txt") as f:
    data = [int(d) for d in f.read().split(",")]

  return data


def part1(fish, days):

  for d in range(days):

    new_fish = []
    for i in range(len(fish)):

      if fish[i] == 0:
        fish[i] = 6
        new_fish.append(8)
      else:
        fish[i] -= 1
    
    fish = fish + new_fish
    
  return len(fish)

def iterate_one_day(fish):

  fish[9] = fish[0]
  fish[7] += fish[0]
  for i in range(1, len(fish)):
      fish[i-1] = fish[i]
  fish[9] = 0
  return fish

def part2(fish, days):

  fish = [fish.count(i) for i in range(10)]
  for i in range(days):
    fish = iterate_one_day(fish)

  return sum(fish)

if __name__ == "__main__":

  input = read_input()
  res1 = part1(input, 80) 
  print(res1)
  res2 = part2(input, 255) 
  print(res2)
  
