import json
class Graph:
    def __init__(self) -> None:
        self.distance = {}
        self.edges = {}

    def add_vertex(self, vertex):
        if vertex not in self.distance and vertex not in self.edges:
            self.distance[vertex] = 0
            self.edges[vertex] = []
        else:
            print("Vertex already in the Graph.You can proceed adding edges to other vetices")

    def add_edge(self, srcvertex, destvertex, cost):
        if srcvertex in self.edges:
            self.edges[srcvertex].append((destvertex, cost))

    def __repr__(self) -> str:
        return json.dumps(self.edges)

    def bellmanford(self, src, checknegativecycle=False):
        for vertex in self.edges:
            if self.edges[vertex]:
                for edges in self.edges[vertex]:
                    dest, cost = edges[0], edges[1]
                    if self.distance[vertex] + cost < self.distance[dest]:
                        # stop , if negative cycle
                        if checknegativecycle:
                            return False
                        else:
                            if dest != src:
                                self.distance[dest] = self.distance[vertex] + cost
        return True

    def calculate_sssp(self, src):
        # setting up initial cost to infinity to all the vertices distance
        for i in self.distance:
            self.distance[i] = float("Inf")

        # setting the src vertex cost as 0
        self.distance[src] = 0

        # relax all the edges (n - 1) time
        # where n is number of vertices
        for _ in range(len(self.distance) - 1):
            self.bellmanford(src)
        
        # checking for negative cycle
        # if any node relaxed here after (n-1) relaxation, that means it has a negative cycle
        if not self.bellmanford(src, checknegativecycle=True):
            return "Sorry, Negative cyle detected, Bellman Ford doesn't work."
        return self.distance

g = Graph()
vertex = ["A", "B", "C", "D"]
for i in vertex:
    g.add_vertex(i)

g.add_edge("A", "B", 5)
g.add_edge("B", "C", 3)
g.add_edge("C", "D", -10)
g.add_edge("A", "D", 4)
#print(g.calculate_sssp("A"))
##### negative cycle graph
g.add_edge("D", "B", 5)
print(g)
print(g.calculate_sssp("A"))
