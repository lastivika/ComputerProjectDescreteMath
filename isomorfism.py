def check_vertices(graph1: dict, graph2: dict) -> bool:
    if len(list(graph1.keys())) == len(list(graph2.keys())):
        return True
    return False



def check_edges(graph1: dict, graph2: dict) -> bool:
    edges_list1 = []
    edges_list2 = []
    for key in graph1.keys():
        for vertex in graph1[key]:
            edges_list1.append(frozenset({key, vertex}))

    for key in graph2.keys():
        for vertex in graph2[key]:
            edges_list2.append(frozenset({key, vertex}))

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
    all_connections_list = []
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
    return False




def breadth_first_search(graph: dict, vertex) -> dict:
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

    return eccentricities




def find_diameter_of_graph(graph: dict) -> int | None:
    '''if check_connection(graph) is False:
        return None'''

    def breadth_first_search(graph: dict, vertex) -> dict:
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

        return eccentricities

    all_eccentricities = []
    for vertex in graph:
        all_eccentricities.append(max((breadth_first_search(graph, vertex)).values()))

    diameter = max(all_eccentricities)

    return diameter


def weisfeiler_lehman_test(graph: dict) -> bool:
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


    return marks


def isomorfism_check(graph1: dict, graph2: dict) -> bool:
    return all([check_vertices(graph1, graph2),
            check_edges(graph1, graph2),
            check_degrees(graph1, graph2),
            check_connection(graph1) != check_connection(graph2),
            find_diameter_of_graph(graph1) != find_diameter_of_graph(graph2),
            weisfeiler_lehman_test(graph1) != weisfeiler_lehman_test(graph2)])





print(weisfeiler_lehman_test({
    1: {2, 3, 4},
    2: {1, 5, 6},
    3: {1, 4},
    4: {1, 3},
    5: {2, 6},
    6: {2, 5},
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
