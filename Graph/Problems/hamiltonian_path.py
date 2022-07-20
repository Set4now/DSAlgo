"""

A Hamiltonian path, is a path in an undirected or directed graph that visits each vertex exactly once. Given an undirected graph  the task is to check if a Hamiltonian path is present in it or not.

https://practice.geeksforgeeks.org/problems/hamiltonian-path2522/1

Input:
    N = 4, M = 4
    Edges[][]= { {1,2}, {2,3}, {3,4}, {2,4} }
    Output:
    1 
    Explanation: 
    There is a hamiltonian path: 
    1 -> 2 -> 3 -> 4 
"""


class Solution:

    def dfs(self, node, path, nodelist, adj_edge_list, visited):
        if not visited[node]:
            visited[node] = True
            path.append(node)
           
        if len(path) == len(nodelist):
            print(path)
            return True
        for edge in adj_edge_list[node]:
            if not visited[edge]:
                if not self.dfs(edge, path, nodelist, adj_edge_list, visited):
                    visited[edge] = False
                    path.pop() 
                else:
                    return True
        return False

    def check(self, N, M, Edges):
        adj_edge_list = {}
        adj_edge_list2 = {}
        start = ''
        # start1 = ''
        nodes = set()
        for edges in Edges:
            node1 = edges[0]
            node2 = edges[1]
            if start == "":
                start = node1
            nodes.add(node1)
            nodes.add(node2)
            
            if node1 not in adj_edge_list:
                adj_edge_list[node1] = [node2]
            else:
                adj_edge_list[node1].append(node2)
            if node2 not in adj_edge_list2:
                adj_edge_list2[node2] = [node1]
            else:
                adj_edge_list2[node2].append(node1)

        # print(adj_edge_list)
        # print(adj_edge_list2)

        from copy import deepcopy
        new = deepcopy(adj_edge_list)
        for k in adj_edge_list:
            if k in adj_edge_list2:
                new[k].extend(adj_edge_list2[k])
        for j in adj_edge_list2:
            if j not in adj_edge_list:
                new[j] = adj_edge_list2[j]
        

        print(new)

        for vertex in new:
            visited = {node: False for node in nodes}
            path = []
            if self.dfs(vertex, path, nodes, new, visited):
                return True
        
        return False

# edges =  [[1,2], [2,3], [3,4], [2,4]]
# N = 4
# M = 4

# edges = [[1,2], [2,3], [2,4]]
# N = 4
# M = 3

edges = [[2, 1], [10, 2], [6, 3], [5, 4], [10, 5], [10, 6], [6, 7], [6, 8], [10, 9], [4, 9], [3, 8], [3, 7], [5, 9], [6, 5]]
N = 10
M = 14

s = Solution()
print(s.check(N, M, edges))







