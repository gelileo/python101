# algorithms/dfs.py

# DFS starts at a source node and explores as far along a branch 
# as possible before backtracking. 
# This is often implemented using recursion or an explicit stack.
def dfs(maze, start, goal):
    """
    Perform a Depth-First Search on the maze using a stack.

    :param maze: 2D list with 0 for open, 1 for wall
    :param start: (row, col)
    :param goal: (row, col)
    :return: (order_visited, path)
    """
    rows = len(maze)
    cols = len(maze[0])
    visited = [[False] * cols for _ in range(rows)]
    parent = dict()

    stack = [start]
    visited[start[0]][start[1]] = True

    order_visited = []

    while stack:
        current = stack.pop()
        order_visited.append(current)

        if current == goal:
            # Reconstruct path
            path = []
            node = goal
            while node in parent:
                path.append(node)
                node = parent[node]
            path.append(start)
            path.reverse()
            return order_visited, path

        r, c = current
        # Explore neighbors
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if maze[nr][nc] == 0 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    parent[(nr, nc)] = current
                    stack.append((nr, nc))

    return order_visited, []
