from copy import deepcopy


adj_edge_list = {2: [1], 10: [2, 5, 6, 9], 6: [3, 7, 8, 5], 5: [4, 9], 4: [9], 3: [8, 7]}
adj_edge_list2 = {1: [2], 2: [10], 3: [6], 4: [5], 5: [10, 6], 6: [10], 7: [6, 3], 8: [6, 3], 9: [10, 4, 5]}


# adj_edge_list = {6: [3, 7, 8, 5]}
# adj_edge_list2 = {6: [10]}

from copy import deepcopy
new = deepcopy(adj_edge_list)
for k in adj_edge_list:
    if k in adj_edge_list2:
        new[k].extend(adj_edge_list2[k])
for j in adj_edge_list2:
    if j not in adj_edge_list:
        new[j] = adj_edge_list2[j]

print(new) 