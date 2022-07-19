#https://leetcode.com/problems/redundant-connection/
from typing import List


class DSUnionByRank:
    def __init__(self, edges) -> None:
        self.parents = {}
        self.rank = self.settingranks(edges)

    def settingranks(self, edges):
        ranks = {}
        for edgelist in edges:
            for node in edgelist:
                if node not in ranks:
                    ranks[node] = 0
        return ranks
            
    def findparent(self, vertex_index):
        parentvertex = self.parents.get(vertex_index, vertex_index) # the 2nd arg is default if key not found 
        if parentvertex != vertex_index:
            parentvertex = self.findparent(parentvertex)
        return parentvertex


    def union(self, vertexa, vertexb):
        parentofvertexa = self.findparent(vertexa)
        parentofvertexb = self.findparent(vertexb)

        if parentofvertexa == parentofvertexb:
            # print("Cycle detected between nodes {} --> {}".format(vertexa, vertexb))
            return False
        else:
            if self.rank[parentofvertexa] == self.rank[parentofvertexb]:
                self.parents[parentofvertexa] = parentofvertexb 
                self.rank[parentofvertexb] += 1
            else:
                if self.rank[parentofvertexa] > self.rank[parentofvertexb]:
                    self.parents[parentofvertexb] = parentofvertexa
             
                if self.rank[parentofvertexb] > self.rank[parentofvertexa]:
                    self.parents[parentofvertexa] = parentofvertexb
            #print(self.parents)
            return True 

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        disjointset = DSUnionByRank(edges)
        finalresult = []
        for edgelist in edges:
            node1, node2 = edgelist[0], edgelist[1]
            if not disjointset.union(node1, node2):
                finalresult = edgelist
        return finalresult

edges = [[1,2],[1,3],[2,3]]
edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
s= Solution()
print(s.findRedundantConnection(edges))