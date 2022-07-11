from collections import namedtuple
import json

Graph = namedtuple("Graph", ["nodes", "edges"])

class DisJointSet:
    '''This is the naive implementation
       Undirected graph
    '''
    def __init__(self, graph: Graph) -> None:
        self.parents = [-1] * len(graph.nodes)
        self.edges = []

    def __repr__(self) -> str:
        return json.dumps(self.parents)

    def findparentroot(self, node):
        if self.parents[node] == -1:
            return node
        else:
            return self.findparentroot(self.parents[node])

    def checksameSet(self, node1, node2):
        return self.findparentroot(node1) == self.findparentroot(node2)
    
    def union(self, node1, node2):
        if not self.checksameSet(node1, node2):
            parentofnode1 = self.findparentroot(node1)
            parentofnode2 = self.findparentroot(node2)
            self.parents[parentofnode1] = parentofnode2
        else:
            print("Cycle detected! | {} - {}".format(node1, node2))
            return False
nodes = range(4)
edges = [
    (0,1),
    (0,3),
    (2,3),
    (1,2),
]
g = Graph(nodes, edges)

# ds = DisJointSet(g)
# print(ds.findparentroot(3))

# print(ds.union(0, 1))
# print(ds.union(0, 3))
# print(ds.union(2, 3))
# print(ds.union(1, 2))
# print(ds)

class DisjointSetsByRank:
    def __init__(self, graph: Graph) -> None:
        self.parent = [-1] * len(graph.nodes)
        self.rank = [0] * len(graph.nodes)

    def __repr__(self) -> str:
        return json.dumps(self.rank)

    def findParent(self, node):
        if self.parent[node] == -1:
            return node
        self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        parentofnode1 = self.findParent(node1)
        parentofnode2 = self.findParent(node2)
        if parentofnode1 != parentofnode2:
            if self.rank[node1] == self.rank[node2]:
                # pointing Absolute parent of node 1 to node 2 and increasing rank of parentofnode2 by +1
                self.parent[parentofnode1] = parentofnode2
                self.rank[parentofnode2] += 1
            else:
                # smaller ranking absolute parent should point to larger rank aboslute parent
                # No need to change Rank
                if self.rank[parentofnode1] > self.rank[parentofnode2]:
                    self.parent[parentofnode2] = parentofnode1
                if self.rank[parentofnode2] > self.rank[parentofnode1]:
                    self.parent[parentofnode1] = parentofnode2
            return True
        else:
            print("cycle detected")
            return False
ds = DisjointSetsByRank(g)
# print(ds.findparentroot(3))

print(ds.union(0, 1))
print(ds.union(0, 3))
print(ds.union(2, 3))
print(ds.union(1, 2))
print(ds)

        
    
    