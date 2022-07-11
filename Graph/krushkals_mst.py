from collections import namedtuple

from disjointset import DisjointSetsByRank

Graph = namedtuple("Graph", ["nodes", "edges"])

### KrushKal's Algorith to find Minimum Spanning Tree ( MST )
nodes = range(5)
edges = {
    (0,1) : 15,
    (1,2) : 5,
    (0,3) : 20,
    (1,3) : 13,
    (3,2) : 10,
    (3,4): 6,
    (2,4): 8
}
g = Graph(nodes, edges)      
def findMSTwithkrushkals(g: Graph):
    ds = DisjointSetsByRank(g)
    edges = g.edges
    edgessortedbycost = sorted(edges.items(), key=lambda item: item[1])
    cost = 0
    print(edgessortedbycost)
    showedgesofmst = []
    for nodes in edgessortedbycost:
        node1 = nodes[0][0]
        node2 = nodes[0][1]
        edgecost = nodes[1]
        if ds.union(node1, node2):
            showedgesofmst.append((node1, node2))
            cost += edgecost
    return cost, showedgesofmst

print(findMSTwithkrushkals(g))
# (34, [(1, 2), (3, 4), (2, 4), (0, 1)]) 