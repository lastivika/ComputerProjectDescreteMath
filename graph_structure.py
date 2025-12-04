class Graph:
    def __init__(self, directed=False):
        self.graph = {}
        self.directed = directed
        self.vertex_count = 0
        self.edge_count = 0
    
    def add_vertex(self, vertex_name):
        if vertex_name not in self.graph:
            self.graph[vertex_name] = []
            self.vertex_count += 1
            return True
        return False
    
    def add_edge(self, from_vertex, to_vertex, weight=1):
        self.add_vertex(from_vertex)
        self.add_vertex(to_vertex)
        
        self.graph[from_vertex].append((to_vertex, weight))
        
        if not self.directed:
            self.graph[to_vertex].append((from_vertex, weight))
        
        self.edge_count += 1
        return True
    
    def get_vertices(self):
        return list(self.graph.keys())
    
    def get_edges(self):
        edges = []
        for from_vertex in self.graph:
            for to_vertex, weight in self.graph[from_vertex]:
                edges.append((from_vertex, to_vertex, weight))
        return edges
    
    def get_neighbors(self, vertex):
        if vertex in self.graph:
            return self.graph[vertex]
        return []
    
    def has_edge(self, from_vertex, to_vertex):
        if from_vertex not in self.graph:
            return False
        
        for neighbor, _ in self.graph[from_vertex]:
            if neighbor == to_vertex:
                return True
        return False
    
    def get_vertex_degree(self, vertex):
        if vertex in self.graph:
            return len(self.graph[vertex])
        return 0
    
    def is_connected(self, vertex1, vertex2):
        visited = set()
        
        def dfs(current):
            if current == vertex2:
                return True
            visited.add(current)
            for neighbor, _ in self.graph[current]:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
            return False
        
        return dfs(vertex1)
    
    def print_info(self):
        print("=" * 50)
        print("ІНФОРМАЦІЯ ПРО ГРАФ:")
        print("=" * 50)
        print(f"Кількість вершин: {self.vertex_count}")
        print(f"Кількість ребер: {self.edge_count}")
        print(f"Тип: {'Орієнтований' if self.directed else 'Неорієнтований'}")
    
    def print_adjacency_list(self):
        print("\nСПИСОК СУМІЖНОСТІ:")
        for vertex in sorted(self.graph.keys()):
            neighbors = self.graph[vertex]
            if neighbors:
                neighbors_str = ", ".join([f"{n}({w})" for n, w in neighbors])
                print(f"  {vertex} -> {neighbors_str}")
            else:
                print(f"  {vertex} -> (немає сусідів)")
    
    def get_adjacency_matrix(self):
        vertices = sorted(self.get_vertices())
        n = len(vertices)
        
        matrix = [[0] * n for _ in range(n)]
        index_map = {vertex: i for i, vertex in enumerate(vertices)}
        
        for from_vertex in self.graph:
            for to_vertex, weight in self.graph[from_vertex]:
                i = index_map[from_vertex]
                j = index_map[to_vertex]
                matrix[i][j] = weight
        
        return matrix, vertices
    
    def copy(self):
        new_graph = Graph(self.directed)
        new_graph.graph = {v: list(neighbors) for v, neighbors in self.graph.items()}
        new_graph.vertex_count = self.vertex_count
        new_graph.edge_count = self.edge_count
        return new_graph
