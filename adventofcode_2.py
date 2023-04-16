with open('./data/inputday2.txt') as f:
    directions = [line.strip().split(" ") for line in f]

x = 0
depth = 0
aim = 0

for direction in directions:
    match direction[0]:
        case "forward":
            x += int(direction[1])
            depth += aim * int(direction[1])
        case "down":
            aim += int(direction[1])
        case "up":
            aim -= int(direction[1])

print(depth * x)