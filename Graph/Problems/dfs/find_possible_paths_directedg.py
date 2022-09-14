"""
Possible paths between 2 vertices

Given a Directed Graph having V nodes numbered from 1 to V, and E directed edges. 
Given two nodes, source and destination, count the number of ways or paths between these two vertices in the directed graph. These paths should not contain any cycle.
Note: Graph doesn't contain multiple edges, self-loop, and cycles.


"""

class Solution:
    
    #Function to count paths between two vertices in a directed graph.
    def countPaths(self, V, adj, source, destination):
        graph = {v: [] for v in range(V)}
        for (src, dest) in adj:
            if src in graph:
                graph[src].append(dest)
            else:
                graph[src] = [dest]

        totalpaths = []
        stackpath = []
        pathcount = 0

        self.dfs(source, destination, stackpath, totalpaths, graph)
        print(totalpaths)
        return len(totalpaths)

    
    def dfs(self, node, destination, stackpath, totalpaths, graph):
        stackpath.append(node)
        if node == destination:
            # temp = [path for path in stackpath]
            # for path in stackpath:
            #     temp.append(path)
            totalpaths.append([path for path in stackpath])
            #stackpath.pop()
            return 
        if graph[node]:
            for edge in graph[node]:
                self.dfs(edge, destination, stackpath, totalpaths, graph)

        stackpath.pop()
        

V = 5
#E = 7
edges = [[0,1], [0,2], [0,4], [1,3], [1,4], [2,4], [3,2]]
source = 0
destination = 4


V = 4
#E = 7
edges = [[0,1], [0,3], [1,2], [1,3], [2, 3]]
source = 0
destination = 3

s = Solution()
print(s.countPaths(V, edges, source, destination))