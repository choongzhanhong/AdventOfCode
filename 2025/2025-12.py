## 2025-12

with open("2025-12-input.txt", 'r') as f:
    lines = f.readlines()
    shapes = []

    ## hard code the shape getting
    # index 1-3, 6-8
    for i in range(6):
        shape_rows = lines[i*5 + 1: i*5 +4]
        print(shape_rows)
        shape_area = 0
        for row in shape_rows:
            for i in row:
                if i == '#': shape_area += 1
        shapes.append(shape_area)

    print(shapes)

    num_able_to_fill = 0

    for line in lines[30:]:
        nums = line.split(':')[0].split('x')
        # area to fill
        amt = int(nums[0]) * int(nums[1])

        values = line.split(':')[1].split()

        # area of shapes
        total_area = 0
        for i, num in enumerate(values):
            # assume every shape just takes up a 3x3 space
            # with no overlap
            total_area += 9 * int(num)


        print(f"{amt} area with {total_area} presents")
        
        if amt >= total_area: num_able_to_fill += 1 

    print(num_able_to_fill)

        
