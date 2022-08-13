
# DFS on every vertex to check if all vertices are reachable from it or not?
# O(V * (V + E))
class Solution:
    def findMotherVertex(self, V, adj):
		#Code here
        visited = []
        mother_vertex = []
        for i in range(V):
            visited = []
            self.dfs(i, visited, adj)
            if len(visited) == V:
                mother_vertex.append(i)
        if mother_vertex:
            return min(mother_vertex)
        return -1

    def dfs(self, node, visited, adj):
        visited.append(node)
        if adj[node]:
            for edgenode in adj[node]:
                if edgenode not in visited:
                    self.dfs(edgenode, visited, adj)
        