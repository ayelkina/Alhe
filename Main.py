from Bruteforce import Bruteforce
import time

import networkx as nx

from Astar import Astar


def add_nodes_from_file(file_nodes, graph):
    file = open(file_nodes, "r")
    data = file.read().splitlines()
    for node in data:
        id, long, lat = node.split(' ')
        graph.add_node(int(id), long=float(long), lat=float(lat))

    file.close()


def add_edges_from_file(file_links, graph):
    # change it
    links_list = []
    distances = []
    file = open(file_links, "r")
    data = file.read().splitlines()
    for link in data:
        n1, n2, distance = link.split(' ')
        links_list.append((n1, n2, float(distance)))
        distances.append(float(distance))

    graph.add_weighted_edges_from(links_list)
    file.close()
    return distances


if __name__ == "__main__":
    graph = nx.Graph()
    distances = add_edges_from_file('links_big.txt', graph)
    astar = Astar()
    bruteforce = Bruteforce()

    start_astar = time.time()
    distances.sort()
    astar.solve(graph, distances)
    print([list(graph.nodes)[0]] + astar.solution.path)
    print("cost", astar.solution.cost)
    print("Expanded nodes", astar.expanded_nodes)
    end_astar = time.time()
    print("A* time", end_astar - start_astar, '\n')
    # print(len(astar.solution.path))
    # print("expanded nodes", astar.expanded_nodes)

    start_brute = time.time()
    bruteforce.solve(graph, list(graph.nodes)[0])
    end_brute = time.time()
    print("bruteforce time", end_brute - start_brute)


