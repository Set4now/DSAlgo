class Graph:
    def __init__(self) -> None:
        # Graph: {}
        self.adjacency_list = {}

    def __repr__(self) -> str:
        return f"Graph: {self.adjacency_list}"

    def add_vertex(self, vertex):
        # Graph: {"A": []}
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
            return True
        return False

    def add_edge(self, vertex1, vertex2):
        # Graph: {'A': ['B', 'C'], 'B': ['A', 'C'], 'C': ['A', 'B']}
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        else:
            return False

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            if vertex2 in self.adjacency_list[vertex1] and vertex1 in self.adjacency_list[vertex2]:
                self.adjacency_list[vertex1].remove(vertex2)
                self.adjacency_list[vertex2].remove(vertex1)
            else:
                print(f'Vertex not connected. [{vertex1}] -!- [${vertex2}]')
        return False


    def remove_vertex(self, vertex):
        # check if vertex exist in graph or not
        if vertex not in self.adjacency_list:
            return False
        
        # find the vertices to which the current vertex is connected
        # and delete the link 
        connected_vertices = self.adjacency_list[vertex]

        # loop through each vertex from connected_vertices and delete the
        # link (edge) to the current vertex i.e. breaking the connection 
        for node in connected_vertices:
            self.adjacency_list[node].remove(vertex)
        
        # now delete the current vertex
        del self.adjacency_list[vertex]

        return True

    def get_starting_vertex(self):
        start_node = ""
        for node, _ in self.adjacency_list.items():
            start_node = node
            break
        return start_node

    def get_adjacencyvertices(self, vertex):
        return self.adjacency_list[vertex]



# g = Graph()
# print(g)
# g.add_vertex("A")
# g.add_vertex("B")
# g.add_vertex("C")
# # print(g)
# g.add_edge("A", "B")
# g.add_edge("A", "C")
# g.add_edge("B", "C")
# # g.add_edge("A", "C")
# print(g)
# g.remove_edge("A", "C")
# print(g)

# g.remove_vertex("C")
# print(g)