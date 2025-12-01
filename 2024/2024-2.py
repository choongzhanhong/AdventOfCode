# 2024-2
### part 1

num_safe = 0

with open("2024-2-input.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        
        num_array = [int(num) for num in line.split()]
        print(num_array)
        # first pair decides if direction should be positive or negative
        direction = 0
        is_line_safe = True
        
        for i in range(len(num_array) - 1):
            diff = num_array[i + 1] - num_array[i]
            if (diff > 0):
                curr_direction = 1
            elif (diff < 0):
                curr_direction = -1
            else:
                curr_direction = 0
            
            # this only happens on first loop, because we exit if there's no change
            if (direction == 0): 
                direction = curr_direction
            
            if (curr_direction != direction or curr_direction == 0):
                is_line_safe = False
            
            if abs(diff) > 3:
                is_line_safe = False
            
        if is_line_safe:
            num_safe += 1    
       
print(num_safe)