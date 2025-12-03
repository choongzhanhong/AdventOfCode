# 2025-3

### Part 1
# repeated twice so even number id's only

sum_joltage = 0

def get_joltage(bank):
    # expect str, return int
    # pseudo queue
    i1 = -1
    i2 = -1
    
    for bat in bank[:-1]: # ignore newline
        val = int(bat)

        # at the start of every loop, you get a new "bat" value to test against existing bat vals
        # if i2 > i1 at the start, that means there exists a value after i2, and it can shift up
        # and any value that comes after is a suitable candidate for i2
        if i2 > i1:
            i1 = i2
            i2 = val
            continue
        
        # if i2 not greater, then i1 remains the same but still test for val > i2
        if val > i2:
            i2 = val

    result = int(f'{i1}{i2}')
    print(i1, "+", i2, "=", result)
    return result 

### part 2
# 12 digits means you get a queue of size 12 instead

def shift_left(array):
    # print(array)
    # test all indices to their left
    out = [-1 for i in range(13)]

    for i in range(len(array) - 1):
        # if current place is higher than left place
        if array[i + 1] > array[i]:
            out[i] = array[i + 1]
            if (i + 2 >= len(array)):
                array[i + 1] = -1
            else:
                array[i + 1] = array[i + 2]
                array[i + 2] = -1
        else:
            out[i] = array[i]
    # print(out[:12])
    # print("===")
    return out[:12] # cut out last one

def get_joltage_part2(bank):
    # expect str, return int
    
    bat_queue = [-1 for i in range(12)]
    for bat in bank[:-1]:
        val = int(bat)
        bat_queue.append(val)
        bat_queue = shift_left(bat_queue)
    # bat_queue is an array of ints
    out = [str(val) for val in bat_queue]
    print(''.join(out))
    return int(''.join(out))

with open("2025-3-input.txt", 'r') as f:
    
    banks = f.readlines()
    for bank in banks:
        
        sum_joltage += get_joltage_part2(bank)

print("Sum of max joltage:", sum_joltage)

