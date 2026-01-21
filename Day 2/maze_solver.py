from collections import deque

# Maze representation (1 = path, 0 = wall)
maze = [
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 1, 1, 1],
    [1, 1, 1, 0, 1]
]

rows = len(maze)
cols = len(maze[0])

start = (0, 0)
end = (4, 4)

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# ---------------- BFS ----------------
def bfs_maze(maze, start, end):
    queue = deque([(start, [start])])
    visited = set([start])
    nodes_explored = 0

    while queue:
        (x, y), path = queue.popleft()
        nodes_explored += 1

        if (x, y) == end:
            return path, nodes_explored

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if maze[nx][ny] == 1 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append(((nx, ny), path + [(nx, ny)]))

    return None, nodes_explored


# ---------------- DFS ----------------
def dfs_maze(maze, start, end):
    stack = [(start, [start])]
    visited = set()
    nodes_explored = 0

    while stack:
        (x, y), path = stack.pop()
        nodes_explored += 1

        if (x, y) == end:
            return path, nodes_explored

        if (x, y) not in visited:
            visited.add((x, y))
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    if maze[nx][ny] == 1 and (nx, ny) not in visited:
                        stack.append(((nx, ny), path + [(nx, ny)]))

    return None, nodes_explored


# -------------- Driver Code --------------
print("BFS Maze Output:")
path, explored = bfs_maze(maze, start, end)
print("Path:", path)
print("Nodes explored:", explored)

print("\nDFS Maze Output:")
path, explored = dfs_maze(maze, start, end)
print("Path:", path)
print("Nodes explored:", explored)
