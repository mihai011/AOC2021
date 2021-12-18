from tqdm import tqdm

def impact(i, j, x, y):

  initial = [0,0]
  max_y = initial[1]
  while True:
    
    initial[0] += j
    initial[1] += i

    if max_y < initial[1]:
      max_y = initial[1]

    if initial[0] <= x[1] and initial[0] >= x[0] and \
      initial[1] <= y[1] and initial[1] >= y[0]:
      return max_y

    i -= 1

    if j > 0 : 
      j -= 1
    elif j < 0:
      j += 1

    if initial[1] <= y[0]:
      return -1



def calculate(x, y):

  strikes = set()
  max_y = - 1
  for i in tqdm(range(-200, 200)):
    for j in range(-200, 200):
      alt = impact(i, j, x, y)
      if alt != -1 and alt > max_y:
        max_y = alt
      if alt != -1:
        strikes.add((i, j))

  return strikes, max_y

if __name__ == "__main__":
  x = [81, 129]
  y = [-150, -108]

  strikes, max_y = calculate(x, y)
  print(max_y)
  print(len(strikes))