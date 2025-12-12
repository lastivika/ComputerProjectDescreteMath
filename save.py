def turn_into_dict(graph: list[list[int]]) -> dict:
    graph_dict = {}
    for i in range(len(graph)):
        graph_dict[i] = []

    all_vertices = list(graph_dict.keys())

    for ind, row in enumerate(graph):
        for indx, element in enumerate(row):
            if element == 1:
                graph_dict[all_vertices[ind]].append(all_vertices[indx])

    return graph_dict



def check_vertices(graph1: dict | list[list[int]], graph2: dict | list[list[int]]) -> bool:
    """
    Checks if two graphs have the same number of vertices.

    Args:
        graph1, (dict): The first graph
        graph2, (dict): The second graph

    Returns:
        bool: Graphs have equal number of vertices
    """
    if isinstance(graph1, dict) and isinstance(graph2, dict):
        if len(list(graph1.keys())) == len(list(graph2.keys())):
            return True
        return False

    else:
        graph_dict_1 = turn_into_dict(graph1)
        graph_dict_2 = turn_into_dict(graph2)

        if len(list(graph_dict_1.keys())) == len(list(graph_dict_2.keys())):
            return True
        return False



def check_edges(graph1: dict | list[list[int]], graph2: dict | list[list[int]]) -> bool:
    """
    Checks if two graphs have the same number of edges.

    Args:
        graph1, (dict): The first graph
        graph2, (dict): The second graph

    Returns:
        bool: Graphs have equal number of edges
    """
    if isinstance(graph1, dict) and isinstance(graph2, dict):
        edges_list1 = []
        edges_list2 = []
        for key in graph1.keys():
            for vertex in graph1[key]:
                edges_list1.append((key, vertex))

        for key in graph2.keys():
            for vertex in graph2[key]:
                edges_list2.append((key, vertex))

        return len(set(edges_list1)) == len(set(edges_list2))

    else:
        graph_dict_1 = turn_into_dict(graph1)
        graph_dict_2 = turn_into_dict(graph2)

        edges_list1 = []
        edges_list2 = []
        for key in graph_dict_1.keys():
            for vertex in graph_dict_1[key]:
                edges_list1.append((key, vertex))

        for key in graph_dict_2.keys():
            for vertex in graph_dict_2[key]:
                edges_list2.append((key, vertex))

        return len(set(edges_list1)) == len(set(edges_list2))



def check_degrees(graph1: dict | list[list[int]], graph2: dict | list[list[int]]) -> bool:
    """
    Checks if two graphs have the same degrees of vertices.

    Args:
        graph1, (dict): The first graph
        graph2, (dict): The second graph

    Returns:
        bool: Graphs have equal degrees of vertices
    """
    if isinstance(graph1, dict) and isinstance(graph2, dict):
        graph1_degrees = []
        graph2_degrees = []
        for key in graph1.keys():
            graph1_degrees.append(len(graph1[key]))

        for key in graph2.keys():
            graph2_degrees.append(len(graph2[key]))

        graph1_degrees = sorted(graph1_degrees)
        graph2_degrees = sorted(graph2_degrees)

        return graph1_degrees == graph2_degrees


    else:
        graph_dict_1 = turn_into_dict(graph1)
        graph_dict_2 = turn_into_dict(graph2)

        graph1_degrees = []
        graph2_degrees = []
        for key in graph_dict_1.keys():
            graph1_degrees.append(len(graph_dict_1[key]))

        for key in graph_dict_2.keys():
            graph2_degrees.append(len(graph_dict_2[key]))

        graph1_degrees = sorted(graph1_degrees)
        graph2_degrees = sorted(graph2_degrees)

        return graph1_degrees == graph2_degrees





def check_connection(graph: dict | list[list[int]]) -> bool:
    """
    Checks if two graphs are both connected or both disconnected.

    Args:
        graph1, (dict): The first graph
        graph2, (dict): The second graph

    Returns:
        bool: True if both graphs have have the same connection
    """
    if isinstance(graph, list):
        graph1 = turn_into_dict(graph)
        graph = graph1

    def dfs_recursive(graph, u, visited):
        """
        Обхід у глибину для перевірки зв'язності
        """
        visited.add(u)
        for v in graph.get(u, []):
            if v not in visited:
                dfs_recursive(graph, v, visited)


    def get_unique_nodes(graph):
        """
        Отримує всі унікальні вершини графа.
        """
        nodes = set(graph.keys())
        for neighbors in graph.values():
            nodes.update(neighbors)
        return nodes

    nodes = get_unique_nodes(graph)
    if len(nodes) == 0:
        return True

    start_node = next(iter(nodes))
    visited = set()
    dfs_recursive(graph, start_node, visited)
    active_nodes = set()
    for n in nodes:
        if n in graph and len(graph[n]) > 0:
            active_nodes.add(n)

    #active nodes не включають ізольовані
    return len(visited) >= len(active_nodes)



def find_diameter_of_graph(graph: dict | list[list[int]]) -> int | None:
    """
    Finds  diameter of the given graph.

    Args:
        graph, (dict): The graph in which we search for diameter

    Returns:
        int | None: The diameter of the graph or None if graph is disconnectes
    """
    if isinstance(graph, list):
        graph1 = turn_into_dict(graph)
        graph = graph1

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
def weisfeiler_leman_test(graph_1: dict | list[list[int]], graph_2: dict | list[list[int]]) -> bool:
    """
    Checks isomorfism of two graphs using Weisfeiler Leman test.

   Args:
        graph_1, (dict): The first graph
        graph_2, (dict): The second graph

    Returns:
        bool: True if two graphs are isomorofic
    """
    k = find_diameter_of_graph(graph_1)
    if k is None:
        k = 4

    print('DIAMETER', k)
    marks_1 = {}
    marks_2 = {}

    for iteration in range(k):
        if iteration == 0:
            for vertex in graph_1:
                marks_1[vertex] = len(graph_1[vertex])

            for vertex in graph_2:
                marks_2[vertex] = len(graph_2[vertex])

        else:
            marks_list_1 = sorted(marks_1.values())
            marks_list_2 = sorted(marks_2.values())

            if marks_list_1 != marks_list_2:
                return False

            new_marks_1 = {}
            new_marks_2 = {}

            for vertex in graph_1:
                previous_mark_1 = marks_1[vertex]

                adjacent_marks_1 = []
                for vertices in graph_1[vertex]:
                    adjacent_marks_1.append(marks_1[vertices])

                adjacent_marks_1 = sorted(adjacent_marks_1)

                new_marks_1[vertex] = hash(f'{previous_mark_1}{adjacent_marks_1}')


            for vertex in graph_2:
                previous_mark_2 = marks_2[vertex]

                adjacent_marks_2 = []
                for vertices in graph_2[vertex]:
                    adjacent_marks_2.append(marks_2[vertices])

                adjacent_marks_2 = sorted(adjacent_marks_2)

                new_marks_2[vertex] = hash(f'{previous_mark_2}{adjacent_marks_2}')

            marks_1 = new_marks_1
            marks_2 = new_marks_2

    marks_list_1 = sorted(marks_1)
    marks_list_2 = sorted(marks_2)

    if marks_list_1 != marks_list_2:
        return False

    return True
