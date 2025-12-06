# 2025-6
### part 1
# N is 1000
# i suppose a 2d array wouldnt be too bad ...

with open("2025-6-input.txt", 'r') as f:
    total = 0
    matrix = []

    # first load into array
    lines = f.readlines()
    for line in lines:
        matrix.append(line.split())

    for i in range(len(matrix[-1])):
        op = matrix[-1][i]
        total_value = int(matrix[0][i])

        for row in matrix[1:-1]:
            val = int(row[i])
            
            if op == '*':
                total_value *= val
            else:
                total_value += val
        total += total_value
    print("Total:", total)

## part 2
# N= 3685 (chars in string) which is still workable
import math 

with open("2025-6-input.txt", 'r') as f:
    total = 0
    matrix = []

    lines = f.readlines()
    for line in lines:
        matrix.append(line)
    
    #gonan loop through all chars in the string backwards

    buffer = []
    for i in range(len(matrix[-1]) -1, -1, -1):
        # forgive me for repetition, tired
        op = matrix[-1][i]
        if op == '*':
            constructed_num = ''
            for row in matrix[:-1]:
                constructed_num += row[i]
            buffer.append(int(constructed_num))

            print(buffer)
            total += math.prod(buffer) 
            buffer = []
        elif op == '+':
            constructed_num = ''
            for row in matrix[:-1]:
                constructed_num += row[i]
            buffer.append(int(constructed_num))

            print(buffer)
            total += sum(buffer)
            buffer = []
        else: # blank
            constructed_num = ''
            for row in matrix[:-1]:
                constructed_num += row[i]
            try:    
                buffer.append(int(constructed_num))
            except:
                continue

    print("Total:", total)
