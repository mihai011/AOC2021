with open("input.txt") as f:
    data = f.read().split("\n")

depth, distance = 0,0

for ins in data:

    mov = ins.split(" ")[0]
    space = ins.split(" ")[1]

    if mov == "forward":
        distance += int(space)
    
    if mov == "up":
        depth -= int(space)

    if mov == "down":
        depth += int(space)

print(depth*distance)


depth, distance, aim = 0,0,0

for ins in data:

    mov = ins.split(" ")[0]
    space = ins.split(" ")[1]

    if mov == "forward":
        distance += int(space)
        depth += int(space) * aim
        
    if mov == "up":
        aim -= int(space)

    if mov == "down":
        aim += int(space)

print(depth*distance)
    

