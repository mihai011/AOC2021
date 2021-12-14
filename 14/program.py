from collections import defaultdict

def read_input():

  with open("input.txt") as f:
    data = f.read()

  pol = data.split("\n\n")[0]
  trans = data.split("\n\n")[1]

  trans = {t.split("->")[0].strip(): t.split("->")[1].strip() for t in trans.split("\n")}

  return pol, trans

def part2(pol, trans):

  g_count = defaultdict(int)
  for i in range(len(pol)-1):
    g_count[pol[i:i+2]] += 1

  c_count = defaultdict(int)
  for p in pol:
    c_count[p] += 1

  for _ in range(40):
    new_g_count = []
    for k, v in g_count.items():

      if k in trans:
        c = trans[k]
        new_g_count.append((k[0]+c, v))
        new_g_count.append((c+k[1], v))
        c_count[c] += v
    
    g_count = defaultdict(int)
    for k, v in new_g_count:
      g_count[k] += v
    
  return max(c_count.values())-min(c_count.values())


def part1(pol, trans):

  for _ in range(10):

    i = 0
    while i < len(pol)-1:
      if pol[i:i+2] in trans:
        pol = pol[:i+1] + trans[pol[i:i+2]] + pol[i+1:]
        i += 2
      else:
        i += 1

    counts = defaultdict(int)
    for p in pol:
      counts[p] += 1

  return max(counts.values())-min(counts.values())
  
if __name__ == "__main__":
  
  pol, trans = read_input()

  res1 = part1(pol, trans)
  print(res1)

  res1 = part2(pol, trans)
  print(res1)