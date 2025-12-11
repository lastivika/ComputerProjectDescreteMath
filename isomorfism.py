def check_vertices(graph1: dict, graph2: dict) -> bool:
    if len(list(graph1.keys())) == len(list(graph2.keys())):
        return True
    return False



def check_edges(graph1: dict, graph2: dict) -> bool:
    edges_list1 = []
    edges_list2 = []
    for key in graph1.keys():
        for vertex in graph1[key]:
            edges_list1.append((key, vertex))

    for key in graph2.keys():
        for vertex in graph2[key]:
            edges_list2.append((key, vertex))

    return len(set(edges_list1)) == len(set(edges_list2))



def check_degrees(graph1: dict, graph2: dict) -> bool:
    graph1_degrees = []
    graph2_degrees = []
    for key in graph1.keys():
        graph1_degrees.append(len(graph1[key]))

    for key in graph2.keys():
        graph2_degrees.append(len(graph2[key]))

    graph1_degrees = sorted(graph1_degrees)
    graph2_degrees = sorted(graph2_degrees)


    return graph1_degrees == graph2_degrees



def check_connection(graph: dict) -> bool:
    '''all_connections_list = []
    used_vertices = set()
    def find_connections(graph: dict, vertex) -> list:
        if vertex not in used_vertices:
            all_connections_list.extend(graph[vertex])
            used_vertices.add(vertex)
            for key in graph[vertex]:
                return find_connections(graph, key)
        else:
            return all_connections_list


    starting_key = list(graph.keys())[0]
    all_connected_vertices = find_connections(graph, starting_key)

    if len(set(all_connected_vertices)) == len(list(graph.keys())):
        return True
    return False'''


    def dfs_recursive(graph, u, visited):
        """Обхід у глибину для перевірки зв'язності (потрібно для is_bridge)."""
        visited.add(u)
        for v in graph.get(u, []):
            if v not in visited:
                dfs_recursive(graph, v, visited)


    def get_unique_nodes(graph):
        """Отримує всі унікальні вершини графа."""
        nodes = set(graph.keys())
        for neighbors in graph.values():
            nodes.update(neighbors)
        return nodes

    nodes = get_unique_nodes(graph)
    if not nodes:
        return True

    start_node = next(iter(nodes))
    visited = set()
    dfs_recursive(graph, start_node, visited)
    active_nodes = {n for n in nodes if n in graph and len(graph[n]) > 0}
    #active nodes не включають ізольовані
    return len(visited) >= len(active_nodes)




'''def breadth_first_search(graph: dict, vertex) -> dict:
    queue = [vertex]
    order = 0
    eccentricities = {vertex: 0}

    while order < len(queue):
        vertex = queue[order]
        order += 1

        for vertices in graph[vertex]:
            if vertices not in eccentricities:
                eccentricities[vertices] = eccentricities[vertex] + 1
                queue.append(vertices)

    return eccentricities'''




def find_diameter_of_graph(graph: dict) -> int | None:
    if check_connection(graph) is False:
        return None

    def breadth_first_search(graph: dict, vertex) -> dict:
        queue = [vertex]
        order = 0
        eccentricities = {vertex: 0}

        while order < len(queue):
            vertex = queue[order]
            order += 1

            for adjacent_vertex in graph[vertex]:
                if adjacent_vertex not in eccentricities:
                    eccentricities[adjacent_vertex] = eccentricities[vertex] + 1
                    queue.append(adjacent_vertex)

        return eccentricities

    all_eccentricities = []
    for vertex in graph:
        all_eccentricities.append(max((breadth_first_search(graph, vertex)).values()))

    diameter = max(all_eccentricities)

    return diameter



####################################################
'''def weisfeiler_lehman_test(graph: dict) -> list:
    k = find_diameter_of_graph(graph)

    marks = []

    def make_mark(v, arr):
        return f"{v}{arr}"

    for i in range(k):
        new_marks = []
        if i == 0:
            for vertex in graph:
                mark = len(graph[vertex])
                new_marks.append(mark)

        else:
            for ind, vertex in enumerate(graph.keys()):
                vertex_neighbours = graph[vertex]
                mark = marks[ind]
                neighbours_marks = []
                for elem in vertex_neighbours:
                    neighbours_marks.append(marks[int(elem) - 1])
                neighbours_marks = sorted(neighbours_marks)
                mark = make_mark(mark, neighbours_marks)
                new_marks.append(mark)

        marks = new_marks

    return marks'''

def weisfeiler_lehman_test(graph_1: dict, graph_2: dict) -> list:
    k = find_diameter_of_graph(graph_1)

    marks_1 = {}
    marks_2 = {}


    for iteration in range(k):
        if iteration == 0:
            for vertex in graph_1:
                marks_1[vertex] = len(graph_1[vertex])

            for vertex in graph_2:
                marks_2[vertex] = len(graph_2[vertex])

        else:
            marks_list_1 = sorted(marks_1)
            marks_list_2 = sorted(marks_2)

            if marks_list_1 != marks_list_2:
                return False

            new_marks_1 = {}
            new_marks_2 = {}

            for vertex in graph_1:
                previous_mark_1 = graph_1[vertex]

                adjacent_marks_1 = []
                for vertices in graph_1[vertex]:
                    adjacent_marks_1.append(vertices)

                adjacent_marks_1 = sorted(adjacent_marks_1)

                new_marks_1[vertex] = f'{previous_mark_1}{adjacent_marks_1}'


            for vertex in graph_2:
                previous_mark_2 = graph_2[vertex]

                adjacent_marks_2 = []
                for vertices in graph_2[vertex]:
                    adjacent_marks_2.append(vertices)

                adjacent_marks_2 = sorted(adjacent_marks_2)

                new_marks_2[vertex] = f'{previous_mark_2}{adjacent_marks_2}'

            marks_list_1 = new_marks_1
            marks_list_2 = new_marks_2


    return True











####################################################




def isomorfism_check(graph1: dict, graph2: dict) -> bool:
    '''if all([check_vertices(graph1, graph2),
            check_edges(graph1, graph2),
            check_degrees(graph1, graph2),
            check_connection(graph1) == check_connection(graph2),
            find_diameter_of_graph(graph1) == find_diameter_of_graph(graph2)]) is False:
        print('FUCK')
        return False


    if weisfeiler_lehman_test(graph1, graph2) is False:
        return False

    return True'''

    if check_vertices(graph1, graph2) is False:
        return 'SHO NAHUi'

    if check_edges(graph1, graph2) is False:
        return 'NE VIRU'

    if check_degrees(graph1, graph2) is False:
        return 'NE MOZHE Bit'

    if check_connection(graph1) == check_connection(graph2) is False:
        return 'NE KONEKT'

    if find_diameter_of_graph(graph1) == find_diameter_of_graph(graph2) is False:
        return 'DIAMETER'

    if weisfeiler_lehman_test(graph1, graph2) is False:
        return 'NU NEEEEE'

    return True



print(isomorfism_check(
    {
    1: [2, 5, 6],
    2: [1, 3, 7],
    3: [2, 4, 8],
    4: [3, 5, 9],
    5: [1, 4, 10],
    6: [1, 11, 12],
    7: [2, 13, 14],
    8: [3, 15, 16],
    9: [4, 17, 18],
    10: [5, 19, 20],
    11: [6],
    12: [6],
    13: [7],
    14: [7],
    15: [8],
    16: [8],
    17: [9],
    18: [9],
    19: [10],
    20: [10]
},
    {
    1:  [10, 19, 20],
    2:  [9, 17, 18],
    3:  [8, 15, 16],
    4:  [7, 13, 14],
    5:  [6, 11, 12],
    6:  [5, 10, 9],
    7:  [4, 8, 3],
    8:  [3, 2, 1],
    9:  [2, 1, 4],
    10: [1, 6, 5],
    11: [5],
    12: [5],
    13: [4],
    14: [4],
    15: [3],
    16: [3],
    17: [2],
    18: [2],
    19: [1],
    20: [1]
}))



G = {
    1: {2},
    2: {1, 3},
    3: {2},

    4: {5},
    5: {4},
}


G1 = {
    1: {2, 3, 4},
    2: {1, 5, 6},
    3: {1, 4},
    4: {1, 3},
    5: {2, 6},
    6: {2, 5},
}

'''print(weisfeiler_lehman_test(G1))'''
'''print(find_diameter_of_graph(G1))'''
'''print(max(breadth_first_search(G1, 1).values()))'''
'''print(check_connection(G1))'''

G2 = {
    1: {2, 3, 4},   # deg 3
    2: {1, 3, 5},   # deg 3
    3: {1, 2},      # deg 2
    4: {1, 6},      # deg 2
    5: {2, 6},      # deg 2
    6: {4, 5},      # deg 2
}

'''print(check_degrees(G1, G2))'''
