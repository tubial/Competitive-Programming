cals = []
cur = 0

with open("./data/input2022day1.txt") as f:
    for line in f:
        if line.strip() != "":
            cur += int(line)
        else:
            cals.append(cur)
            cur = 0
          

print(sum(sorted(cals, reverse=True)[0:3]))
