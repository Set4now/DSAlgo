class DSUnionByRank:
    def __init__(self, number_of_vertices) -> None:
        self.parents = [-1] * number_of_vertices
        self.rank = [0] * number_of_vertices

    def findparent(self, vertex_index):
        
        if self.parents[vertex_index] == -1:
            return vertex_index
        self.parents[vertex_index] = self.findparent(self.parents[vertex_index])
        return self.parents[vertex_index]

    def union(self, vertexa, vertexb):
        parentofvertexa = self.findparent(vertexa)
        parentofvertexb = self.findparent(vertexb)

        if parentofvertexa == parentofvertexb:
            print("Cycle detected between nodes {} --> {}".format(vertexa, vertexb))
            return False
        else:
            if self.rank[parentofvertexa] == self.rank[parentofvertexb]:
                self.parents[parentofvertexa] = parentofvertexb 
                self.rank[parentofvertexb] += 1
            else:
                if self.rank[parentofvertexa] > self.rank[parentofvertexb]:
                    self.parents[parentofvertexb] = parentofvertexa
             
                if self.rank[parentofvertexb] > self.rank[parentofvertexa]:
                    self.parents[parentofvertexa] = parentofvertexb
            print(self.parents)
            return True 
# detect cycle in undirected graph using disjoint set
def detectcycle(number_of_vertices, edges):
    disjointset = DSUnionByRank(number_of_vertices)
    # edges are like {{1}, {0, 2, 4}, {1, 3}, {2, 4}, {1, 3}} 
    # means 0 --> 1 | 1 --> [0,2,4] | 2 --> [1, 3] etc

    # creating a mapping and ignoring bidirectional edges
    # {0: [1], 1: [2, 4], 2: [3], 3: [4], 4: []
    vertex_edge_mapping = {vertex: [] for vertex in range(len(edges))}
    for vertex in range(len(edges)):
        for node in edges[vertex]:
            if vertex not in vertex_edge_mapping[node]:
                  vertex_edge_mapping[vertex].append(node)

    print(vertex_edge_mapping)
    for vertex, e in vertex_edge_mapping.items():
        for edge in e:
            print("vertex {} | edge {}".format(vertex, edge))
            if not disjointset.union(vertex, edge):
                return True
    return False

edges = [[1,2],[1,3],[2,3]]
edges = [[1], [0, 2, 4], [1, 3], [2, 4], [1, 3]]
#edges = [[], [2], [1, 3], [2]]
print(detectcycle(5, edges))


