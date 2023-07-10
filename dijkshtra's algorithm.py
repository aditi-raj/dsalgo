#dijkshtra's algorithm
def dijkstra(graph, start):

    dist = [float('inf') for _ in range(len(graph))]
    dist[start] = 0
    visited = set()
    
    while len(visited) < len(graph):
#to check which node to move next having smallest distance
        curr_node = None
        curr_dist = float('inf')

        for node, distance in enumerate(dist):
            if node not in visited and distance < curr_dist:
                curr_node = node
                curr_dist = distance
        
        visited.add(curr_node)
#to update minimum distance
        for neighbor in range(len(graph)):
            if graph[curr_node][neighbor] != 0:
                new_dist = dist[curr_node] + graph[curr_node][neighbor]
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
    
    return dist


graph = [
    [0, 1, 2, 0],
    [1, 0, 2, 1],
    [2, 2, 0, 2],
    [0, 1, 2, 0]
]

print(dijkstra(graph,0))

# #floyd warshall algorithm
# nV = 4
# INF = 999
# def floyd(G):
#     dist = list(map(lambda p: list(map(lambda q: q, p)), G))
#     # print(dist)
#     # Adding vertices individually
#     for i in range(nV):
#         for j in range(nV):
#             for k in range(nV):
#                 dist[j][k] = min(dist[j][k], dist[j][i] + dist[i][k])
#     sol(dist)
# # Printing the output
# def sol(dist):
#     for p in range(nV):
#         for q in range(nV):
#             if(dist[p][q] == INF):
#                 print("INF", end=" ")
#             else:
#                 print(dist[p][q], end=" ")
#         print(" ")
# G = [[0, 9, -4, INF],
# [6, 0, INF, 2],
# [INF, 5, 0, INF],
# [INF, INF, 1, 0]]
# floyd(G)

