import json
from string import printable


class Graph:
    """
    add edge with weight (A, B, 2)
    distance = {"node1": float('inf'), "node2": float('inf')}
    final_path = []

    graph = {
        "A": [("B", 2), ("C", 1)]
        A -- 2 --> B
        |
        1
        |
        C
    }
    
    """
    def __init__(self) -> None:
        self.graph = {}
        self.shorted_distance = {}
        self.visited = set()
        self.shortest_paths = {}

    def __repr__(self) -> str:
        return json.dumps(self.graph )

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
            self.shorted_distance[vertex] = float('inf')
    
    def add_edge(self, src, dest, distance):
        if src in self.graph and dest in self.graph:
            self.graph[src].append((dest, distance))
            self.graph[dest].append((src, distance))
            self.shortest_paths[src] = []
            self.shortest_paths[dest] = []

    def _get_all_sssp(self, source):
        """
         Dijkstras Algorithm

        """
        # get adjacent nodes of source
        nodes = self.graph[source]

        # calculate distance of each adjacent nodes which are not visited and update them
        for node in nodes:
            # node = ["B", 2] where 2 is the distance 
            if node not in self.visited:
                distance = self.shorted_distance[source] + node[1]
                if distance < self.shorted_distance[node[0]]:
                    # keeping a track of the parent to later show the actual paths
                    self.shortest_paths[node[0]].append(source)

                    # updating the new distance
                    self.shorted_distance[node[0]] = distance

        minimum = float('inf')
        nextnode = ""
        # find the next node among all the remaing unvisited with shorted distance 
        for node, distance in self.shorted_distance.items():
            if node not in self.visited:
                if distance < minimum:
                    nextnode = node
                    minimum = distance
       
        # when you have reached the last node,
        # means all the other vertices are already selected with calculated shortest path
        # so, nextnode is not updated and remain as "" , stop recursion
        if nextnode != "":

            self.visited.add(nextnode)
            self._get_all_sssp(nextnode)

    def show_shortest_path(self, source, destination):
        """
         this shows the actual path from source to destination
         
         whenever we update the shortest distance, we also keep track of the
         parent node to the current node

         then traverse the chain until we find the source whose parent will be always empty
         for example here c is the source, D is the destination 
         'A': ['C'], 'B': ['C'], 'C': [], 'E': ['B'], 'D': ['B'], 'F': ['C'], 'G': ['F']}
        

         so we basically back track from the destination to src , to get the path
         path = destination...src

         then reverse the path to get src...dest
         so the return value is 
         C-->B-->D

        """
        self.get_all_sssp(source)
        path = [destination]
        # print(self.shortest_paths[destination][0])
        node = self.shortest_paths[destination][0]
        while node:
            path.append(node)
            if not self.shortest_paths[node]:
                break
            else:
                node = self.shortest_paths[node][0]
        return "-->".join(path[::-1])
        
    def get_all_sssp(self, source):
         # the start origin disance is always 0
        self.shorted_distance[source] = 0
        self.visited.add(source)
        self._get_all_sssp(source)
        return self.shorted_distance

            
g = Graph()
# g.add_vertex("A")
# g.add_vertex("B")
# g.add_vertex("C")
# g.add_vertex("D")
# g.add_vertex("E")
# g.add_vertex("F")
# g.add_vertex("G")

# g.add_edge("A", "B", 2)
# g.add_edge("A", "C", 5)
# g.add_edge("B", "E", 3)
# g.add_edge("B", "D", 1)
# g.add_edge("B", "C", 6)
# g.add_edge("D", "E", 4)
# g.add_edge("C", "F", 8)
# g.add_edge("F", "G", 7)
# g.add_edge("E", "G", 9)
# # print(g)
# # print(g.get_all_sssp("C"))

# print(g.show_shortest_path("A", "C"))


g.add_vertex("hit")
g.add_vertex("hot")
g.add_vertex("dot")
g.add_vertex("lot")
g.add_vertex("log")
g.add_vertex("dog")
g.add_vertex("cog")

g.add_edge("hit", "hot", 1)
g.add_edge("hot", "dot", 1)
g.add_edge("hot", "lot", 1)
g.add_edge("dot", "lot", 1)
g.add_edge("lot", "log", 1)
g.add_edge("dot", "dog", 1)
g.add_edge("dog", "log", 1)
g.add_edge("dog", "cog", 1)
g.add_edge("log", "cog", 1)
# print(g)
# print(g.get_all_sssp("C"))

print(g.show_shortest_path("hit", "cog"))

    
