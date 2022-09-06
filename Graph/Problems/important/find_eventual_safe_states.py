from collections import defaultdict
from typing import List








"""
# inefficient solution (v + E) * n
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        self.g = defaultdict(list)
        self.terminal = set()
        
        unsafenode = set()
        safenodes = set()
        
        n = len(graph)

        for i in range(n):
            if not graph[i]:
                self.terminal.add(i)
                self.g[i] = []
            else:
                for edge in graph[i]:
                    if edge == i:
                        unsafenode.add(edge)
                    
                    self.g[i].append(edge)

        
        def dfs(node, visited, start, unsafenode, recstack):
    
            visited[node] = True
            recstack[node] = True
            if node in unsafenode:
                unsafenode.add(start)
                return False
            if node in self.terminal:
                recstack[node] = False
                return True
            for edge in self.g[node]:
                if not visited[edge]:
                    if not dfs(edge, visited, start, unsafenode, recstack):
                        return False
                elif recstack[edge] == True:
                    unsafenode.add(start)
                    return False
            recstack[node] = False
            return True

        for i in range(n):
            if i not in unsafenode:
                visited = [False] * len(graph)
                recstack = [False] * len(graph)
                if dfs(i, visited, i, unsafenode, recstack):
                    safenodes.add(i)  

        for n in self.terminal:
            safenodes.add(n)

        return sorted(list(safenodes))


"""


"""
# Detecting cycle with colors
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        ans = [0] * len(graph)
        
        def dfs(node):
            ans[node] = 1
            
            for edge in graph[node]:
                if ans[edge] == 0:
                    dfs(edge)
                if ans[edge] == 1:
                    return False
            ans[node] = 2
            return True
        
        for i in range(len(graph)):
            if ans[i] == 0:
                dfs(i)
        return [ i for i in range(len(graph)) if ans[i] == 2]
"""

    
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        unsafenodes = [False] * n # Starting every node as safe
        visited = [False] * n

        def dfs(node, unsafenodes, visited):
            
            unsafenodes[node] = True
            visited[node] = True
            
            for edge in graph[node]:
                if not visited[edge]:
                    if not dfs(edge, unsafenodes, visited): #stop if any child node is not safe
                        return False
                elif unsafenodes[edge] == True: # cycle
                    return False

            unsafenodes[node] = False # all child nodes are safe, means current node is also safe
            return True
        
        for i in range(n):
            if not unsafenodes[i]: # dfs for every unsafe nodes
                dfs(i, unsafenodes, visited)
       
        return [i for i in range(n) if unsafenodes[i] == False]



s = Solution()
graph = [[1,2],[2,3],[5],[0],[5],[],[]]


graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]

graph = [[],[0,2,3,4],[3],[4],[]]

#graph = [[1, 2], [1], [], []]
print(s.eventualSafeNodes(graph))