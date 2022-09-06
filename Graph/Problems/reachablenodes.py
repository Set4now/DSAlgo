from collections import defaultdict
from typing import List


class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        self.g = defaultdict(list)
        self.g[0] = []
        
        for n1,n2 in edges:
            #if n1 not in restricted and n2 not in restricted:
            self.g[n1].append(n2)
            self.g[n2].append(n1)
                
        visited = set()
            
        restricted = set(restricted)
        
        def dfs(node, visited):
            visited.add(node)
            for x in self.g[node]:
                if x not in visited and x not in restricted:
                    dfs(x, visited)
                    
        dfs(0, visited)
        return len(visited)
                

n = 7
edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]]
restricted = [4,5]
s = Solution()
print(s.reachableNodes(n, edges, restricted))