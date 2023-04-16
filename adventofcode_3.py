import time

t_0 = time.time()

def b_to_i(binary_num: list) -> int:
    total = 0

    for i in range(len(binary_num)):
        if binary_num[len(binary_num) - 1 - i] == 1:
            total += 2 ** i
    return total


with open("./data/inputday3.txt") as f:
    nums = [line.strip() + "1" for line in f]

gamma = [0] * len(nums[0])
sigma = [0] * len(nums[0])

for num in nums:
    for i in range(len(num)):
        gamma[i] += 1 if num[i] == "1" else 0

for i in range(len(gamma)-1):
    gamma[i] = 1 if gamma[i] > len(nums) - gamma[i] else 0
    sigma[i] = 0 if gamma[i] == 1 else 1

print(b_to_i(gamma[:-1]) * b_to_i(sigma[:-1]))



for i in range(len(nums[0])-1):
    count_i = sum([int(num[i]) for num in nums if int(num[-1]) == 1])
    total_i = len([num for num in nums if int(num[-1]) == 1])

    print(count_i, total_i)
    print(count_i/total_i)

    for j in range(len(nums)):
        # if valid
        if nums[j][-1] == '1':
            # if num at index is 1 and there are fewer 1s, don't keep
            if nums[j][i] == '1' and count_i / total_i < 0.5:
                nums[j] = nums[j][:-1] + "0"
            # if num at index is 0 and there are fewer 0s, don't keep
            elif nums[j][i] == '0' and count_i / total_i >= 0.5:
                nums[j] = nums[j][:-1] + "0"