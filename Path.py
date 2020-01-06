class Path:
    cost = 0
    heuristic = 0
    goal = ''
    path = []
    not_used_edges = []

    def __init__(self, cost, heuristic, path, not_used_edges):
        self.cost = cost
        self.heuristic = heuristic
        self.path = path
        self.goal = cost + heuristic
        self.not_used_edges = not_used_edges
