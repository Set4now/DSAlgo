"""

There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.

Return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold, If there are multiple such cities, return the city with the greatest number.

Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.


https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

Solution
Floyd Warshall algorithm to find all pair shortest path (O v^3)
then for each node, extract all the nodes which has path cost <= threshold

find all the cities (in a list) which has Smallest Number of Neighbors at a Threshold Distance
return the max ( of the list)


"""

from typing import List

class Graph:
    def __init__(self, n, graph) -> None:
        self.adjmtrx = [[float("inf")] * n for _ in range(n)]
        for i in range(len(graph)):
            n1, n2, cost = graph[i]
            self.adjmtrx[n1][n2] = cost
            self.adjmtrx[n2][n1] = cost
                    
        for i in range(len(self.adjmtrx)):
            self.adjmtrx[i][i] = 0 #self distance is always 0
    
    def floyd_marshall(self, n):
        #print(self.adjmtrx)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    self.adjmtrx[i][j] = min(self.adjmtrx[i][j], (self.adjmtrx[i][k] + self.adjmtrx[k][j]))
        return self.adjmtrx


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        s = Graph(n, edges)
        self.distance = s.floyd_marshall(n)

        ans = {i: [] for i in range(n)}

        for i in range(len(self.distance)):
            for j in range(len(self.distance[i])):
                if i != j: # ignoring self loop
                    if self.distance[i][j] <= distanceThreshold:
                        ans[i].append(j)

        city_with_smallest_neighbors = []
        smallest_neighbors = float("Inf")


        for city in ans:
            if len(ans[city]) <= smallest_neighbors:
                smallest_neighbors = len(ans[city])
                city_with_smallest_neighbors.append(city)

        return max(city_with_smallest_neighbors)



n = 4
edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
distanceThreshold = 4


n = 5
edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]
distanceThreshold = 2

s= Solution()
print(s.findTheCity(n, edges, distanceThreshold))