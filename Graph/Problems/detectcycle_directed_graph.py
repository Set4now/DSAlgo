class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        visited = []
        for node in range(V):
            if node not in visited:
                dfs_stack = []
                if self.checkcycle(node, visited, dfs_stack, adj):
                    return 1
        return 0
                
        
    def checkcycle(self, node, visited, dfs_stack, adj):
        visited.append(node)
        dfs_stack.append(node)
        
        for edgenode in adj[node]:
            if edgenode not in visited:
                # print(edgenode, dfs_stack)
                if edgenode in dfs_stack:
                    return True
                else:
                    return self.checkcycle(edgenode, visited, dfs_stack, adj)
        visited.pop()
        return False

s = Solution()
input = [[], [2], [4], [1], [0], [3]]
v = 6

input = [[1], [3, 0], [0], [1]]
v = 4
print(s.isCyclic(v, input))


