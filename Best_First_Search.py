from queue import PriorityQueue as pq


def best_first_search(graph, start, goal, heuristic):
    pq = [(heuristic[start], start)]
    visited = set()

    while pq:
        h, node = pq.pop(0)

        if node not in visited:
            visited.add(node)

            if node == goal:
                path = [node]

                while node != start:
                    node = graph[node][1]
                    path.append(node)
                return path[::-1]

            for child, _ in graph[node][0]:
                if child not in visited:
                    pq.append((heuristic[child], child))

    return None


# Example usage:
graph = {
    "A": ([("B", 5), ("C", 8)], None),
    "B": ([("D", 10)], "A"),
    "C": ([("D", 7)], "A"),
    "D": ([("E", 3)], "B"),
    "E": ([], "D"),
}
start = "A"
goal = "E"
heuristic = {"A": 5, "B": 3, "C": 4, "D": 2, "E": 0}

path = best_first_search(graph, start, goal, heuristic)
if path:
    print("Path found:", path)
else:
    print("Path not found")
