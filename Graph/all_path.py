from copy import deepcopy
from typing import List


class Solution:

    def dfs(self, vertex, edgelist, path, result):
        path.append(vertex)
        # if not edgelist[vertex]:
        if path[-1] == len(edgelist) - 1:
            result.append(deepcopy(path))
        else:
            for node in edgelist[vertex]:
                self.dfs(node, edgelist, path, result)
        path.pop()

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        edgelist = {v : [] for v in range(len(graph))}
        for v in range(len(graph)):
            for node in graph[v]:
                edgelist[v].append(node)
        #print(edgelist)
        path = []
        result = []

        self.dfs(0, edgelist, path, result)
        return result
graph = [[1,2],[3],[3],[]]
graph = [[4,3,1],[3,2,4],[],[4],[]]
#graph = [[2],[],[1]]
s = Solution()
print(s.allPathsSourceTarget(graph))
