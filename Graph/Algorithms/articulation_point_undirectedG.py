"""

A vertex in an undirected connected graph is an articulation point (or cut vertex) if removing it (and edges through it) disconnects the graph. Articulation points represent vulnerabilities in a connected network – single points whose failure would split the network into 2 or more components. They are useful for designing reliable networks. 

For a disconnected undirected graph, 
an articulation point is a vertex removing which increases number of connected components.

Naive Approach: A simple approach is to one by one remove all vertices and see if removal of a vertex causes disconnected graph. Following are steps of simple approach for connected graph.

For every vertex v, do following:

Remove v from graph 
See if the graph remains connected (We can either use BFS or DFS) 
Add v back to the graph
Time Complexity: O(V*(V+E)) for a graph represented using adjacency list.





Efficient Approach (Using DFS) using Tarjans Algorith concept: 
The idea is to use DFS (Depth First Search). 


In DFS, we follow vertices in tree form called DFS tree. 
In DFS tree, a vertex u is parent of another vertex v, if v is discovered by u (obviously v is an adjacent of u in graph). 

In DFS tree, a vertex u is articulation point if one of the following two conditions is true. 

u is root of DFS tree and it has at least two children. 
u is not root of DFS tree and it has a child v such that no vertex in subtree rooted with v has a back edge to one of the ancestors (in DFS tree) of u.

"""


from collections import defaultdict



class Graph:
    def __init__(self, vertices) -> None:
        self.v = vertices
        self.graph = defaultdict(list)
        self.time = 0

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def APutil(self, node, disc, low, parent, visited, articulation_point):

        # tracking children (subgraph) of each ndoe
        children = 0
        
        visited[node] = True
        
        # first DFS visit, a time representing when the node is visited in DFS call 
        disc[node] = self.time 


        #to store the topmost reachable ancestor node from this subtree rooted with u
        # first DFS visit, initialise Low time as time
        low[node] = self.time

        # increment the time for its adjacent nodes
        self.time += 1

        # Peform DFS for its adjacent nodes
        for v in self.graph[node]:
            if not visited[v]:

                #setting parent of adjacent node to current node
                parent[v] = node

                #incrementing children of current vertex
                children += 1

                #recursvely call for adjacent nodes of current node
                self.APutil(v, disc, low, parent, visited, articulation_point)

                # updating low as min of (low of current node and low of its adjacent vertex
                low[node] = min(low[node], low[v])


                # case 1
                # when current vertex is a root node and has more than 1 children
                if parent[node] == -1 and children > 1:
                    articulation_point[node] = True


                """
                u is not root of DFS tree 
                and 
                it has a child v such that no vertex in subtree rooted with v has a back edge to one of the ancestors (in DFS tree) of u.
                """
                #(2) If u is not root and low value of one of its child is more
                # than discovery value of u.
                if parent[node] != -1 and low[v] >= disc[node]:
                    articulation_point[node] = True

            elif v != parent[node]: # Back edge , We don;t consider back edge to its parent
                low[node] = min(low[node], disc[v])
        

    def find_articulation(self):
        # tracking parent of each vertex
        parent = [-1] * self.v

        # disc time of every vertex
        disc = [-1] * self.v

        #low 
        low = [-1] * self.v

        # keep each vertices as AP or not
        articulation_point = [False] * self.v

        # to check if the node is currently present in stack this will help to find out if its an cross edge or back edge
        visited = [False] * self.v

        for node in self.graph:
            if not visited[node]:
                self.APutil(node, disc, low, parent, visited, articulation_point)

        for node in range(len(articulation_point)):
            if articulation_point[node]:
                print (node)

g1 = Graph(5)
g1.addEdge(1, 0)
g1.addEdge(0, 2)
g1.addEdge(2, 1)
g1.addEdge(0, 3)
g1.addEdge(3, 4)
print(g1.find_articulation())

print("===========")

g3 = Graph (7)
g3.addEdge(0, 1)
g3.addEdge(1, 2)
g3.addEdge(2, 0)
g3.addEdge(1, 3)
g3.addEdge(1, 4)
g3.addEdge(1, 6)
g3.addEdge(3, 5)
g3.addEdge(4, 5)
print(g3.find_articulation())