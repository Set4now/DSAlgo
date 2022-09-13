from collections import defaultdict
from dis import dis
import heapq

class Dijkstars:
    def __init__(self) -> None:
        self.g = defaultdict(list)
        self.v = set()
    
    def add_edge(self, u, v, w):
        self.g[u].append((v, w))
        self.g[v].append((u, w))
        if u not in self.v:
            self.v.add(u)
        if v not in self.v:
            self.v.add(v)

    def get_shortest_path(self, src):

        h = [(0, src)]
        distance = {v: float("Inf") for v in self.v}
        distance[src] = 0

        visited = set()

        while h:
            weight, node = heapq.heappop(h)
            if node in visited:
                continue
            visited.add(node)
            for edge, edgeweight in self.g[node]:
                if edge not in visited:
                    if distance[node] + edgeweight < distance[edge]:
                        distance[edge] = distance[node] + edgeweight
                        heapq.heappush(h, (distance[edge], edge))

        return distance


d = Dijkstars()
d.add_edge("a", "b", 8)
d.add_edge("b", "c", 3)

d.add_edge("a", "d", 1)
d.add_edge("d", "b", 3)
d.add_edge("d", "c", 20)

print(d.get_shortest_path("a"))

        