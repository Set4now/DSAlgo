"""
Ford-Fulkerson Algorithm for Maximum Flow Problem


Given a graph which represents a flow network where every edge has a capacity. 
Also given two vertices source ‘s’ and sink ‘t’ in the graph, find the maximum possible flow from s to t with following constraints:

Flow on an edge doesn’t exceed the given capacity of the edge.
Incoming flow is equal to outgoing flow for every vertex except s and t.


Ford-Fulkerson Algorithm 

Start with initial flow as 0.
While there is a augmenting path from source to sink. 
Add this path-flow to flow.
Return flow.

"""


class Graph:
    def __init__(self, g) -> None:
        self.graph = g


    def bfs(self, src, sink, parent_array):
        visited = {v: False for v in range(len(self.graph))}
        queue = []
        
        queue.append(src)
        visited[src] = True

        while queue:
            popped = queue.pop(0)
            # enumerate(self.graph[popped]) will give edge values for each adjacent edges for the source
            for source, edgevalue in enumerate(self.graph[popped]):
                # edgevalue > 0 means as long as the residual capacity doesn't become 0, there is a path
                if visited[source] == False and edgevalue > 0:
                    parent_array[source] = popped
                    queue.append(source)
                    visited[source] = True

                    # if you reach the destination which is sink, then return True
                    if source == sink:
                        return True

        # if you cannot reach the destination which is sink, then return False
        # means there is no path
        return False

    def ford_fulkerson(self, src, sink):
        parent_array = [-1] * len(self.graph)
        max_flow = 0

        while self.bfs(src, sink, parent_array):
            dest = sink

            # getting path flow which is the min flow in the path
            # min weight / capacity among all the edges in the path
            path_flow = float("Inf") 
            while dest != src: # backtrack until we reach from destination to src
                path_flow = min(path_flow, self.graph[parent_array[dest]][dest]) # flow from current node to its parent 
                dest = parent_array[dest] #update with parent

            # adding the path flow for each path to the max_flow which is the final ans
            max_flow += path_flow

            # Augmenting the path (residula graph)
            dest = sink
            while dest != src:
                parent = parent_array[dest]
                self.graph[parent][dest] -= path_flow
                self.graph[dest][parent] += path_flow
                dest = parent

        return max_flow
            
graph = [[0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]]

graph = [[0, 8, 0, 0, 3, 0],
         [0, 0, 9, 0, 0, 0],
         [0, 0, 0, 0, 7, 2],
         [0, 0, 0, 0, 0, 5],
         [0, 0, 7, 4, 0, 0],
         [0, 0, 0, 0, 0, 0]]
g = Graph(graph)
 
source = 0; sink = 5
print(g.ford_fulkerson(source, sink))


