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
    distances = add_edges_from_file('links.txt', graph)
    astar = Astar()
    astar.solve(graph, distances)

    print(astar.solution.path)
    print(len(astar.solution.path))
    print("expanded nodes", astar.expanded_nodes)
    print("cost", astar.solution.cost)


