# https://leetcode.com/problems/course-schedule/submissions/
# https://practice.geeksforgeeks.org/problems/prerequisite-tasks/1
"""
The solution is related to topological sorting..
Topological sorting (dependencies ) is only possible if the grah is DAG

So our solution is to check if every connected components of graph if its DAG or NOT

Means if there is a cycle , then task's cannot be performed in order since cyclic dependencies present

Approachs
I. departure time , d(u) < d(v) where v is already visited, means back edge, means cycle
2. Union Find
3. DFS
 We use a vector visited to record all the visited nodes and 
 another vector onpath to record the visited nodes of the current DFS visit. 
 Once the current visit is finished, we reset the onpath value of the starting node to false

"""

class Solution:
    def isPossible(self,N,prerequisites):
        graph = {}
        for ( node1, node2 ) in prerequisites:
            if node1 not in graph:
                graph[node1] = [node2]
            else:
                graph[node1].append(node2)
        if not self.isdag(graph):
            return True
        return False  

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
                    return False # means it has a back edge
        return True

# N = 4 
# prerequisites  = [[1,0],[2,1],[3,2]]


# N = 2
# prerequisites = [[1,0],[0,1]]



N = 20
prerequisites = [[0, 10], [3, 18] , [5, 5], [6 ,11], [11, 14 ],[13, 1], [15,1] , [17, 4]]

            
s = Solution()
print(s.isPossible(N, prerequisites))