graph = {5: [2, 7], 2: [6, 4], 7: [8], 6: [], 4: [8], 8: []}

visited = set()


def dfs(graph, visited, node):

    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for child in graph[node]:
            dfs(graph, visited, child)


dfs(graph, visited, 5)
