"""
There are n computers numbered from 0 to n - 1 connected by ethernet cables connections 
forming a network where connections[i] = [ai, bi] represents a connection between computers ai and bi. 
Any computer can reach any other computer directly or indirectly through the network.

You are given an initial computer network connections. 
You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.

Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return -1.


Concepts to undestand


The idea is to find redundant edges in the Graph from existing connected component's 
which can be used to connect all other disconnected componenst to make a single component

Redundant edges:
An edge if removed , will not increase the number of components in the Graph


From concept of MST,
If there are N vertices, then we need (N - 1 ) edges to make the Graph one single component

Redudant edges in a Graoh = Total edges present in graph - ( N - 1), N is total number of vertices

So, If we have C components in a graph, then

Formula of Redudant edges in a Graph with more than 1 component.

Redudant edges = Total edges - ((N - 1) - (# of components - 1))

If Redudant edges >= (# of components - 1):
    return (# of components - 1) # This would be the answer
if total edges < (N - 1):
    You cannot create a single compoent
If Redudant edges < (# of components - 1):
    You cannot create a single compoent



"""

from typing import List
from collections import defaultdict


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        #edge case 1 
        num_of_edges = len(connections)

        if num_of_edges < (n - 1):
            return -1
        
        
        self.g = defaultdict(list)
        
        # creating an adjacency list (undirected or bidirectional)
        for n1,n2 in connections:
            self.g[n1].append(n2)
            self.g[n2].append(n1)
            
        
        # finding number of components
        num_of_components = 0
        
        visited = [False] * n
        for node in range(n):
            if not visited[node]:
                self.dfs(node, visited)
                num_of_components += 1
        
        # finding redundant edges in the graph
        redundant_edges = num_of_edges - ( (n -1 ) - ( num_of_components  - 1))
        
        
        if redundant_edges >=  num_of_components  - 1:
            return num_of_components  - 1
        
        if redundant_edges < num_of_components  - 1:
            return - 1
        
        
    def dfs(self, node, visited):
        visited[node] = True
        for edge in self.g[node]:
            if not visited[edge]:
                self.dfs(edge, visited)