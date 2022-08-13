from collections import defaultdict 

class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)
        self.startvertices = []
        self.dependencies = []

    def addedge(self, vertex, edge):
        # we are also maintaing a list of dependencies 
        # and start vertices which are not dependent on anything
        if vertex not in self.startvertices and vertex not in self.dependencies:
            self.startvertices.append(vertex)
        self.graph[vertex].append(edge)
        if edge not in self.dependencies:
            self.dependencies.append(edge)
    
    def helper(self, vertex, visited, stack):
        visited.append(vertex)
        stack.append(vertex)
        return visited, stack

    def recursive(self,  vertex, visited, stack):
        if vertex in self.graph:
            edges =  self.graph[vertex]
            for edge in edges:
                if edge not in visited:
                    self.recursive(edge, visited, stack)
            else:
               self.helper(vertex, visited, stack) 
        else:  
            self.helper(vertex, visited, stack)

    def toposort(self):
        visited = []
        stack = []
        # print(self.graph)
        # print(self.startvertices)
        for startvertex in self.startvertices:
            self.recursive(startvertex, visited, stack)
        #self.recursive("A", visited, stack)

        # since its list representation of stack
        # the last inserted is at the last
        # so a topological order of preference is just the opposite of it
        # the dependency order

        # ['H', 'G', 'F', 'E', 'C', 'A', 'D', 'B']
        # to 
        # ['B', 'D', 'A', 'C', 'E', 'F', 'G', 'H']
        return stack[::-1]

g = Graph()
g.addedge("A", "C")
g.addedge("C", "E")
g.addedge("E", "H")
g.addedge("E", "F")

g.addedge("B", "D")
g.addedge("B", "C")
g.addedge("D", "F")
g.addedge("F", "G")

print(g.toposort())