import argparse

import graph_structure
import isomorfism
import hamilton
import eulerian
import bipartive


parser = argparse.ArgumentParser(description='Change substring')


parser.add_argument('filename_1', help='Name of the first CSV file with graph')
parser.add_argument('function', choices = ["check_isomorfism", "find_hamiltonian", "find_eulerian",\
 "is_bipartite"], help='Function which should be called')
parser.add_argument('--filename_2', help='Name of the second CSV file with graph')
parser.add_argument('--starting_vertex', type=int, help='Starting vertex')

args = parser.parse_args()

filename1 = args.filename_1
filename2 = args.filename_2
starting_vertex = args.starting_vertex
function = args.function

graph_1 = graph_structure.get_adjacency_matrix(graph_structure.read_csv_to_graph(filename1))

if function == 'check_isomorfism':
    if filename2 is None:
        raise SystemExit('При check_isomorfism потрібно вказати другий файл з графом (--filename_2)')
    graph_2 = graph_structure.get_adjacency_matrix(graph_structure.read_csv_to_graph(filename2))
    checker = isomorfism.isomorfism_check(graph_1, graph_2)
    if checker:
        print('Графи ізоморфні')
    else:
        print('Графи не ізоморфні')

if function == 'find_hamiltonian':
    print(hamilton.find_hamiltonian_cycle(graph_1))

if function == 'find_eulerian':
    if starting_vertex is None:
        raise SystemExit('При find_eulerian потрібно вказати початкову вершину (--starting_vertex)')
    print(eulerian.fleury_algorithm(graph_1, starting_vertex))

if function == 'is_bipartite':
    print(bipartive.is_bipartite_matrix(graph_1))
