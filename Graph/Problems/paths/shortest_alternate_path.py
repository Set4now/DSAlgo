from collections import defaultdict, deque
from typing import List


# this is not an optimized version, thus will give LTE
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        ans_distance = [-1] * n
        ans_distance[0] = 0
        
        if n == 1:
            return ans_distance
        
        self.g = defaultdict(list)
        for n1,n2 in redEdges:
            self.g[n1].append((n2, "red"))
        for n1,n2 in blueEdges:
            self.g[n1].append((n2, "blue"))
    
        

        def bfs(q, visited):                  
            while q:
                src_color, src_distance, src = q.pop(0)
                if src in visited:
                    src_distance += 1
                    for edge, edge_colr in self.g[src]:
                    #if edge not in visited:
                        if edge_colr != src_color:
                            q.append((edge_colr, src_distance, edge))
                    continue
                visited.add(src)
                
                if ans_distance[src] == -1:
                    ans_distance[src] = src_distance

                for edge, edge_colr in self.g[src]:
                    if edge not in visited:
                        if edge_colr != src_color:
                            q.append((edge_colr, src_distance + 1, edge))
        q = []
        src_distance = 0
        src = 0 
        q.append(("green", src_distance, src))
        q.append(("blue", src_distance, src))
        visited = set()
        #visited.add(src)
        bfs(q, visited)
        return ans_distance


# Optimized BFS version similar to finding level of node in BFS
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        q=deque([(0,'g')])
        res,steps=[-1]*n,0
        seen=set()
        adj=defaultdict(list)
        for x,y in redEdges:
            adj[x].append((y,'r'))
        for x,y in blueEdges:
            adj[x].append((y,'b'))

        #print(adj)

        while q:
            #print(q)
            for _ in range(len(q)):
                curr=q.popleft()
                #print(curr, steps)
                if curr in seen:
                    continue
                seen.add(curr)
                if res[curr[0]]==-1:
                    res[curr[0]]=steps
                for nei in adj[curr[0]]:
                    if nei[1]!=curr[1]:
                        q.append(nei)
            steps+=1
        return res


n = 3
redEdges = [[0,1],[0,2]]
blueEdges = [[1,0]]


n = 3
redEdges = [[0,1],[1,2]]
blueEdges = []

# n = 3
# redEdges = [[0,1]]
# blueEdges = [[2, 1]]


# n = 3
# redEdges = [[0,1]]
# blueEdges = [[1,2]]

# n = 3
# redEdges = [[0,1],[0,2]]
# blueEdges = [[1,0]]


n = 5
redEdges = [[0,1], [1,2],[2,3],[3,4]]
blueEdges = [[1,2],[2,3],[3,1]]


s = Solution()
print(s.shortestAlternatingPaths(n, redEdges, blueEdges))