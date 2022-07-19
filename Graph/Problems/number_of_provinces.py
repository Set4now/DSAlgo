def getprovincecountwithdfs(root, vertex_edge_mapping, visited_nodes):
    if root not in visited_nodes:
        visited_nodes.append(root)
    if root in vertex_edge_mapping:
        if vertex_edge_mapping[root]:
            for node in vertex_edge_mapping[root]:
                if node not in visited_nodes:
                    getprovincecountwithdfs(node, vertex_edge_mapping, visited_nodes)
    

def findprovinces(isconnected):
    vertex_edge_mapping = {}
    for i in range(len(isconnected)):
        vertex_edge_mapping[i] = []
        for j in range(len(isconnected[i])):
            if i != j:
                if isconnected[i][j] == 1:
                    vertex_edge_mapping[i].append(j)
    print(vertex_edge_mapping)
    count = 0
    visited_nodes = []
    for vertex in vertex_edge_mapping:
        if vertex not in visited_nodes:
            getprovincecountwithdfs(vertex, vertex_edge_mapping, visited_nodes)
            count += 1
    return count



isConnected = [[1,1,0],[1,1,0],[0,0,1]]
isConnected = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
isConnected = [[1,0,0],[0,1,0],[0,0,1]]
print(findprovinces(isConnected))


