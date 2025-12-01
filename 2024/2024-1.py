# 2024-1

### Part 1

left_nums, right_nums = [], []

with open("2024-1-input.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        numbers = line.split()
        left, right = int(numbers[0]), int(numbers[1]),
        left_nums.append(left)
        right_nums.append(right)

left_nums.sort()
right_nums.sort()

total_dist = 0

for i in range(len(left_nums)):
    total_dist += abs(left_nums[i] - right_nums[i])

print(total_dist)

### Part 2 
# right list keeps track of occurrences

right_dict = {}

total_dist = 0

for num in right_nums:
    if num not in right_dict:
        right_dict[num] = 1
    else:
        right_dict[num] += 1

for num in left_nums:
    if num not in right_dict:
        continue
    total_dist += num * right_dict[num]

print(total_dist)
