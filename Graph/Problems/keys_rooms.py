from collections import defaultdict
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        self.g = defaultdict(list)
        total_nodes = len(rooms)
        
        for i in range(len(rooms)):
            for node in rooms[i]:
                if node != i:
                    self.g[i].append(node)
                
        visited = set()
        #visited.add(0)
        
        self.dfs(0, visited)
        # print(visited)
        if len(visited) != total_nodes:
            return False
        return True
        
    
    def dfs(self, node, visited):
        visited.add(node)
        for edge in self.g[node]:
            if edge not in visited:
                self.dfs(edge, visited)

s = Solution()
rooms = [[1,3],[3,0,1],[2],[0]]
print(s.canVisitAllRooms(rooms))