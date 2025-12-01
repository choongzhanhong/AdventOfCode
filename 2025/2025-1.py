# 2025-1

### Part 1
# basically modulo 100

dial = 50
num_zero = 0

with open("2025-1-input.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        direction = line[0]
        number = int(line[1:])
        if (direction == "L"):
            dial = (dial - number) % 100
        else:
            dial = (dial + number) % 100

        if (dial == 0):
            num_zero += 1

print("Num of zero:", num_zero)

### Part 2
# if number is greater than 100:
#   divide it by 100 and subtract the quotient?
# e.g. 50 - 168 = goes through zero twice
#   50 - 100 - 68  

dial = 50
num_zero = 0
with open("2025-1-input.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        direction = line[0]
        number = int(line[1:])
        
        quotient = number // 100
        remainder = number % 100

        if (direction == "L"):
            final_dial = (dial - remainder)
        else:
            final_dial = (dial + remainder)

        # check if the result is the same
        # when starting from dial = 0, do not bother checking

        prev_dial = dial
        dial = final_dial % 100
        if (dial == 0 or (dial != final_dial and prev_dial != 0)):
            num_zero += 1
        
        num_zero += quotient

print("Num of zero clicks:", num_zero)

