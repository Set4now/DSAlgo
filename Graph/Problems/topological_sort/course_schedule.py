class Solution:
    
    def dfs(self, node, visited, recstack, stack, graph):
        visited.append(node)
        recstack.append(node)
        
        for edge in graph[node]:
            if edge not in visited:
                if self.dfs(edge, visited, recstack, stack, graph):
                    return True
            elif edge in recstack:
                return True
        stack.append(node)
        # once finished traversing, remove it from recursion stack
        recstack.pop()
        return False

    def findOrder(self, n, m, prerequisites):
        graph = {v: [] for v in range(n)}
        
        for (src, dest) in prerequisites:
            graph[src].append(dest) 

        visited = []
        stack = [] # track the ordering of task
        recstack = [] # to detect cycle by tracking the recursion stack or 

        for node in graph:
            if node not in visited:
                # return empty array if ordering is not possible
                if self.dfs(node, visited, recstack, stack, graph):
                    return []
        return stack


n = 4
m = 4
prerequisites = [[1, 0],[2, 0],[3, 1],[3, 2]]
s = Solution()
print(s.findOrder(n, m , prerequisites))

