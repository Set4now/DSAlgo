'''
Given a directed graph. 
The task is to do Breadth First Traversal of this graph starting from 0.

Note: One can move from node u to node v only if there's an edge from u to v and 
find the BFS traversal of the graph starting from the 0th vertex, 
from left to right according to the graph. 

Also, you should only take nodes directly or indirectly connected from Node 0 in consideration.
'''

from collections import namedtuple
Graph = namedtuple("Graph", ["nodes", "edges"])


class GraphQueue:
    def __init__(self) -> None:
        self.queue = [] 
    
    def enque(self, vertex):
        self.queue.append(vertex)

    def deque(self):
        popedvertex = self.queue[0]
        del self.queue[0]
        return popedvertex

    def isempty(self):
        return len(self.queue) == 0

class BFSGraph:

    def __init__(self, g: Graph) -> None:
        self.vertices = g.nodes
        self.edges = g.edges
        self.vertex_adjacent_edges = self._vertices_edge_mapper()

    def _vertices_edge_mapper(self):
        mapping = {}
        if self.edges:
            for edge in self.edges:
                node1 = edge[0]
                node2 = edge[1]
                if node1 not in mapping:
                    mapping[node1] = [node2]
                else:
                    mapping[node1].append(node2)
        else:
            mapping[self.vertices[0]] = []
        print(mapping)
        return mapping

    def bfs(self, src):
        "BFS Traversal using queue"
        output = []
        already_visited = []
        queue = GraphQueue()
        queue.enque(src)
        while not queue.isempty():
            poppedvertex = queue.deque()
            if poppedvertex not in already_visited:
                already_visited.append(poppedvertex)
                output.append(poppedvertex)
                if poppedvertex in self.vertex_adjacent_edges:
                    if self.vertex_adjacent_edges[poppedvertex]:
                        for edge in self.vertex_adjacent_edges[poppedvertex]:
                            if edge not in already_visited:
                                queue.enque(edge)
        return output

    def dfs(self, src):
        """DFS using Stack"""
        stack = []
        stack.append(src)
        output = []
        visited = []
        while stack:
            print(stack)
            popped = stack.pop()
            print(popped)
            if popped not in visited:
                output.append(popped)
                visited.append(popped)
            if popped in self.vertex_adjacent_edges:
                if self.vertex_adjacent_edges[popped]:
                    for edge in self.vertex_adjacent_edges[popped]:
                        if edge not in visited:
                            stack.append(edge)
        return output

######### Test Cases #############
# edge case where there is only single node
# nodes = range(1) # 0
# edges = []
# # output shuld be [0]

# # Normal case
# nodes = range(5)
# edges = [
#     (0, 1),
#     (0, 2),
#     (0, 3),
#     (2, 4)
# ]
# # output should be [0, 1, 2, 3, 4]
# g = Graph(nodes, edges)
# mygraph = BFSGraph(g)
# print(mygraph.bfs(0))
#########################################

######### DFS Test case ##########
# nodes = range(6)
# edges = [
#     (0, 1),
#     (0, 2),
#     (1, 2),
#     (1, 3),
#     (2, 3),
#     (3, 4),
#     (4, 0),
#     (4, 1),
#     (4, 5)
# ]
# # output should be [0, 1, 2, 3, 4]
# g = Graph(nodes, edges)
# mygraph = BFSGraph(g)
# # print(mygraph.bfs(0))

# print(mygraph.dfs(0))
## 0, 2, 3, 4, 5, 1]
#########################################

"""
Trasitive closure (Connected Matrix) for a Directed Graph (G) repesented with a 2D Array

Connected Matrix where each G[i][j] = 1
if there is a direct path btw i --> j either direct or via another vertex i --> k --> j

if there is no path , then G[i][j] = 0

Everynode to itself can be reprented as 1

input_graph = 
  0   1  2  3
0 [1, 0, 1, 0],
1 [1, 1, 0, 0],
2 [0, 0, 1, 0],
3 [0, 1, 0, 1]

"""

class CustomGraph:
    def __init__(self, input_graph) -> None:
        self.input_graph = input_graph
        self.num_of_vertices = len(input_graph)
        self.adjacency_list = self.create_adjacentlist() # {0: [2], 1: [0], 3: [1]}

    def create_adjacentlist(self):
        vertex_edge_list = {}
        for i in range(len(self.input_graph)):
            for j in range(len(self.input_graph[i])):
                # don't do any thing for self loop egdes
                # [0][0] , keep it as 1 as input graph
                if i != j:
                    if  self.input_graph[i][j] == 1:
                        if i not in vertex_edge_list:
                            vertex_edge_list[i] = [j]
                        else:
                            vertex_edge_list[i].append(j)
        # {0: [2], 1: [0], 3: [1]}
        return vertex_edge_list

    def dfs(self, root, child, connectivity_matrix):
        ''' 
        eg A --> B --> C --> D
        [A][B] = 1, 
        [A][C] = 1
        [A][D] = 1
        '''
        if connectivity_matrix[root][child] == 0:
            connectivity_matrix[root][child] = 1
        if child in self.adjacency_list:
            # recursively using a DFS approach
            # updating [parent][all nested child] = 1
            for childedge in self.adjacency_list[child]:
                self.dfs(root, childedge, connectivity_matrix)

    def show_connectivity_matrix(self):
        """
        Using a DFS approach

        1. Create an ajacency list dict from the input graph
        where key is vertex and value is list of edges
        
        eg. 

        input graph:-
        [
            [1, 0, 1, 0],
            [1, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 1, 0, 1]
        ]
        
        ajacency list dict will be {0: [2], 1: [0], 3: [1]}
        NOTE: a vertex to itself is always 1, we are considering it's own path is always 1 (reachble) 
        this already 1 as you can see in the input graph

        G[0][0] = 1, G[1][1] = 1.... means the diagonal is always 1

        see create_adjacentlist()

        2. Now use a DFS appoach
        for every node in ajacency list dict
            consider it as parent root node
            all its edges as child
            so connectivity matrix (result) will have

            connectivity_matrix[parent][child] = 1

            also, the parent will be same for the nested childs of current child as well

            eg A --> B --> C --> D

            here, A is parent, its child is B
            B' child is C
            C' child is D

            So, keep updating the result connectivity_matrix[parent][allchilds] = 1
            [A][B] = 1, 
            [A][C] = 1
            [A][D] = 1
        
        """
        # create a copy of the input graph, we will keep the input graph as it as
        connectivity_matrix =[i[:] for i in  self.input_graph]

        # iterate on all the vertices
        for node in self.adjacency_list:
            root = node
            descendants = self.adjacency_list[root]
            # same for its edges
            for child in descendants:
                self.dfs(root, child, connectivity_matrix)
        return connectivity_matrix

    def show_connectivity_matrix_anotherapproach(self):
        # its is verty similar to FLoyd Warshall law
        # but instead of finding shortest path pair , we are just check
        # if there is any path btw(i to j ) through all the intermittent vertices 

        # create a copy of the input graph, we will keep the input graph as it as {0, 1, 2, .. k}

        """
        The core idea behind Warshall’s algorithm is that a path exists between two pairs of vertices i, j if and only if there is an edge from i to j, 
        or any of the following conditions is true:

        There is a path from i to j going through vertex 1.
        There is a path from i to j going through vertex 1 and/or 2.
        There is a path from i to j going through vertex 1, 2, and/or 3.
        There is a path from i to j going through any other vertices.

        Easy to code then the DFS approach
            
        """
        connectivity_matrix =[i[:] for i in  self.input_graph]
        for k in range(self.num_of_vertices):
            for i in range(self.num_of_vertices):
                for j in range(self.num_of_vertices):
                  connectivity_matrix[i][j] = connectivity_matrix[i][j] or ( connectivity_matrix[i][k] and connectivity_matrix[k][j])
        return connectivity_matrix

sampleg = [
    [1, 0, 1, 0],
    [1, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 1, 0, 1]
    ]
 
g = CustomGraph(sampleg)
print(g.show_connectivity_matrix())
# [[1, 0, 1, 0], [1, 1, 1, 0], [0, 0, 1, 0], [1, 1, 1, 1]]
print(g.show_connectivity_matrix_anotherapproach())
# [[1, 0, 1, 0], [1, 1, 1, 0], [0, 0, 1, 0], [1, 1, 1, 1]]
    
    
