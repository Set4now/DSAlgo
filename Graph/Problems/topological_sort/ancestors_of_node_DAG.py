from collections import defaultdict
from typing import List

"""

https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

All Ancestors of a Node in a Directed Acyclic Graph

You are given a positive integer n representing the number of nodes of a Directed Acyclic Graph (DAG). The nodes are numbered from 0 to n - 1 (inclusive).

You are also given a 2D integer array edges, where edges[i] = [fromi, toi] denotes that there is a unidirectional edge from fromi to toi in the graph.

Return a list answer, where answer[i] is the list of ancestors of the ith node, sorted in ascending order.

A node u is an ancestor of another node v if u can reach v via a set of edges.


Using Topological sort (Khans Algorothm using Queue)

The idea is whenever we get a node whose edges indegree becomes 0,
add the node and the nodes ancestor to edge ancestor list.

V + E

"""

class Graph:
    def topological_order(self, n, edges) -> None:

        self.g = defaultdict(list)
        #self.indegreenodes = defaultdict(list)


        indegree = [0] * n

        for n1,n2 in edges:
            self.g[n1].append(n2)
            #self.indegreenodes[n2].append(n1)
            indegree[n2] += 1
        
        self.ans = [set() for _ in range(n)]
        q = []
                                                                                              
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            popped = q.pop(0)
            
            for edge in self.g[popped]:
                indegree[edge] -= 1
                # add the popped node to edge ancestor list
                self.ans[edge].add(popped)
                self.ans[edge].update(self.ans[popped])
                if indegree[edge] == 0:
                    q.append(edge)
        return self.ans


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ancestors = Graph().topological_order(n, edges)
        return [ sorted(list(a)) for a in ancestors]
n = 8
edgeList = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]

n = 5
edgeList = [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

n = 6
edgeList = [[0,3],[5,0],[2,3],[4,3],[5,3],[1,3],[2,5],[0,1],[4,5],[4,2],[4,0],[2,1],[5,1]]

# [[2, 4, 5], [0, 2, 4, 5], [4], [0, 1, 2, 4, 5], [], [2, 4]]
s = Solution()
print(s.getAncestors(n, edgeList))


###### Another approach using Simble BFS for each node

# class Solution:
#     def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
#         self.g = defaultdict(lambda:[])
    
#         for n1,n2 in edges:
#             self.g[n2].append(n1)

#         # q = []
#         # for i in range(n):
#         #     q.append(i)

#         def bfs(i):
#             q = [i]
#             visited = set()

#             while q:
#                 node = q.pop(0)
#                 if node in visited:
#                     continue
#                 visited.add(node)
#                 for edge in self.g[node]:
#                     q.append(edge)

#             visited.discard(node) 
#             return sorted(list(visited))



        
#         ans = []
#         for i in range(n):
#             ans.append(bfs(i))

#         return ans

n = 6
edgeList = [[0,3],[5,0],[2,3],[4,3],[5,3],[1,3],[2,5],[0,1],[4,5],[4,2],[4,0],[2,1],[5,1]]

# [[2, 4, 5], [0, 2, 4, 5], [4], [0, 1, 2, 4, 5], [], [2, 4]]
s = Solution()
print(s.getAncestors(n, edgeList))
            