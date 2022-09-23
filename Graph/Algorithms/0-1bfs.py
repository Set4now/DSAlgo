from collections import defaultdict

from collections import deque

"""

n normal BFS of a graph all edges have equal weight but in 0-1 BFS some edges may have 0 weight and some may have 1 weight. In this we will not use bool array to mark visited nodes but at each step we will check for the optimal distance condition. We use double ended queue to store the node. While performing BFS if a edge having weight = 0 is found node is pushed at front of double ended queue and if a edge having weight = 1 is found, it is pushed at back of double ended queue.
The approach is similar to Dijkstra that the if the shortest distance to node is relaxed by the previous node then only it will be pushed in the queue. 
The above idea works in all cases, when pop a vertex (like Dijkstra), it is the minimum weight vertex among remaining vertices. If there is a 0 weight vertex adjacent to it, then this adjacent has same distance. If there is a 1 weight adjacent, then this adjacent has maximum distance among all vertices in dequeue (because all other vertices are either adjacent of currently popped vertex or adjacent of previously popped vertices).
Below is the implementation of the above idea. 


Algorithm,

Follow normal BFS shortest path
with a change
if current edge weight is 0, put it at the front of the Queue
If current edge weight is 1, append at the end

Time : V + E

"""

class Graph:
    def __init__(self) -> None:
        self.g = defaultdict(list)
        self.v = set()
    
    def addedge(self, u, v, w):
        self.g[u].append((v, w))
        self.g[v].append((u, w))
        self.v.add(u)
        self.v.add(v)

    def shortest_path(self, src):

        Q = deque()
        Q.append(src)

        distance = {u: float("Inf") for u in self.v}
        distance[src] = 0

        while Q:
            popped = Q.popleft()
            for edge, weight in self.g[popped]:
                if distance[popped] + weight < distance[edge]:
                    distance[edge] = distance[popped] + weight 

                    if weight == 0:
                        Q.appendleft(edge)
                    else:
                        Q.append(edge)

        return distance


g  = Graph()
g.addedge(0, 1, 1)
g.addedge(0, 2, 1)
g.addedge(0, 7, 1)
g.addedge(0, 8, 0)
g.addedge(1, 2, 0)
g.addedge(1, 3, 1)
g.addedge(1, 7, 0)

g.addedge(2, 5, 1)
g.addedge(2, 6, 0)
g.addedge(3, 4, 1)
g.addedge(4, 5, 1)
g.addedge(5, 6, 1)
g.addedge(6, 7, 1)
g.addedge(7, 8, 1)

print(g.shortest_path(2))