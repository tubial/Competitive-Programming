from typing import List

# 3
# 10 3 3
# 2 7 9
# 10 2 3
# 2 7 9
# 10 2 4
# 2 3 7 9


def illuminate(highway: List, bulb_locations: List[int], radius: int) -> bool:
    for bulb_loc in bulb_locations:
        if bulb_loc - radius < 0 and bulb_loc + radius > len(highway) + 1:
            # Radius of one bulb is bigger than the whole highway
            return [True for _ in range(len(highway))]
        elif bulb_loc - radius < 0:
            pass


for case_num in range(int(input())):
    highway_length, radius, num_bulbs = (int(num) for num in input().strip().split(" "))

    highway = [False for i in range(highway_length)]

    bulb_locations = [int(num) for num in input().strip().split(" ")]
