graph = {"5": ["3", "7"], "3": ["2", "4"], "7": ["8"], "2": [], "4": ["8"], "8": []}

visited = []
quque = []


def bfs(graph, visited, node):
    visited.append(node)
    quque.append(node)
    while quque:
        m = quque.pop(0)
        print(m, end=" ")
        for child in graph[m]:
            if child not in visited:
                visited.append(child)
                quque.append(child)


bfs(graph, visited, "5")
