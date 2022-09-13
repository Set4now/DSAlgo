from collections import defaultdict
from typing import List
import heapq


"""
ou are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.

If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.


Approach 1:
Dijkstars Algo without using Priority Queue (Leetcode will not pass because of time complexity)
Use Dijkstras using Heap to get a O(ELogV) time complexity ( Recommended )


Bellman ford (Leetcode will not pass because of time complexity)
Bfs shortest distance
"""

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        
        """
        Python heapq provides Min Priority Queue ( Ascending order)
        But here we need Max prority Queue since we need max probability or max cost
        So, we will just use -ve integers so that Our python inbuild heapq (MinHeap) works as expected
        Use a negative priority instead

        But the ans will just depend on integer

        eg.
        
        negative priority 
        An item with priority -10 will be returned before items with priority -5, for example.
        That will be like 10 is bigger than 5

        
        """

        self.probability = {i: float("Inf") for i in range(n)}
        self.probability[start] = -1

        self.g = defaultdict(list)
        for i in range(len(edges)):
            n1 = edges[i][0]
            n2 = edges[i][1]
            probability = succProb[i]
            self.g[n1].append((n2, probability))
            self.g[n2].append((n1, probability))
        self.dijkstras(start)
        # converting the -ve to +ve , we used negative priority 
        return 0 if self.probability[end] == float("inf") else -self.probability[end]

    def dijkstras(self, node):
        #print(node)
        h = [(-1, node)]
        visited = set()

        while h:
            probability, n = heapq.heappop(h) 
            for edge, cost in self.g[n]:
                if self.probability[n] * cost < self.probability[edge]:
                    self.probability[edge] = self.probability[n] * cost
                    heapq.heappush(h, (self.probability[edge], edge))

n = 3
edges = [[0,1],[1,2],[0,2]]
succProb = [0.5,0.5,0.2]
start = 0
end = 2

# n = 3
# edges = [[0,1],[1,2],[0,2]]
# succProb = [0.5,0.5,0.3]
# start = 0
# end = 2

# n = 3
# edges = [[0,1]]
# succProb = [0.5]
# start = 0
# end = 2


# n = 5
# edges = [[1,4],[2,4],[0,4],[0,3],[0,2],[2,3]]
# succProb = [0.37,0.17,0.93,0.23,0.39,0.04]
# start = 3
# end = 4
s = Solution()
print(s.maxProbability(n, edges, succProb, start, end))