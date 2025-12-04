# 2025-4
### Part 1

def num_adjacent(matrix, i, j):
    # in: matrix, row, col
    # out: num of adjacent '@'
    num = 0
    
    # search thru all 9
    for u in range(-1, 2):
        for v in range(-1, 2):
            if u == 0 and v == 0: 
                continue
            
            # avoid accessing wrap around index
            if (i + u < 0) or (j + v < 0):
                continue
            
            # avoid indexerror
            try:
                get_item = matrix[i + u][j + v]
            except:
                get_item = False

            if not get_item:
                continue
                
            if get_item == '@':
                num += 1
    # print(f"({i}, {j}): {matrix[i][j]} has {num} @ adjacent")
    return num

with open("2025-4-input.txt", 'r') as f:
    num_rolls = 0
    
    rows = f.readlines()
    matrix = []
    for row in rows:
        matrix.append(list(row[:-1])) # remove newline
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            
            num_of_at = num_adjacent(matrix, i, j)
            if num_of_at < 4 and matrix[i][j] == '@':

                num_rolls += 1

    print("Num rolls:", num_rolls)
    num_rolls_part2 = 0
    ### part 2 stuff
    while(True):
        num_to_add = 0
        temp_matrix = matrix[:]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                num_of_at = num_adjacent(matrix, i, j)
                if num_of_at < 4 and matrix[i][j] == '@':
                    num_to_add += 1
                    temp_matrix[i][j] = 'X'

        num_rolls_part2 += num_to_add
        matrix = temp_matrix
        if num_to_add == 0:
            break

    print("Num rolls part 2:", num_rolls_part2)
    

