"""
There is an infrastructure of n cities with some number of roads connecting these cities. Each roads[i] = [ai, bi] indicates that there is a bidirectional road between cities ai and bi.

The network rank of two different cities is defined as the total number of directly connected roads to either city. If a road is directly connected to both cities, it is only counted once.

The maximal network rank of the infrastructure is the maximum network rank of all pairs of different cities.

Given the integer n and the array roads, return the maximal network rank of the entire infrastructure.



Input: n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]
Output: 4
Explanation: The network rank of cities 0 and 1 is 4 as there are 4 roads that are connected to either 0 or 1. The road between 0 and 1 is only counted once.


https://leetcode.com/problems/maximal-network-rank/
"""

from collections import defaultdict
from typing import List


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        indegree = {i: 0 for i in range(n)}
        self.g = defaultdict(list)
        

        # computing inDegrees 
        for n1,n2 in roads:
            indegree[n1] += 1
            indegree[n2] += 1
            
            self.g[n1].append(n2)
            self.g[n2].append(n1)
            
        nodes = range(n)
        i = 1
        max_rank = 0
        while i < len(nodes):
            for j in nodes[i:]:
                # checking each pair and calculating total indegree of each node in the pair
                n1 = nodes[i - 1]
                n2 = j
                if n2 in self.g[n1] or n1 in self.g[n2]:
                    rank = ( indegree[n1] + indegree[n2] ) - 1 #  If a road is directly connected to both cities, it is only counted once.
                    max_rank = max(max_rank, rank)
                else:
                    rank = ( indegree[n1] + indegree[n2] )
                    max_rank = max(max_rank, rank)
            i += 1
            
        return max_rank