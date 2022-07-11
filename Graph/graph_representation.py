from collections import namedtuple

Graph = namedtuple("Graph", ["nodes", "edges"])
nodes = ["A", "B", "C", "D", "E", "F", "G"]
edges = [
    ("A", "B"),
    ("A", "C"),
    ("B", "D"),
    ("B", "G"),
    ("C", "D"),
    ("D", "F"),
    ("C", "E"),
    ("E", "F"),
    ("F", "G")
]

def show_adjacency_list(graph):
    """
    Assumes that graph nodes are represented as string or objects 
    which are hashable
    
    {   
        'A': ['B', 'C'], 
        'B': ['D', 'G'],
        'C': ['D', 'E'], 
        'D': ['F'], 
        'E': ['F'], 
        'F': ['G'], 
        'G': []
    }
    """
    final_graph = {vertex: [] for vertex in graph.nodes}
    for edge in graph.edges:
        node1, node2 = edge[0], edge[1]
        final_graph[node1].append(node2)
    return final_graph

def show_adjacency_matrix(graph):
    """
    returns adjacency matrix representation

    Assumes that graph nodes are represented as integers
    """
    final_graph = [ [0] * len(graph.nodes) for vertex in graph.nodes]
    for edge in graph.edges:
        node1, node2 = edge[0], edge[1]
        final_graph[node1][node2] += 1
        final_graph[node2][node1] += 1
    return final_graph

graph = Graph(nodes, edges)
print(show_adjacency_list(graph))


nodes = range(4)
edges = [
    (0,1),
    (0,1),
    (0,2),
    (0,2),
    (0,3),
    (1,3),
    (2,3)
]
g = Graph(nodes, edges)
print(show_adjacency_matrix(g))