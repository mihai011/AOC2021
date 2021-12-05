with open("input.txt") as f:
  data = f.read().split("\n")

gamma = ''
epsilon = ''

for i in range(len(data[0])):
  stats = {'1':0, '0':0}
  for b in data:
    stats[b[i]] +=1
  stats= {v:k for k,v in stats.items()}
  gamma += stats[max(list(stats.keys()))]
  epsilon += stats[min(list(stats.keys()))]


gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

print(gamma * epsilon)

co2 = data
oxy = data

for i in range(len(data[0])):

  stats_co2 = {'1':0, '0':0}
  new_co2_1 = []
  new_co2_0 = []

  if len(co2) > 1:
    for b in co2:
      stats_co2[b[i]] += 1
      if b[i] == '0':
        new_co2_0.append(b)
      else:
        new_co2_1.append(b)
    if stats_co2['0'] == stats_co2['1']:
      co2 = new_co2_0
      continue
    stats = {v:k for k,v in stats_co2.items()}
    if stats[min(list(stats.keys()))] == '1':
      co2 = new_co2_1
    else:
      co2 = new_co2_0
  else:
    break

for i in range(len(data[0])):

  stats_oxy = {'1':0, '0':0}
  new_oxy_1 = []
  new_oxy_0 = []

  if len(oxy) > 1:
    for b in oxy:
      stats_oxy[b[i]] += 1
      if b[i] == '0':
        new_oxy_0.append(b)
      else:
        new_oxy_1.append(b)
    if stats_oxy['0'] == stats_oxy['1']:
      oxy = new_oxy_1
      continue
    stats = {v:k for k,v in stats_oxy.items()}
    if stats[max(list(stats.keys()))] == '1':
      oxy = new_oxy_1
    else:
      oxy = new_oxy_0
  else:
    break
  


co2 = int(co2[0], 2)
oxy = int(oxy[0], 2)

print(co2 * oxy)


  
    
