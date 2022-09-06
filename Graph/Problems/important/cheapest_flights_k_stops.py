from typing import List

# using DFS Not efficient , Cannot pass Leetcode
# class Solution:
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
#         self.g = {i: [] for i in range(n)}
        
        
#         self.n = n
#         self.distance = [float("Inf")] * n
#         self.distance[src] = 0
        
#         for node1,node2,cost in flights:
#             self.g[node1].append((node2, cost))
        

        
#         #visited[src] = True
        
#         self.allpaths = []
        
#         src_cost = 0
#         visited = [False] * n
#         visited[src] = True

#         cheapest_price = 0
#         self.results = []
#         stops = k
#         return self.dfs(src, dst, visited, stops, src_cost, k)
        
#     def dfs(self, src, dest, visited, stops, cheapest_price, k):
#         if src == dest:
#             return cheapest_price

#         for node,cost in self.g[src]:
#             stops -= 1
#             if stops >= 0 and not visited[node]:
#                 visited[node] = True
#                 return self.dfs(node, dest, visited, stops, cheapest_price + cost, k)
        
#         #cheapest_price = float("Inf")
#         # stops -= 1
#         visited[src] = False
#         return -1


# Modification of Bellman Ford 
# K + 1 times relax the edges using a temp price ( temp price for each layer if you assuime it like BFS)
# Time  -> O(E * k)
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        distance = {i: float("Inf") for i in range(n)}
        distance[src] = 0

        for i in range(k + 1):
            tempprice = distance.copy()
            for source,dest,cost in flights:
                if distance[source] == float("Inf"):
                    continue
                if distance[source] + cost < tempprice[dest]:
                    tempprice[dest] = distance[source] + cost
            distance = tempprice
        return -1 if distance[dst] == float("Inf") else distance[dst]


n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1


# n = 3
# flights = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0
# dst = 2
# k = 1


n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 0


n = 10
flights = [[3,4,4],[2,5,6],[4,7,10],[9,6,5],[7,4,4],[6,2,10],[6,8,6],[7,9,4],[1,5,4],[1,0,4],[9,7,3],[7,0,5],[6,5,8],[1,7,6],[4,0,9],[5,9,1],[8,7,3],[1,2,6],[4,1,5],[5,2,4],[1,9,1],[7,8,10],[0,4,2],[7,2,8]]
src = 6
dst = 0
k = 7

s =Solution()
print(s.findCheapestPrice(n, flights, src, dst, k))


