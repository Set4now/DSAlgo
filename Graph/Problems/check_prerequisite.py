class Solution:
    def isPossible(self,N,prerequisites):
        graph = {}
        for ( node1, node2 ) in prerequisites:
            if node1 not in graph:
                graph[node1] = [node2]
            else:
                graph[node1].append(node2)
        if self.isdag(graph):
            return False
        return True  

    def dfs_calculate_depart_time(self, node, visited, time, departure, graph):
        if node not in visited:
            visited.add(node)
        
        if node in graph and graph[node]:
            for edge in graph[node]:
                if edge not in visited:
                    time = self.dfs_calculate_depart_time(edge, visited, time, departure, graph)
        
        # setting departure tme after visiting all adjacent nodes , back tracking 
        departure[node] = time
        time = time + 1
        return time 

    def isdag(self, graph):
        visited = set()
        departure = {vertex: None for vertex in graph}

        # initial time 
        time = 0
        
        for vertex in graph:
            if vertex not in visited:
                time = self.dfs_calculate_depart_time(vertex, visited, time, departure, graph)

        # check if the given directed graph is DAG or not
        for vertex in graph:
            for edge in graph[vertex]:
                # If the departure time of vertex `v` is greater than equal
                # to the departure time of `u`, they form a back edge.
    
                # Note that `departure[u]` will be equal to `departure[v]`
                # only if `u = v`, i.e., vertex contain an edge to itself
                if departure[vertex] <= departure[edge]:
                    return True
        return False

# N = 4 
# prerequisites  = [[1,0],[2,1],[3,2]]


# N = 2
# prerequisites = [[1,0],[0,1]]



N = 20
prerequisites = [[0, 10], [3, 18] , [5, 5], [6 ,11], [11, 14 ],[13, 1], [15,1] , [17, 4]]

            
s = Solution()
print(s.isPossible(N, prerequisites))