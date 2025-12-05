# 2025-5
### part 1

# N inputs
# k number of ranges (which is smaller than N)
# can just brute force

with open("2025-5-input.txt", 'r') as f:
    num_fresh = 0

    # first load into array
    ranges = [] # pair tuples
    inputs = []
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if '-' in line:
            pair = line.split('-')
            ranges.append((int(pair[0]), int(pair[1])))
        elif line:
            inputs.append(int(line))

    # start
    for val in inputs:
        for pair in ranges:
            if pair[0] <= val and val <= pair[1]:
                num_fresh += 1
                break

    print("Num of fresh:", num_fresh)

print("====== part 2======")
### part 2
# quite different 
with open("2025-5-input.txt", 'r') as f:
    num_fresh = 0

    # first load into array
    ranges = [] # pair tuples
    for line in lines:
        line = line.strip()
        if '-' in line:
            pair = line.split('-')
            ranges.append((int(pair[0]), int(pair[1])))
    
    # sort by left item, lower bound of range
    ranges_sorted = sorted(ranges, key = lambda item: item[0])

    for i in range(len(ranges_sorted)):
        # first range by definition has all the numbers
        if (i == 0):
            num_fresh += ranges_sorted[i][1] - ranges_sorted[i][0] + 1
            print(f"Adding from: [{ranges_sorted[i][0]}, {ranges_sorted[i][1]}]")
        else:
            # not first range
            # check if overlap with previous range
            start_range = ranges_sorted[i][0] 
            end_range = ranges_sorted[i][1]
            print(f"Checking ({start_range}, {end_range})")

            if end_range <= ranges_sorted[i - 1][1]:
                # dont bother, start is greater than the previous start (by definition)
                # but end is less than previous end, means this range is already included
                # by the previous range 
                
                # adopt the previous tuple
                ranges_sorted[i] = (start_range, ranges_sorted[i - 1][1])
                print(f"changed to {ranges_sorted[i]}")
                print("---") 

                continue

            if start_range <= ranges_sorted[i - 1][1]:
                start_range = ranges_sorted[i - 1][1] + 1
                num_fresh += end_range - start_range + 1
                print(f"if Adding from: [{start_range}, {end_range}]")

            else:
                num_fresh += end_range - start_range + 1  
                print(f"else Adding from: [{start_range}, {end_range}]")
        print("---") 
    
    print("Num of fresh (part 2):", num_fresh)
