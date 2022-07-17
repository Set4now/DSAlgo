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


#def countprovinces(isconnected):
    #vertices = range(len(isconnected))
    vertices = len(isconnected) - 1
    visited_nodes = []
    start_vertex = 0
    count = 0 
    while len(visited_nodes) != len(isconnected):
        print(visited_nodes)
        if isconnected[start_vertex] not in visited_nodes:
            visited_nodes.append(start_vertex)
            for edge in range(len(isconnected[start_vertex])):
                if edge != start_vertex:
                    if isconnected[start_vertex][edge] == 1:
                        if edge not in visited_nodes:
                            visited_nodes.append(edge)
                            start_vertex += 1 
                            #vertices -= 1
            #else:
                #vertices -= 1
            count += 1
    return count 



isConnected = [[1,1,0],[1,1,0],[0,0,1]]
isConnected = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
isConnected = [[1,0,0],[0,1,0],[0,0,1]]
print(findprovinces(isConnected))


