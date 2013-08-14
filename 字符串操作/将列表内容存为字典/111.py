v_list = [[123, 4], [123, 5], [123, 6], [345, 29], [345, 78]]

n_map = {}
for i, j in v_list:
    print i,j
    if n_map.has_key(i):
        n_map[i].append(j)
    else:
        n_map[i] = [j]

