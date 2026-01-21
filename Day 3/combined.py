from collections import deque

# Graph representation (city map)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E', 'G'],
    'G': ['F']
}


# ---------------- BFS ----------------
def bfs(graph, start, goal):
    queue = deque([[start]])
    visited = set([start])
    nodes_explored = 0

    while queue:
        path = queue.popleft()
        node = path[-1]
        nodes_explored += 1

        if node == goal:
            return path, nodes_explored

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(path + [neighbour])

    return None, nodes_explored


# ---------------- DFS ----------------
def dfs(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    nodes_explored = 0

    while stack:
        node, path = stack.pop()
        nodes_explored += 1

        if node == goal:
            return path, nodes_explored

        if node not in visited:
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    stack.append((neighbour, path + [neighbour]))

    return None, nodes_explored


# ----------- Bi-Directional BFS -----------
def bidirectional_bfs(graph, start, goal):
    if start == goal:
        return [start], 1

    start_queue = deque([[start]])
    goal_queue = deque([[goal]])

    start_visited = {start: [start]}
    goal_visited = {goal: [goal]}

    nodes_explored = 0

    while start_queue and goal_queue:

        # Expand from start side
        path = start_queue.popleft()
        node = path[-1]
        nodes_explored += 1

        for neighbour in graph[node]:
            if neighbour not in start_visited:
                new_path = path + [neighbour]
                start_visited[neighbour] = new_path
                start_queue.append(new_path)

                if neighbour in goal_visited:
                    return new_path + goal_visited[neighbour][::-1][1:], nodes_explored

        # Expand from goal side
        path = goal_queue.popleft()
        node = path[-1]
        nodes_explored += 1

        for neighbour in graph[node]:
            if neighbour not in goal_visited:
                new_path = path + [neighbour]
                goal_visited[neighbour] = new_path
                goal_queue.append(new_path)

                if neighbour in start_visited:
                    return start_visited[neighbour] + new_path[::-1][1:], nodes_explored

    return None, nodes_explored


# -------------- Driver Code --------------
start_node = 'A'
goal_node = 'G'

print("BFS Output:")
path, explored = bfs(graph, start_node, goal_node)
print("Path:", path)
print("Nodes explored:", explored)

print("\nDFS Output:")
path, explored = dfs(graph, start_node, goal_node)
print("Path:", path)
print("Nodes explored:", explored)

print("\nBi-Directional BFS Output:")
path, explored = bidirectional_bfs(graph, start_node, goal_node)
print("Path:", path)
print("Nodes explored:", explored)
