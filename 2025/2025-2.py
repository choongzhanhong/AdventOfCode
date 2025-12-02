# 2025-2

### Part 1
# repeated twice so even number id's only

invalids = 0

def get_invalid_ids(id1, id2):
    # returns array of invalid ides within the [id1, id2] 
    invalid_ids = []
    for current_id in range(int(id1), int(id2) + 1):
        if is_invalid_part2(str(current_id)):
            invalid_ids.append(current_id)

    return invalid_ids 

def is_invalid(in_id):
    # expects string, return True or False

    id_length = len(in_id)

    # odd
    if (id_length % 2 == 1):
        return False 
    
    if (int(in_id[:id_length//2]) == int(in_id[id_length//2:])): 
        return True

    return False
    
## part 2
def is_invalid_part2(in_id):
    # at last twice now
    # expect string, return bool
    # using buffer method is costly, try math
    # number of repeats ranges from 2 to len(in_id)
    # aka if len is 6, you have example 123123, 121212, 111111
    # notice how these are all factors of len
    # hopefully this reduces the time complexity by a bit xdxdxdxd
    # print("=== Testing id:", in_id)

    for factor in find_all_factors(in_id):
        # e.g. factor is 3, for 101010 (len 6), snippet is 10 (len 6//3 = 2)
        #       range through [:2], [2:4], [4:6]
        # keep track if the snippets so far are similar
        has_invalid = True 
        part = len(in_id) // factor
        snippet = in_id[:part]
        # print("Snippet:", snippet)

        for i in range(1, factor): 
            if (in_id[i * part : (i + 1) * part] != snippet): 
                has_invalid = False
                break 
                    
        if has_invalid:
            return True

    return False 

def find_all_factors(in_id):
    # aside from 1, but inclusive of len itself
    return [i for i in range(2, len(in_id) + 1) if len(in_id)%i == 0]

with open("2025-2-input.txt", 'r') as f:
    ids = f.readlines()[0].split(',')
    # it's id1-id2 ranges
    # aka 2 ids in one range
    for id_range in ids:
        id1, id2 = id_range.split('-')
        # print("id pair:", id1, id2)
        for invalid_id in get_invalid_ids(id1, id2):
            invalids += invalid_id

print("Sum of invalid IDs:", invalids)

