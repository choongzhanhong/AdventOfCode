# 2025-7
### part 1
# length of line is 15 so n^2 could be possible

with open("2025-7-input.txt", 'r') as f:
    num_split = 0
    
    ### part 2
    particles = []
    num_timelines = 1

    matrix = []

    # first load into array
    lines = f.readlines()
    for line in lines:
        matrix.append(line.strip())

    # indexes where a tachyon beam exists
    indices = {i for i in range(len(matrix[0])) if matrix[0][i] == 'S'}
    
    for line in matrix[1:]:
        new_indices = indices.copy() 
        for index in indices:
            if line[index] == '^':
                new_indices.remove(index)
                if (index - 1 >= 0): new_indices.add(index - 1)
                if (index + 1 < len(line)): new_indices.add(index + 1)
                num_split += 1

        indices = new_indices 

    # part 2
    # part 2 stuff
    # matrix[row][i] will have a count of particles in index i
    particles = [1 if i == 'S' else 0 for i in matrix[0]]
    for line in matrix[1:]:
        new_particles = particles[:]
        for i in range(len(particles)):
            if line[i] == '^' and particles[i] > 0:
                # transfer them to adjacent
                if (i - 1 >= 0): new_particles[i - 1] = new_particles[i - 1] + particles[i]
                if (i + 1 < len(particles)): new_particles[i + 1] = new_particles[i + 1] + particles[i]
                new_particles[i] = 0

        particles = new_particles 

    num_timelines = sum(particles)
        
    print("Num split:", num_split)
    print("Num timelines:", num_timelines)
