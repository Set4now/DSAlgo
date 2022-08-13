"""
Given a Undirected Graph with V vertices and E edges, 
Find the level of node X. if X does not exist in the graph then print -1

"""

class Solution:
    
    #Function to find the level of node X.
    def nodeLevel(self, V, adj, X):
        # code here
        #print(adj)
        queue = []
        visited = set()
        queue.append(0)
        level = 0
        
        while queue:
            temp = []
            while queue:
                temp.append(queue[0])
                del queue[0]
                
            if X in temp:
                return level
            else:
                level += 1
            for node in temp:
                if node not in visited:
                    visited.add(node)
                    if adj[node]:
                        for edge in adj[node]:
                            if edge not in visited:
                                queue.append(edge)
            temp = []   
            
        return -1 