from collections import defaultdict
from platform import node
from typing import List

# Time --> V + E
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        self.g = defaultdict(list)


        self.division_results = {}
        self.vertices = []

        for i in range(len(equations)):
            # creating a undirected graph
            self.g[equations[i][0]].append(equations[i][1])
            self.g[equations[i][1]].append(equations[i][0])
            if equations[i][0] not in self.vertices:
                self.vertices.append(equations[i][0])
            if equations[i][1] not in self.vertices:
                self.vertices.append(equations[i][1])

            # storing 2 division results for a edge pair  (u,v) in a division_results hashmap
            # division_results = {}
            # division_results["u/v"] = value from  values 
            # division_results["v/u"] = ( 1 / value of u / v from values )
            if i < len(values):
                node1, node2 = equations[i][0], equations[i][1]

                self.division_results[f"{node1}/{node2}"] = values[i]

                node2bynode1 = 1 / values[i]
                self.division_results[f"{node2}/{node1}"] = node2bynode1

        queries_result = []


        # Run a DFS
        for i in range(len(queries)):
            node1, node2 = queries[i][0], queries[i][1]
            # -1.0 for any unknown string or vertex
            if node1 not in self.vertices or node2 not in self.vertices:
                queries_result.insert(i, -1.0)
            else:
                # 1.0 if both input are same
                if node1 == node2:
                    queries_result.insert(i, 1.0)
                else:
                    # else start DFS and store all the vertices along the path if we can reach node2 (destination)
                    visited = set()
                    queries_result.insert(i, [node1])
                    if not self.dfs(node1, node2, queries_result, visited, i, self.g):
                        # if we can't reach than -1.0
                        queries_result[i] =  -1.0

        final = []

        # Finally compute result for each path and append it in final
        # Formula
        # if path of (a,d) is a--b--c--d
        # then a / d = a / b * b / c * c / d
        # if path of (e,b) is e--d--c--e
        # then e / b = e / d * d / c * c / b

        for i in range(len(queries_result)):
            each = queries_result[i]
            if type(each) == list:
                i = 0
                result = 1
                while i < len(each) - 1:
                    node1 = each[i]
                    node2 = each[i+1]
                    newresult = float(result * self.division_results[f"{node1}/{node2}"])
                    result = newresult
                    i += 1
                final.append(result)
            else:
                final.append(each)

        return final

    # Keep traversing until we reach destination
    def dfs(self, node, target, result, visited : set, resultindex, graph):
        visited.add(node)
        if node == target:
            return True
        for edge in graph[node]:
            if edge not in visited:
                if f"{node}/{edge}" in self.division_results:
                    result[resultindex].append(edge)
                    if self.dfs(edge, target, result, visited, resultindex, graph):
                        return True 
        result[resultindex].pop()
        visited.discard(node)


# equations = [["a","b"],["b","c"]]
# values = [2.0,3.0]

# queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]


equations = [["a","b"],["b","c"],["bc","cd"]]
values = [1.5,2.5,5.0]
queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]


equations = [["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]]
values = [3.0,4.0,5.0,6.0]
queries = [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]


#queries = [["x2","x4"]]

equations = [["a","e"],["b","e"]]
values = [4.0,3.0]
queries = [["a","b"],["e","e"],["x","x"]]

equations = [["x1","x2"],["x2","x3"],["x1","x4"],["x2","x5"]]
values = [3.0,0.5,3.4,5.6]
queries = [["x2","x4"],["x1","x5"],["x1","x3"],["x5","x5"],["x5","x1"],["x3","x4"],["x4","x3"],["x6","x6"],["x0","x0"]]


# 1.33332, 1, -1.0]
s = Solution()
print(s.calcEquation(equations, values, queries))


