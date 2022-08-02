
class Graph:
    def __init__(self) -> None:
        self.graph = {} # original adjacency list
        self.transposed_graph = {}
        self.vertices = []

    def add_edge(self, src, dest):
        if src not in self.graph:
            self.graph[src] = [dest]
        else:
            self.graph[src].append(dest)
        if src not in self.vertices:
            self.vertices.append(src)
        if dest not in self.vertices:
            self.vertices.append(dest)

    def dfs(self, node, visited, graph):
        visited[node] = True 
        if node in graph:
            for edge in graph[node]:
                if not visited[edge]:
                    self.dfs(edge, visited, graph)

    def transpose_graph(self):
        # creating another transposes_graph by reversing the edges
        for vertex in self.graph:
            for edge in self.graph[vertex]:
                if edge not in self.transposed_graph:
                    self.transposed_graph[edge] = [vertex]
                else:
                    self.transposed_graph[edge].append(vertex)

    def isconnected(self):
        """
        KOSARAJU ALGORITHM FOR CHECKING IF GRAPH IS SCC (Stronglely Connected Directed Graph)

        1. Peform a DFS using an arbitary vertex, if any node remains unvisited, means its not a SCC
        2. Transpose the graph by revering the edges
        3. Peform a 2nd DFS on the transposed_graph using the same arbitary vertex, return False if any node remains
           unvisited like step 1 
           else 
             return True


        The idea is, if every node can be reached from a vertex v, and every node can reach v, 
        then the graph is strongly connected. In step 2, we check if all vertices are reachable from v. 

        Kosaraju uses the fact that the SCC property of a graph remains Same even after 
        revering the edges.

        Note, start the DFS using only one vertex unlike we do normally in DFS 
        Since we are talking about strongley Connected characteristics, 
        All the nodes should be reacble from the start node if not then the G is not Connected

        """
        visited = {vertex: False for vertex in self.vertices}

        #peform DFS by selecting one random key 
        import random
        print(self.vertices)
        start_vertex = random.choice(self.vertices)

        self.dfs(start_vertex, visited, self.graph)
        
        print(visited)
        for vertex in visited:
            if not visited[vertex]:
                return False 

        
        # # transposing Graph
        self.transpose_graph()
        

        # making visited again False based on transposed
        visited = {vertex: False for vertex in self.vertices}
        self.dfs(start_vertex, visited, self.transposed_graph)

        for vertex in visited:
            if not visited[vertex]:
                return False 

        return True


# g1 = Graph()
# g1.add_edge(0, 1)
# g1.add_edge(1, 2)
# g1.add_edge(2, 3)
# g1.add_edge(3, 0)
# g1.add_edge(2, 4)
# g1.add_edge(4, 2)

# print(g1.isconnected())

g2 = Graph()
g2.add_edge(0, 1)
g2.add_edge(1, 2)
g2.add_edge(2, 3)
print(g2.isconnected())

###################

# Python program to check if a given directed graph is strongly
# connected or not GEEKS FOR GEEKS

# from collections import defaultdict

# # This class represents a directed graph using adjacency list representation


from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices # No. of vertices
        self.graph = defaultdict(list) # default dictionary to store graph
    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

	# A function used by isSC() to perform DFS
    def DFSUtil(self, v, visited):
        visited[v] = True
		# Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

	# Function that returns reverse (or transpose) of this graph
    def getTranspose(self):
        g = Graph(self.V)
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j, i)
        return g

	# The main function that returns true if graph is strongly connected
    def isSC(self):
		# Step 1: Mark all the vertices as not visited (For first DFS)
        visited =[False]*(self.V)
		
		# Step 2: Do DFS traversal starting from first vertex.
        self.DFSUtil(0,visited)

        print(visited)
		# If DFS traversal doesnt visit all vertices, then return false
        if any(i == False for i in visited):
            return False

		# Step 3: Create a reversed graph
        gr = self.getTranspose()

        # print(gr.graph)
		
		# Step 4: Mark all the vertices as not visited (For second DFS)
        visited =[False]*(self.V)

		# Step 5: Do DFS for reversed graph starting from first vertex.
		# Starting Vertex must be same starting point of first DFS
        gr.DFSUtil(0,visited)

        print(visited)

		# If all vertices are not visited in second DFS, then
		# return false
        if any(i == False for i in visited):
            return False
            
        return True

# Create a graph given in the above diagram
# g1 = Graph(5)
# g1.addEdge(0, 1)
# g1.addEdge(1, 2)
# g1.addEdge(2, 3)
# g1.addEdge(3, 0)
# g1.addEdge(2, 4)
# g1.addEdge(4, 2)
# print ("Yes" if g1.isSC() else "No")

# g2 = Graph(4)
# g2.addEdge(0, 1)
# g2.addEdge(1, 2)
# g2.addEdge(2, 3)
# print ("Yes" if g2.isSC() else "No")

# This code is contributed by Neelam Yadav



