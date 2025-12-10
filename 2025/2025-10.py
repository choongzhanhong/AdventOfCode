# 2025-10
from itertools import chain, combinations

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

def result_of_buttons(button_set, length):
    empty = [0 for i in range(length)]
    for buttons in button_set:
        for index in buttons:
            empty[index] += 1

    return empty 

def is_subtractable(array1, array2):
    # input: 2 arrays of integers [x1, x2, ...] and [y1, y2, ...]
    # returns true if for all i, xi-y1 >= 0 
    for i in range(len(array1)):
        if array1[i] - array2[i] < 0: return False

    return True

def subtractable_how_many(array1, array2):
    # assumes inputs are subtractable
    # eg 3,2,2 - 1,1,1 => 2 times (result is 1,0,0)
    # works
    
    n = 999
    for i in range(len(array1)):
        if array2[i] != 0:
            n = min(n, array1[i]//array2[i])

    return n

def subtract_arrays(array1, array2, n = 1):
    # array1 - n(array2)
    temp = array1[:]
    for i in range(len(temp)):
        temp[i] = array1[i] - array2[i]*n

    return temp

def is_all_zero(array):
    for i in array:
        if i > 0: return False
    return True

def less_than_zero(array):
    for i in array:
        if i < 0: return True
    return False

def button_result(button, length):
    temp = [0 for i in range(length)]
    for i in button:
        temp[i] += 1
    
    return temp
### Should be a coin combination problem
memo = {}

def min_button_press(array, available_buttons):

    # success base case
    if is_all_zero(array):
        return 0
    
    # failure case
    if less_than_zero(array):
        return float('inf')

    min_count = float('inf')

    for button in available_buttons:
        result = min_button_press(subtract_arrays(array, button_result(button, len(array))), available_buttons)
        if result != float('inf'):
            min_count = min(min_count, result + 1)
    
    return min_count

with open("2025-10-test.txt", 'r') as f:
    machines = []
    buttons = []
    ### part 2
    joltages = []
    total = 0

    lines = f.readlines()
    for line in lines:
        buttons_line = []
        for group in line.strip().split():
            if group[0] == '[':
                machines.append([0 if char == '.' else 1 for char in group[1:-1]]) 
            elif group[0] == '(':
                buttons_line.append([int(i) for i in group[1:-1].split(',')])

            # part 2
            elif group[0] == '{':
                joltages.append([int(i) for i in group[1:-1].split(',')]) 

        buttons.append(buttons_line)

    # seems to work
    # powerset is ok because each button is pressed 1 time max 
    for i in range(len(machines)):
        mins = 999
        powerbuttons = powerset(buttons[i])
        for buttons_set in powerbuttons:
            empty = [0 for i in machines[i]]
            for button in buttons_set:
                for index in button:
                    empty[index] = 1 if empty[index] == 0 else 0
            
            if empty == machines[i]:
                # print("Works:", buttons_set)
                mins = min(mins, len(buttons_set))

        total += mins
    print("total button presses:", total)

    total_pt2 = 0
   
    ### part 2
    for i in range(len(joltages)):
        print(f"Checking {joltages[i]}: {buttons[i]}")
        min_num_press = 999

        minimum = min_button_press(joltages[i], buttons[i])

        total_pt2 += min_num_press 
        print("========")

    print("total part 2:", total_pt2)





    # for i in range(len(joltages)):
    #     print(f"Checking {joltages[i]}")
    #     min_num_press = 999
    #     powerbuttons = powerset(buttons[i])
    #     # num button presses + result of pressing buttons in each set
    #     results_set = [] 
    #     for buttons_set in powerbuttons:
    #         resultant = result_of_buttons(buttons_set, len(joltages[i]))
    #         # num button press, resultant value
    #         results_set.append( (len(buttons_set), resultant) )

    #     results_set.pop(0) #remove the empty set result
    #     for result in results_set:
    #         print(result)

    #     # TODO: need to trim result set?
    #     # some button presses result in the same value but different number of presses

    #     # check combinations
    #     # if the set of button presses results in non-zero, it isn't part of the set
    #     while results_set:
    #         temp = joltages[i][:]
    #         subset_results = []

    #         num_presses = 0
    #         for presses, result in results_set:

    #             if (is_subtractable(temp, result)):
    #                 n = subtractable_how_many(temp, result)
    #                 temp = subtract_arrays(temp, result, n)
    #                 num_presses += n*presses

    #                 subset_results.append((presses, result))

    #             # after subtracting
    #             if is_all_zero(temp):
    #                 min_num_press = min(min_num_press, num_presses)
    #                 print(subset_results, "and", num_presses)
    #                 break
    #         results_set.pop(0)

    #     total_pt2 += min_num_press
    #     print("=====")
    #     break
    
    # print("total part 2:", total_pt2)
