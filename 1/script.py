with open("input.txt") as f:
    data = [int (e) for e  in f.read().split()]


increased = 0

for i in range(1,len(data)):
    if data[i-1] < data[i]:
        increased += 1

print(increased)

incresed_3 = 0
for i in range(3, len(data)):
    # print(data[i-3:i],data[i-2:i+1] )
    print(data[i])
    if sum(data[i-3:i]) < sum(data[i-2:i+1]):
        incresed_3 += 1

print(incresed_3)        

