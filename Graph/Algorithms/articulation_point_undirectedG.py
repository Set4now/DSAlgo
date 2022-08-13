from collections import defaultdict
from re import U


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

                # case 2
                # when current node is not a root node 
                # and there is a back edge from its descendent to any ancestor of current vertex
                if parent[node] != -1 and low[v] >= disc[node]:
                    articulation_point[node] = True

            elif v != parent[node]:
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