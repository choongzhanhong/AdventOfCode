# 2025-11
import time
start_time = time.time()

def get_edges(u_in, edges):
    return [v for u,v in edges if u == u_in]

def dfs(to_visit, edges):
    # base case: to_visit is empty
    if not to_visit: 
        return 0

    output = 0

    for u in to_visit:
        if (u == "out"):
            # for this u, there is one out
            output += 1
        else:
            output += dfs(get_edges(u, edges), edges)

    return output

MEMO = {}

def dfs_2(to_visit, edges, dac=False, fft=False, path=[], curr_vertex="", target="out"):
    if curr_vertex in MEMO:
        return MEMO[curr_vertex]

    # base case: to_visit is empty
    if not to_visit: 
        return 0

    output = 0

    for u in to_visit:
        if (u == target):
            # for this u, there is one out
            if dac and fft:
                print("no", path)
            output += 1
        else:
            curr_path = path[:]
            curr_path.append(u)

            dac_now = u == "dac" or dac
            fft_now = u == "fft" or fft

            output += dfs_2(get_edges(u, edges), edges, dac_now, fft_now, curr_path, curr_vertex=u, target=target)
            MEMO[curr_vertex] = output

    # print(f"Time elapsed: {time.time() - start_time:.6f}s", end='\r', flush=True)
    # print("Output so far:", output, end='\r', flush=True)
    return output

with open("2025-11-input.txt", 'r') as f:
    # edges are in one direction only (u,v) -> u to v
    edges = []
    lines = f.readlines()
    
    for line in lines:
        inputs = line.strip().split()
        u = inputs[0][:-1]
        
        for v in inputs[1:]:
            edges.append((u,v))

    ## dfs
    to_visit = get_edges("you", edges) 

    print(dfs(to_visit, edges))
    

with open("2025-11-input.txt", 'r') as f:
    print("Started test case 2")
    edges = []
    lines = f.readlines()

    for line in lines:
        inputs = line.strip().split()
        u = inputs[0][:-1]

        for v in inputs[1:]:
            edges.append((u,v))

    MEMO = {}
    to_visit_1 = get_edges("svr", edges)
    print('svr to out:', dfs_2(to_visit_1, edges, path=["svr"], curr_vertex="svr", target="out"))

    MEMO = {}
    to_visit_2 = get_edges("dac", edges)
    print('dac to fft:', dfs_2(to_visit_2, edges, path=["dac"], curr_vertex="dac", target="fft"))

    MEMO = {}
    to_visit_3 = get_edges("fft", edges)
    print('fft to dac:', dfs_2(to_visit_3, edges, path=["fft"], curr_vertex="fft", target="dac"))

    MEMO = {}
    to_visit_4 = get_edges("svr", edges)
    print('svr to fft:', dfs_2(to_visit_4, edges, path=["svr"], curr_vertex="svr", target="fft"))

    MEMO = {}
    to_visit_5 = get_edges("dac", edges)
    print('dac to out', dfs_2(to_visit_5, edges, path=["dac"], curr_vertex="dac", target="out"))

    
