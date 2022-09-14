from collections import defaultdict
from typing import List

"""
Network Delay Time


You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.


The solution is to find the max of ( min distance or time  of all the vertices from the src)
This will ultimately give the min distance to travel to the last node

Aproaches:
1. BFS (V+E)
2. Dijkstras (V*V) or VLogE (using Binary Heap)


"""

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        self.distance = {i: float("Inf") for i in range(1, n+1)}
        self.distance[k] = 0

        self.g = defaultdict(list)
        for u,v,w in times:
            self.g[u].append((v,w))

        # using BFS with Queue 
        #return self.bfs()

        processed = set()
        processed.add(k)

        self.dijkstras_shortest_path(k, processed)
        return self.get_min_time()




    def bfs(self):
        q = []
        q.append((k,0))
        
        # using BFS technique
        # Keep updating the distance map where we store the min distance from source k to the current node
        while q:
            src, srcdist = q.pop(0)
            
            for dest,time in self.g[src]:
                dest_time = srcdist + time

                #only update if the current distance from current src is min from the already stored distance
                if dest_time <  self.distance[dest]:
                    self.distance[dest] = dest_time
                    q.append((dest, dest_time))

        return self.get_min_time()


    def get_min_time(self):
        "Utility Function to return the max of min distance or time of all the vertices from the src"
        final_min_time = 0
        #return the max val from the distance dictionry
        for node in self.distance:
            if self.distance[node] > final_min_time:
                final_min_time = self.distance[node]
        
        # if all nodes are not reachable , then its distance will not be updated from "Inf"
        # return -1 , means the signal can't reach all the node
        if final_min_time == 0 or final_min_time == float("Inf"):            
            return -1
        return final_min_time 

    def dijkstras_shortest_path(self, src, processed):

        for dest, distance in self.g[src]:
            if dest not in processed:
                current_dest_distance = self.distance[src] + distance
                if current_dest_distance < self.distance[dest]:
                    self.distance[dest] = current_dest_distance
        
        next_min_distance_node = None
        min_distance = float("Inf")

        for node in self.distance:
            if node not in processed:
                if self.distance[node] < min_distance:
                    min_distance = self.distance[node]
                    next_min_distance_node = node 
        if next_min_distance_node:
            processed.add(next_min_distance_node)
            self.dijkstras_shortest_path(next_min_distance_node, processed)



times = [[1,2,1],[2,3,1],[2,4,2],[1,5,1]]
n = 5
k = 1

s = Solution()
print(s.networkDelayTime(times, n, k))