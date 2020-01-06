import copy
from Path import Path


class Astar:
    expanded_nodes = 0
    solution = []

    def solve(self, graph, dist):
        input = list(graph.nodes)
        nodes_number = len(input)
        first_node = input[0]
        edges = list(dist)
        edges.sort()
        open_set = [Path(0, 0, [first_node], edges)]

        while open_set:
            self.solution = self.minimal_solution(open_set)
            last_node = self.solution.path[-1]
            if len(self.solution.path) == nodes_number:
                break
            for neigh in graph.adj[last_node].items():
                node = neigh[0]
                cost = neigh[1]['weight']
                if node in self.solution.path: continue
                sum_cost = self.solution.cost + cost
                new_path = self.solution.path + [node]
                not_used_edges = copy.deepcopy(self.solution.not_used_edges)
                not_used_edges.remove(cost)
                heuristic = self.heuristic_fun(not_used_edges, nodes_number, len(new_path)-1)
                open_set.append(Path(sum_cost, heuristic, new_path, not_used_edges))
            self.expanded_nodes += 1

    @staticmethod
    def minimal_solution(open_set):
        min_cost = 9999999
        solution = ''
        for state in open_set:
            if state.goal < min_cost:
                min_cost = state.goal
                solution = state
        open_set.remove(solution)
        return solution

    @staticmethod
    def heuristic_fun(edges, n, k):
        sum = 0
        minimal_edges = edges[:(n-k)]
        for edge in minimal_edges:
            sum += edge

        return sum