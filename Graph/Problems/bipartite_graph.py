"""
Question:
There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

There are no self-edges (graph[u] does not contain u).
There are no parallel edges (graph[u] does not contain duplicate values).
If v is in graph[u], then u is in graph[v] (the graph is undirected).
The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.





A Bipartite Graph is a graph whose vertices can be divided into two independent sets, 
U and V such that every edge (u, v) either connects a vertex from U to V or a vertex from V to U. 


In other words, for every edge (u, v), either u belongs to U and v to V, or u belongs to V and v to U. 
We can also say that there is no edge that connects vertices of same set.

A bipartite graph is possible if the graph coloring is possible using two colors such that vertices in a set are colored with the same color.

One important observation is a graph with no edges is also Bipartite.


If a bipartite graph is not connected, it may have more than one bipartition

Algorithm:

    Fact: In a Bipartite Graph, every edge should be connected to 2 diff vertices from 2 sets
    eg, (u,v)
    u (set U) --> v (set V) OR v (Set V) --> u (Set u)

"""
from typing import List
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        self.graph = {index: edges for index,edges in enumerate(graph)}
        
        self.colors = {v: None for v in self.graph} # setting None as default initial color for all the vertices
        self.colors[0] = "green" #setting initial color src vertex as green
        visited = set()

        for vertex in self.graph:
            if vertex not in visited:
                if not self.bfs(vertex, visited, self.colors, self.graph):
                    return False
        return True 



        
    def bfs(self, node, visited, colors, graph):
        queue = []
        queue.append(node)
        

        while queue:
            popleft = queue[0]
            del queue[0]
            
            if graph[popleft]:
                for edge in graph[popleft]:
                    if edge not in visited:
                        if colors[edge] is None:
                            if colors[popleft] == "green":
                                colors[edge] = "blue"
                            else:
                                colors[edge] = "green"
                            queue.append(edge)
                        elif colors[popleft] == colors[edge]:
                            return False
        return True















        
