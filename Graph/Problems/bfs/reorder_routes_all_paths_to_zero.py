"""
Q: . Reorder Routes to Make All Paths Lead to the City Zero


There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

It's guaranteed that each city can reach city 0 after reorder.


O ---- > 1 ----> 3 <-----2
^
|------- 4 -----> 5

Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3

Change the below direction of edges  such that each node can reach the node 0 (capital).

0 ---> 1
1 ---> 3
4 ---> 5

O <---- 1 <---- 3 <-----2
^
|------- 4 <----- 5


"""


from collections import defaultdict
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self.g = defaultdict(list)
        self.inputg = {}


        # for node1,node2 in connections:
        #     self.inputg[node1].append(node2)

        for node1,node2 in connections:
            self.g[node1].append(node2)
            self.g[node2].append(node1)

            if node1 not in self.inputg:
                self.inputg[node1] = [node2]
            else:
                self.inputg[node1].append(node2)

        return self.bfs()

    

    def bfs(self):
        reordercount = 0
        q = []
        q.append(0)
        visited = set()
        visited.add(0)

        # print(self.g)
        # print(self.inputg)

        while q:
            poped = q.pop(0)
            for edge in self.g[poped]:
                if edge not in visited:
                    if edge in self.inputg:
                        if poped not in self.inputg[edge]:
                            reordercount += 1
                    else:
                        reordercount += 1
                    visited.add(edge)
                    q.append(edge)
                
        return reordercount
        
s = Solution()



a = "{:.6f}".format(2.0 * 3.0)
print(float(a))
print(type(a))

# from decimal import *
# getcontext().prec = 6
# a = Decimal(2.0 * 3.0)
# print(a)
# print(type(a))

# n = 6
# connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
# print(s.minReorder(n, connections))

# connections = [[1,0],[1,2],[3,2],[3,4]]
# print(s.minReorder(n, connections))

# n = 3
# connections = [[1,0],[2,0]]
# print(s.minReorder(n, connections))