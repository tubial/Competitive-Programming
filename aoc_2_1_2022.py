scores = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

cur = 0
total = 0

with open("./data/input2022day2.txt") as f:
    for line in f:
        them, us = line.strip().split(" ")

        # win
        if them == "A" and us == ""
        