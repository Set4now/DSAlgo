from collections import defaultdict
from typing import List

"""
Possible Bipartition


We want to split a group of n people (labeled from 1 to n) into two groups of any size. Each person may dislike some other people, and they should not go into the same group.

Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person labeled ai does not like the person labeled bi, return true if it is possible to split everyone into two groups in this way.

 

Example 1:

Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4] and group2 [2,3].


Algorithm
check if the graph is bipartite or not using 2 colors technique

Note: Your need to convert the directed graph to undirected graph for the 2 colors algo to work
"""
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        self.g = defaultdict(list)

        for n1,n2 in dislikes:
            self.g[n1].append(n2)
            self.g[n2].append(n1)

        colors = {i: None for i in range(1, n+1)}
        colors[1] = "green"
        


        def bfs(i):

            q = []
            q.append(i)
            #visited[i] = True

            while q:
                node = q.pop(0)
                for edge in self.g[node]:
                    # if not visited[edge]:
                    # if edge not in visited:
                        if colors[edge] is None:
                            if colors[node] == "green":
                                colors[edge] = "red"
                            else:
                                colors[edge] = "green"
                            #visited.add(edge)
                            q.append(edge)
                        else:
                        # return False if they are in the same set and its not bipartite
                            if colors[node] == colors[edge]:
                            # print(node, colors[node], edge, colors[edge])
                                return False
            # bipartite
            #print(colors)
            return True
        

        for i in range(1, n + 1):
            if not bfs(i):
                return False
        return True
        

n = 4
dislikes = [[1,2],[1,3],[2,4]]


# n = 3
# dislikes = [[1,2],[1,3],[2,3]]

# n = 5
# dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]

# n = 5
# dislikes = [[1,2],[3,4],[4,5],[3,5]]


# n = 3
# dislikes = [[1,2],[1,3],[2,3]]
s= Solution()
print(s.possibleBipartition(n, dislikes))
