from collections import namedtuple
import random


Graph = namedtuple("Graph", ["nodes", "edges"])

nodes = ["A", "B", "C", "D", "E"]
edges = {
    ("A", "B"): 10,
    ("B", "A"): 10,
    ("A", "C"): 20,
    ("C", "A"): 20,
    ("B", "D"): 5,
    ("D", "B"): 5,
    ("B", "C"): 30,
    ("C", "B"): 30,
    ("D", "C"): 15,
    ("C", "D"): 15,
    ("D", "E"): 8,
    ("E", "D"): 8,
    ("E", "C"): 6,
    ("C", "E"): 6,
}
g = Graph(nodes, edges)

def calculate_weight(src, nodes_edges_list, weight_of_vertices, selected_path_mst, already_visted_nodes):
    vertex_list_of_edges = nodes_edges_list[src]

    #edge case to check if it has got any edges or not
    if vertex_list_of_edges:
        for edge in vertex_list_of_edges:
            node, cost = edge[0], edge[1]
            if node not in already_visted_nodes:
                if cost < weight_of_vertices[node]:
                    # update weight if cost is less than current weight
                    # initial weight is always infinity
                    weight_of_vertices[node] = cost

    # select next non-visited node which got the min weight 
    next_node_with_lowest_weight = ""
    min_weight = float("Inf")
    for vertex, weight in weight_of_vertices.items():
        if vertex not in already_visted_nodes:
            if weight < min_weight:
                min_weight = weight
                next_node_with_lowest_weight = vertex

    if next_node_with_lowest_weight != "":
        already_visted_nodes.append(src)
        if next_node_with_lowest_weight not in selected_path_mst:
            selected_path_mst.append(next_node_with_lowest_weight)
        calculate_weight(next_node_with_lowest_weight, nodes_edges_list, weight_of_vertices, selected_path_mst, already_visted_nodes)


def findmstwithprims(g: Graph, src=None):

    """
    
    Algorithm

    It finds MST with lower cost / weight in a Graph

    1. Select a src vertex
    2. get its adjacency edges
    3. Update each adjacency edge's weight if needed
       if cost(src, edgenode) < current weight of edgenode:
            current weight of edgenode = cost(src, edgenode)
    4. Select the next non-visited node which got the min weight and make the current src as visited
    5. Recursive call the same function until you reach the last node
          

    """
    vertices = set()

    # Keeping a list of all vertices
    for edge in g.edges:
        # print(type(edge))
        # print(edge[0], edge[1])
        node1, node2 = edge[0], edge[1]
        # print(node1, node2)
        vertices.add(node1)
        vertices.add(node2)


    # creating a list of adjacent vertices (edges) with cost of each vertex for easy tracking
    # {"A": [(B, 10), (..)], "B": [(A, 10), (..)]}
    nodes_edges_list = {}
    for edge, cost in g.edges.items():
        node1, node2 = edge[0], edge[1]
        if node1 not in nodes_edges_list:
            nodes_edges_list[node1] = [(node2, cost)]
        else:
            nodes_edges_list[node1].append((node2, cost))

    # choose a starting vertex randomly if not given
    #src_vertex = src if src else random.choice(list(vertices))
    src_vertex = "A"

    # initial weights of vertices as infinity except source vertex
    weight_of_vertices = { vertex: float('Inf') for vertex in vertices}
    weight_of_vertices[src_vertex] = 0

    selected_path_mst = [src_vertex]

    already_visted_nodes = []

    calculate_weight(src_vertex, nodes_edges_list, weight_of_vertices, selected_path_mst, already_visted_nodes)

    print(selected_path_mst)
    return weight_of_vertices

print(findmstwithprims(g))
#['A', 'B', 'D', 'E', 'C']
#{'C': 6, 'B': 10, 'A': 0, 'D': 5, 'E': 8}
    






    
