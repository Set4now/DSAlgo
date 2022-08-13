"""
Tarjans Algorithm for finding SCC in a directed graph 

"""
from collections import defaultdict

class Graph:
    def __init__(self, vertices) -> None:
        self.v = vertices
        self.graph = defaultdict(list)
        self.time = 0

    def addEdge(self, u, v):
        self.graph[u].append(v)

    
    def dfsutil(self, u, low, disc, visited, instack):

        self.time += 1

        """
        when DFS starts for a node, the initial low and disc will be set to current time 
        """
        #to store the topmost reachable ancestor node from this subtree rooted with u 
        low[u] = self.time

        #disc is the discovery time, first time when the node is visited in the DFS call
        disc[u] = self.time

        # to check if the node is currently present in stack this will help to find out if its an cross edge or back edge
        visited[u] = True 

        # to store the nodes whuch will be find in dfs call path
        instack.append(u)

        for v in self.graph[u]:
            # dfs for nodes which are not yet visited 
            if disc[v] == -1: 
                self.dfsutil(v, low, disc, visited, instack)

                # For normal Tree edge 
                low[u] = min(low[u], low[v])

            elif visited[v] == True:

                # Back edge
                low[u] = min(low[u], disc[v])

        # We have reach to a point where u does not have any adjacent nodes left for to be processed
        # now check if u is a head node or not
        # if u is a head node, then pop all the elements from stack until you move out head 
        # all the popped nodes are part of 1 SCC
        temp = -1
        scc = []
        # u is a head node if low[u] == disc[u]
        if low[u] == disc[u]:
            while temp != u:
                popped = instack.pop()
                scc.append(popped)
                temp = popped
                visited[popped] = False
        if scc:
            print(scc)
        
             
    def tarjans_get_scc(self):
        visited = [False] * self.v
        low = [-1] * self.v
        disc = [-1] * self.v

        instack = []

        for i in range(self.v):
            if disc[i] == -1:
                self.dfsutil(i, low, disc, visited, instack)

# Create a graph given in the above diagram
g1 = Graph(5)
g1.addEdge(1, 0)
g1.addEdge(0, 2)
g1.addEdge(2, 1)
g1.addEdge(0, 3)
g1.addEdge(3, 4)
print ("SSC in first graph ")
g1.tarjans_get_scc()


g4 = Graph(11)
g4.addEdge(0, 1)
g4.addEdge(0, 3)
g4.addEdge(1, 2)
g4.addEdge(1, 4)
g4.addEdge(2, 0)
g4.addEdge(2, 6)
g4.addEdge(3, 2)
g4.addEdge(4, 5)
g4.addEdge(4, 6)
g4.addEdge(5, 6)
g4.addEdge(5, 7)
g4.addEdge(5, 8)
g4.addEdge(5, 9)
g4.addEdge(6, 4)
g4.addEdge(7, 9)
g4.addEdge(8, 9)
g4.addEdge(9, 8)
print ("nSSC in fourth graph ")
g4.tarjans_get_scc();

        