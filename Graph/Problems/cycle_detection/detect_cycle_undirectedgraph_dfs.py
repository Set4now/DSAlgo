# https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1
"""
Input:  
    V = 5, E = 5
    adj = {{1}, {0, 2, 4}, {1, 3}, {2, 4}, {1, 3}} 
    Output: 1

https://www.youtube.com/watch?v=UPfUFoWjk5w
"""

def dfs(vertex, edges , visited, parent):

    if vertex not in visited:
        visited.add(vertex)
    """
    base condition
        if an already visted node comes as anedge, then its a cycle
    """
    for edgenode in edges[vertex]:
        if edgenode not in visited:
            if dfs(edgenode, edges , visited, vertex):
                return True
        else:
            if parent != edgenode:
                return True
    return False
        
def detectcycle(edges):
    parents = {}
    visited = set()
    for vertex in range(len(edges)):
        if vertex not in visited:
            if dfs(vertex, edges , visited, -1):
                return True
    return False


class Solution:
    
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V, adj):
		#Code here
		return detectcycle(adj)

#edges = [[1], [0, 2, 4], [1, 3], [2, 4], [1, 3]]
edges = [[1], [0, 2, 4], [1, 3], [2, 4], [1, 3]]
edges = [[], [2], [1, 3], [2]]
s = Solution()
print(s.isCycle(5, edges))
