from collections import defaultdict
class Graph:
    """
    Walk: A random traversal in a Graph 

    Trail: A Walk in which no edge is repeated

    Euler Path: A path which visits every edge only once

    Eulerian Circuit: A Trail that starts and end at the same node (vertex)


    Eulerian Graph:
    Two Conditions:- 
        a) All the edges should be visited once. 
           This also means all the vertices with non zero degress should be in a single component
           Rest all the disconnected component should not have any edge (means only 0 degree allowed)
        b) All the vertices in the graph should have EVEN number of edges


    Semi Eulerian Graph:
    a) All the edges should be visited once
    b) Exactly 2 vertices will have odd egdes 
    NOTE: This is an Euler Path but not Eulerian Circuit

    NOT Eulerian Graph:
    1. All the edges are visited
    2. But the count of nodes whose degrees are ODD are more than 2


    """
    def __init__(self) -> None:
        self.graph = defaultdict(list)
        self.degrees = {}

    def addEdge(self, src, dest):
        self.graph[src].append(dest)
        if src in self.degrees:
            self.degrees[src] += 1
        else:
            self.degrees[src] = 1

        # also incrementing degree while adding edges
        self.graph[dest].append(src)
        if dest in self.degrees:
            self.degrees[dest] += 1
        else:
            self.degrees[dest] = 1

    def dfs(self, node, visited, graph):
        if node not in visited:
            visited.add(node)
        for edge in graph[node]:
            if edge not in visited:
                self.dfs(edge, visited, graph)

    def check_eulerian(self):
        #Run DFS to check connectivity 
        visited = set()
        for node in self.graph:
            if node not in visited:
                self.dfs(node, visited, self.graph)
        
        ####### Condition 
        #checking if any node with degree more than 0 is unvsited
        # if yea then its not an Eulerian Graph
        for node in self.graph:
            if self.degrees[node] > 0:
                if self.degrees[node] not in visited:
                    return "This is not an Eulerian Graph"
        
        ######## Condition 2 ############
        # Count Odd Degree Node:
        count = 0
        for node in self.degrees:
            if self.degrees[node] % 2 != 0:
                count += 1

        if count == 0: # An Eulerian Graph have all edges visited once and always have even edges
            return "Graph Eulerian"
        if count == 2: # 2 verices will always have odd edges
            return "Graph is Semi Eulerian"
        if count > 2:
            return "Graph is not Eulerian"
g1 = Graph()
g1.addEdge(1, 0)
g1.addEdge(0, 2)
g1.addEdge(2, 1)
g1.addEdge(0, 3)
g1.addEdge(3, 4)
print(g1.check_eulerian())




g2 = Graph()
g2.addEdge(1, 0)
g2.addEdge(0, 2)
g2.addEdge(2, 1)
g2.addEdge(0, 3)
g2.addEdge(3, 4)
g2.addEdge(4, 0)
print(g2.check_eulerian())
      

g3 = Graph()
g3.addEdge(1, 0)
g3.addEdge(0, 2)
g3.addEdge(2, 1)
g3.addEdge(0, 3)
g3.addEdge(3, 4)
g3.addEdge(1, 3)
print(g3.check_eulerian())



g4 = Graph()
g4.addEdge(0, 1)
g4.addEdge(1, 2)
g4.addEdge(2, 0)
print(g4.check_eulerian())

