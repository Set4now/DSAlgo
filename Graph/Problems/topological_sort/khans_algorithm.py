from collections import defaultdict


class Graph:
    def __init__(self) -> None:
        self.g = defaultdict(list)
        self.v = set()
        self.indegree = {}

    def addedge(self, u, v):
        self.g[u].append(v)
        self.v.add(u)
        self.v.add(v)
        if u not in self.indegree:
            self.indegree[u] = 0
        if v not in self.indegree:
            self.indegree[v] = 1
        else:
            self.indegree[v] += 1

    def khans_topological_sort(self):
        q = []

        for v in self.indegree:
            if self.indegree[v] == 0:
                q.append(v)

        visited = []
        while q:
            node = q.pop(0)
            visited.append(node)
            for edge in self.g[node]:
                self.indegree[edge] -= 1
                if self.indegree[edge] == 0:
                    q.append(edge)

        return visited

g = Graph()
g.addedge("bread", "yeast")
g.addedge("bread", "flour")

g.addedge("sandwitch", "bread")
g.addedge("sandwitch", "meat")


g.addedge("burger", "sandwitch")
g.addedge("burger", "meat")
g.addedge("burger", "bread")

g.addedge("icecream", "flour")
g.addedge("icecream", "cream")

print(g.khans_topological_sort())