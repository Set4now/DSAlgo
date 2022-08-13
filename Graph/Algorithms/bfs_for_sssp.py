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

import json
class Graph:
    def __init__(self) -> None:
        self.graph = {}

    def __repr__(self) -> str:
        return json.dumps(self.graph)

    def add_edge(self, vertex, edge):
        if vertex in self.graph:
            self.graph[vertex].append(edge)
        else:
            self.graph[vertex] = [edge]

    def bfs(self, startvertex):
        # level order using Queue 
        visited = []
        from_vertex = {} # here we store each vertex and its parent vertex
        c = CustomQueue() 
        c.enque(startvertex)
        from_vertex[startvertex] = None
        while not c.isempty():
            popped = c.dequeue()
            if popped not in visited:
                visited.append(popped)
            if popped in self.graph:
                for edge in self.graph[popped]:
                    if edge not in visited:
                        if edge not in from_vertex:
                            from_vertex[edge] = popped
                        c.enque(edge)
        return from_vertex

    def recursivepathfind(self, prevsource, destination):
        # we backtrack from destination to source with the help 
        # of parent
        currentvertex = prevsource[destination]
        paths = [destination]
        while currentvertex is not None:
            paths.append(currentvertex)
            pre = prevsource[currentvertex]
            currentvertex = pre
        return paths[::-1]

    def getpath(self, source, destination):
        from_vertex = self.bfs(source)
        return self.recursivepathfind(from_vertex, destination)

g = Graph()
g.add_edge("A", "B")
g.add_edge("A", "C")

g.add_edge("B", "D")
g.add_edge("B", "G")

g.add_edge("C", "E")
g.add_edge("C", "D")

g.add_edge("D", "F")
g.add_edge("E", "F")

g.add_edge("G", "F")
# print(g)
print(g.getpath("A", "G"))