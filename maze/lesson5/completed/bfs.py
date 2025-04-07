# Completed code for Lesson 5
# This code includes a BFS implementation to find a path in the maze.
from collections import deque

def bfs(maze, start, end):
    """
    Perform Breadth-First Search (BFS) to find a path in the maze.
    Args:
        maze: 2D list representing the maze (1 = wall, 0 = path).
        start: Tuple[int, int], starting position.
        end: Tuple[int, int], ending position.
    Returns:
        List[Tuple[int, int]]: The path from start to end, or an empty list if no path exists.
    """
    rows, cols = len(maze), len(maze[0])
    queue = deque([start])
    visited = set()
    visited.add(start)
    parent = {start: None}

    while queue:
        current = queue.popleft()

        if current == end:
            # Reconstruct the path
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]

        # Explore neighbors
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = current[0] + dr, current[1] + dc
            neighbor = (nr, nc)

            if (
                0 <= nr < rows
                and 0 <= nc < cols
                and maze[nr][nc] == 0
                and neighbor not in visited
            ):
                queue.append(neighbor)
                visited.add(neighbor)
                parent[neighbor] = current

    return []  # No path found