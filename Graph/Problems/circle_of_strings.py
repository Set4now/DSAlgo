#https://practice.geeksforgeeks.org/problems/circle-of-strings4530/1

"""

Given an array of lowercase strings A[] of size N, determine if the strings can be chained together to form a circle.
A string X can be chained together with another string Y if the last character of X is same as first
character of Y. If every string of the array can be chained, it will form a circle.

For example, for the array arr[] = {"for", "geek", "rig", "kaf"} the answer will be Yes as the given strings can be chained as "for", "rig", "geek" and "kaf"


Example 1:

Input:
N = 3
A[] = { "abc", "bcd", "cdf" }
Output:
0
Explaination:
These strings can't form a circle 
because no string has 'd'at the starting index.
Example 2:

Input:
N = 4
A[] = { "ab" , "bc", "cd", "da" }

a ---> b
|      |
d <---  c
Output:
1
Explaination:
These strings can form a circle 
of strings.

Solution:
Consider the first and last character as 2 nodes in an edge

Check if the directed graph has a Eulerian Circuit or not?

Using Kosarajus algorithm

Both conditions 1 & 2 must be True
1. All the non zero degree vertices should be a part of one singly Connected Component
2. The In degree and Out degree of all the vertices should be samme 
"""
from collections import defaultdict

class Solution:
    def isCircle(self, N, A):
        self.graph = defaultdict(list)
        self.transposed_graph = defaultdict(list)
        self.vertices = set()
        self.indegree = {}
        return self.iseuleriancycle(A)

    def add_edges(self, A):
        for word in A:
            edges = [char for char in word]
            if len(edges) == 1:
                if edges[0] not in self.graph:
                    self.graph[edges[0]] = []
                    self.vertices.add(edges[0])
                    if edges[0] not in self.indegree:
                        self.indegree[edges[0]] = 0
            else:
                src = edges[0]
                dest = edges[-1]
                if src not in self.graph:
                    self.graph[src] = [dest]
                else:
                    self.graph[src].append(dest)

                self.vertices.add(src)
                self.vertices.add(dest)

                if src not in self.indegree:
                    self.indegree[src] = 0
                # else:
                #     self.indegree[src] += 1

                if dest not in self.indegree:
                    self.indegree[dest] = 1
                else:
                    self.indegree[dest] += 1
                
                

    def dfs(self, node, visited, graph):
        visited[node] = True
        for edge in graph[node]:
            if not visited[edge]:
                self.dfs(edge, visited, graph)

    def transpose(self):
        for vertex, edges in self.graph.items():
            for edge in edges:
                if edge not in self.transposed_graph:
                    self.transposed_graph[edge] = [vertex]
                else:
                    self.transposed_graph[edge].append(vertex)

    def isconnected(self, A):
        """
        Finding if a directed graph is singly strongly connected 

        Kosaraju Algorithm

        1. Peform a DFS (using a starting vertex) (to check if all the other vertices
            are reachable from this starting vertex
            check if any vertex not visted,
               if not visited then False, means graph is not connected
        2. Transpose the matrix
        3  Perform DFS again using the same start_vertex on the transposed_graph
             if any vertex not visited then graph is not connected 

        Using the property:
           after transposing the graph the SCC should not change

        """
        self.add_edges(A)
        visited = {v: False for v in self.vertices}
        
        import random
        start_vertex = random.choice(list(visited))


        self.dfs(start_vertex, visited, self.graph)
        
        # condition 1 using kosar
        for v in visited:
            if not visited[v]:
                return 0

            
        self.transpose()

        visited = {v: False for v in self.vertices}
        self.dfs(start_vertex, visited, self.transposed_graph)

        for v in visited:
            if not visited[v]:
                return 0
        return 1

    def iseuleriancycle(self, A):
        """
        Algorithm to check if a directed graph has a Eulerian Circuit

        1. All the non zero degree vertices should be in the same connected component
        2. ALl the vertices should be In degree == Out degree
           
        """
        if self.isconnected(A) == 0:
            return 0
        
        # print(self.indegree)
        #print(self.graph)
        for v in self.graph:
            if len(self.graph[v]) != self.indegree[v]:
                return 0
        return 1

s =Solution()
N = 4
A = [ "ab" , "bc", "cd", "da" ]

# N = 3
# A = [ "abc", "bcd", "cdf" ]


N  = 4
A = ["aa", "aa", "aa", "aa"]

N = 1
A = ["v"]
print(s.isCircle(N, A))