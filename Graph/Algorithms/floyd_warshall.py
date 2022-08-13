from collections import namedtuple
Graph = namedtuple("Graph", ["nodes", "edges"])
nodes = range(4)
edges = [
    (0, 1, 5), # [0]-- cost 5--> [1]
    (1, 2, 3),
    (2, 3, 1),
    (0, 3, 10),
]
g = Graph(nodes, edges)

class MatrixGraph:
    def __init__(self, graph: Graph) -> None:
        self.g = self.creategraph(graph)

    def creategraph(self, graph):
        """
        [
         [0, 5, inf, 10], 
         [inf, 0, 3, inf],
         [inf, inf, 0, 1],
         [inf, inf, inf, 0]
         ]
        """
        final_graph = [[float("Inf")] * len(graph.nodes) for vertex in graph.nodes]
        for edge in graph.edges:
            node1, node2, cost = edge[0], edge[1], edge[2]
            final_graph[node1][node2] = cost
        for i in range(len(final_graph)):
            for j in range(len(final_graph[i])):
                if i == j:
                    final_graph[i][j] = 0
        return final_graph

    def showg(self):
        return self.g

    def shortestpathpairs(self):
        """
        [[0, 5, 8, 9],
         [inf, 0, 3, 4],
         [inf, inf, 0, 1],
         [inf, inf, inf, 0]]
        """
        current_distance = self.g
        totalvertices = len(current_distance)
        for k in range(totalvertices):
            for i in range(totalvertices):
                for j in range(totalvertices):
                    current_distance[i][j] = min(current_distance[i][j], (current_distance[i][k]) + (current_distance[k][j]))
        return current_distance

mg = MatrixGraph(g)
print(mg.showg())
print(mg.shortestpathpairs())

