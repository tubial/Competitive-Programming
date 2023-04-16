max = 0
cur = 0
times_reset = 0

with open("./data/input2022day1.txt") as f:
    for line in f:
        if line.strip() != "":
            cur += int(line)
        else:
            if cur > max:
                max = cur
            cur = 0
            times_reset += 1

print(max)
print(times_reset)