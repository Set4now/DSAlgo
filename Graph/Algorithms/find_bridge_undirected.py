"""
An edge in an undirected connected graph is a bridge if removing it disconnects the graph. 

For a disconnected undirected graph, definition is similar, 
a bridge is an edge removing which increases number of disconnected components. 


Like Articulation Points, bridges represent vulnerabilities in a connected network and 
are useful for designing reliable networks.


For example, in a wired computer network, an articulation point indicates the critical computers and a bridge indicates the critical wires or connections.



Naive Approach: 


A simple approach is to one by one remove all edges and see if removal of an edge causes disconnected graph. 



Following are steps of simple approach for connected graph.

For every edge (u, v), do following :

Remove (u, v) from graph 
See if the graph remains connected (We can either use BFS or DFS) 
Add (u, v) back to the graph.

Time Complexity: O(E*(V+E)) for a graph represented using adjacency list.



Efficient Approach:  

The idea is similar to O(V+E) algorithm for Articulation Points. 

We do DFS traversal of the given graph. In DFS tree an edge (u, v) (u is parent of v in DFS tree) is bridge if there does not exist any other alternative to reach u or an ancestor of u from subtree rooted with v. 

As discussed in the previous post, the value low[v] indicates earliest visited vertex reachable from subtree rooted with v.
The condition for an edge (u, v) to be a bridge is, “low[v] > disc[u]”. 

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

    def APutil(self, node, low, disc, visited, parent, brides):
        
        visited[node] = True
        disc[node] = self.time

        low[node] = self.time 


        self.time += 1

        for v in self.graph[node]:
            if not visited[v]:
                parent[v] = node
                self.APutil(v, low, disc, visited, parent, brides)

                
                low[node] = min(low[node], low[v])

                # The condition for an edge (u, v) to be a bridge is, “low[v] > disc[u]”
                # Tarjans algorithm for a back edge

                ''' 
                
                it has a child v such that no vertex in subtree rooted with v has a back edge to one of the ancestors (in DFS tree) of u.

                This also means
                If the lowest vertex reachable from subtree
                under v is below u in DFS tree, then u-v is
                a bridge
                
                '''
                if low[v] > disc[node]:
                    brides.append((node, v))

            elif v != parent[node]: # Back edge Back edge , We don;t consider back edge to its parent
                low[node] = min(low[node], disc[v])
    
    def get_bridges(self):
        brides = []

        parent = [-1] * self.v 

        low = [-1] * self.v 

        disc = [-1] * self.v

        visited = [False] * (self.v)

        for i in range(self.v):
            if not visited[i]:
                self.APutil(i, low, disc, visited, parent, brides)

        print(brides)

g1 = Graph(5)
g1.addEdge(1, 0)
g1.addEdge(0, 2)
g1.addEdge(2, 1)
g1.addEdge(0, 3)
g1.addEdge(3, 4)
g1.get_bridges()


g3 = Graph (7)
g3.addEdge(0, 1)
g3.addEdge(1, 2)
g3.addEdge(2, 0)
g3.addEdge(1, 3)
g3.addEdge(1, 4)
g3.addEdge(1, 6)
g3.addEdge(3, 5)
g3.addEdge(4, 5)
g3.get_bridges()