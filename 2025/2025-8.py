# 2025-8
### part 1
# 1000 junction boxes, n^2 is 1 mil... is that ok?

import math 

#thx gemini
class UnionFind:
    def __init__(self, n):
        # parent[i] stores the parent of element i. 
        self.parent = list(range(n))
        
        # size[i] stores the size of the set ONLY if i is the root.
        self.size = [1] * n
        self.n = n

    def find(self, i):
        """
        Finds the representative (root) of the set containing element i,
        using Path Compression.
        """
        if self.parent[i] == i:
            return i
        
        # Path Compression
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        """
        Unites the sets containing elements i and j, using Union by Size.
        """
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            # Union by Size: Attach smaller tree to the root of the larger tree.
            if self.size[root_i] < self.size[root_j]:
                root_i, root_j = root_j, root_i  # Swap 
            
            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]
            return True
        return False

    def get_set_size(self, i):
        """
        Returns the size of the set containing element i.
        """
        root = self.find(i)
        return self.size[root]

    def get_all_set_sizes(self):
        """
        Returns a list of the sizes of all disjoint sets, 
        sorted from largest to smallest.
        
        Returns:
            list[int]: The list of all unique set sizes.
        """
        set_sizes = []
        # Iterate through all elements 0 to n-1
        for i in range(self.n):
            # Check if 'i' is the root of its set
            if self.parent[i] == i:
                # If it's a root, its 'size' entry holds the true set size
                set_sizes.append(self.size[i])
        
        # Sort the sizes in descending order (largest to smallest)
        return sorted(set_sizes, reverse=True)

def distance(v1, v2):
    return math.sqrt((v1[0] - v2[0])**2 + (v1[1] - v2[1])**2 + (v1[2] - v2[2])**2)

with open("2025-8-input.txt", 'r') as f:
    vectors = []
    pairs = []

    # first load into array
    lines = f.readlines()
    for line in lines:
        vec = line.strip().split(',')
        vec = [int(i) for i in vec]
        vectors.append(tuple(vec))

    # v1, v2, distance
    for i in range(len(vectors)):
        for j in range(len(vectors)):
            if i != j:
                # store indexes to use in unionfind
                # prevent (i, j) and (j, i) duplication
                if i < j:
                    pairs.append((i, j, distance(vectors[i], vectors[j])))

    pairs.sort(key=lambda pair:pair[2]) #sort by distance

    UF = UnionFind(len(vectors))

    # i = 0
    # N = 1000
    # for pair in pairs:
    #     print("Unioning:", vectors[pair[0]], vectors[pair[1]])
        
    #     # if (UF.find(pair[0]) == UF.find(pair[1])): continue # no change

    #     UF.union(pair[0], pair[1])

    #     i += 1
    #     if i == N: break

    for pair in pairs:
        UF.union(pair[0], pair[1])

        total_sets = len(UF.get_all_set_sizes())
        if total_sets == 1:
            print(vectors[pair[0]][0] * vectors[pair[1]][0])
            break

    print(UF.get_all_set_sizes())
    print("Product of top 3 sets:", math.prod(UF.get_all_set_sizes()[:3]))