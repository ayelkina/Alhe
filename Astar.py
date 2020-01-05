from Path import Path


class Astar:
    heuristic = ''
    expanded_nodes = 0
    solution = []

    def __init__(self, heuristic):
        self.heuristic = heuristic

    def solve(self, input, goal):
        self.expanded_nodes = 0
        expanded = []
        open_set = [Path(0, 0, [input])]

        while open_set:
            self.solution = self.minimal_solution(open_set)
            current_node = self.solution.path[-1]
            if current_node == goal:
                break
            if current_node in expanded: continue
            for node in neighbors(current_node):
                if node in expanded: continue
                cost = self.solution.cost + 1
                new_path = self.solution.path + [node]
                open_set.append(Path(cost, self.heuristic.compute(node, goal), new_path))
            expanded.append(current_node)
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
