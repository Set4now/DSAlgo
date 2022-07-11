from graph import Graph
from custom_queue import CustomQueue
# A handly Queue
class CustomQueue:
    def __init__(self) -> None:
        self.container = []

    def enque(self, key):
        self.container.append(key)

    def dequeue(self):
        popped = self.container[0]
        self.container.remove(self.container[0])
        return popped

    def isempty(self):
        return len(self.container) == 0

def bfstraversal(graph: Graph):
    """
    time complexity (O(V + E)) 
    Space: (V + E)
    
    type: Breadth first search (BFS) --> aka level order

    Algorithm: using Queue
    
    Get any starting vertex
    enque the startng node

    while queue is not empty:
        dequeue the vertex
        if vertex is not visited:
            enque all the unvisited adjacent vertices of it
    """
    # get any starting vertex
    start_node = graph.get_starting_vertex()
    q = CustomQueue() #create a Queue
    q.enque(start_node) # enque the starting vertex

    visited_nodes = [] # to track all tghe visited nodes

    while not q.isempty():
        node = q.dequeue() 
        if node not in visited_nodes: # only if its not visisted
            visited_nodes.append(node) # store it 
            adjacent_vertices = graph.get_adjacencyvertices(node) # get connected adjacency vertices
            for vertex in adjacent_vertices:
                if vertex not in visited_nodes:
                    q.enque(vertex) #enqueu all the unvisited vertices
    return visited_nodes


# print(bfstraversal(g))
# ['A', 'B', 'C', 'D', 'G', 'E', 'F']


def dfstraversal(graph: Graph):
    """
    time complexity (O(V + E)) 
    Space: (V + E)
    
    type: Depth first search (DFS) 

    Algorithm: using Stack
    
    Get any starting vertex
    push the startng node

    while stack is not empty:
        pop the current vertex
        if current vertex is not visited:
            push all the unvisited adjacent vertices of current vertex
    """
    # get any starting vertex
    start_node = graph.get_starting_vertex()
    stack = [] #create a stack
    stack.append(start_node) # push the starting vertex

    visited_nodes = [] # to track all tghe visited nodes

    while stack:
        node = stack.pop() 
        if node not in visited_nodes: # only if its not visisted
            visited_nodes.append(node) # store it 
            adjacent_vertices = graph.get_adjacencyvertices(node) # get connected adjacency vertices
            for vertex in adjacent_vertices:
                if vertex not in visited_nodes:
                    stack.append(vertex) #push all the unvisited vertices
    return visited_nodes
g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_vertex("E")
g.add_vertex("F")
g.add_vertex("G")
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("B", "G")
g.add_edge("C", "D")
g.add_edge("C", "E")
g.add_edge("E", "F")
g.add_edge("F", "D")
g.add_edge("F", "G")

print(dfstraversal(g))