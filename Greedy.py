from networkx import Graph


class Greedy:

    min_cost = 9999999999
    solution = []
    count = 0

    def solve(self, graph: Graph, first_node):
        self.min_cost = 9999999999
        self.solution = []
        self._solve(graph, first_node, first_node, [], 0)
        print('cost={}, solution={}'.format(self.min_cost, self.solution))
        print(self.count)

    def _solve(self, graph: Graph, first_node, cur_node, visited_nodes: list, cost):
        self.count += 1

        if len(visited_nodes) == len(graph.nodes):
            if visited_nodes[-1] == first_node and cost < self.min_cost:
                self.min_cost = cost
                self.solution = [first_node] + visited_nodes
                return True
            else:
                return False

        neighbors = list(graph.adj[cur_node].items())

        nearest_neighbors = sorted(neighbors, key=lambda item: item[1]['weight'], reverse=False)

        for node, attrs in nearest_neighbors:
            if node not in visited_nodes:
                cycle_found = self._solve(graph, first_node, node, visited_nodes + [node], cost + attrs['weight'])
                if cycle_found:
                    return True

        return False
