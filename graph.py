#graph implementation
from collections import deque
class Graph:
    def __init__(self,vertices) -> None:
        self.vertex=vertices
        self.adj_list=[[] for _ in range(vertices)]
    
    def add_edge(self,node1,node2):
        self.adj_list[node1].append(node2)
        self.adj_list[node2].append(node1)

    
    def bfs(self, start_vertex):
        visited = set()
        q = deque([start_vertex])
        visited.add(start_vertex)
        while q:
            curr_vertex = q.popleft()
            print(curr_vertex,end=" ")
            for neighbor in self.adj_list[curr_vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
        
    
    def dfs(self, start):
        visited = set()
        self._dfs(start, visited)

    def _dfs(self, vertex, visited):
        visited.add(vertex)
        print(vertex,end=" ")

        for neighbor in self.adj_list[vertex]:
            if neighbor not in visited:
                self._dfs(neighbor, visited)


my_graph=Graph(4)
my_graph.add_edge(0,1)
my_graph.add_edge(0,2)
my_graph.add_edge(1,3)
my_graph.add_edge(1,2)
# my_graph.print_graph()
my_graph.bfs(0)
my_graph.dfs(0)






