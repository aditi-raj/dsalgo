INF=999999
V=5
G = [[INF,3,4,INF,INF],
     [3,INF,5,6,13],
     [4,5,INF,INF,8],
     [INF,6,INF,INF,7],
     [INF, INF,8,7, INF]]
selected = {}
for i in range(V):
    selected[i]=False
selected[0] = True
no_edges=0
while (no_edges< V - 1):
    minimum = INF
    x = 0
    y = 0
    for i in range(V):
        if selected[i]:
            for j in range(V):
                if ((not selected[j]) and G[i][j]!=INF):  
                    if minimum >= G[i][j]:
                        minimum = G[i][j]
                        x = i
                        y = j
    print(str(x) + "-" + str(y) + ":" + str(G[x][y]))
    selected[y] = True
    no_edges+= 1