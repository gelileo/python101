# Greedy Best-First Search:
# Selects the next node based solely on the heuristic estimate to the goal. 
# While it can be faster, it doesn’t guarantee the shortest path.

import heapq
from typing import List, Tuple, Dict


def manhattan_distance(a: Tuple[int, int], b: Tuple[int, int]) -> int:
    """Compute the Manhattan distance between two cells."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def greedy_best_first_search(
    maze: List[List[int]], start: Tuple[int, int], goal: Tuple[int, int]
) -> Tuple[List[Tuple[int, int]], List[Tuple[int, int]]]:
    """
    Perform Greedy Best-First Search on a grid maze.

    :param maze: 2D list where 0 represents an open cell and 1 represents a wall.
    :param start: Tuple (row, col) for the start cell.
    :param goal: Tuple (row, col) for the goal cell.
    :return: A tuple (order_visited, path) where:
             - order_visited is the list of cells in the order they were expanded.
             - path is the final path from start to goal (inclusive). If no path is found,
               path will be an empty list.
    """
    rows = len(maze)
    cols = len(maze[0])

    # Priority queue holds entries of the form (heuristic, cell)
    open_set = []
    heapq.heappush(open_set, (manhattan_distance(start, goal), start))

    # For reconstructing the path: maps a cell to its predecessor.
    parent: Dict[Tuple[int, int], Tuple[int, int]] = {}

    # Record the order in which cells are expanded.
    order_visited: List[Tuple[int, int]] = []

    # Keep track of visited nodes to avoid re-expansion.
    visited = set()

    while open_set:
        current_priority, current = heapq.heappop(open_set)

        if current in visited:
            continue

        visited.add(current)
        order_visited.append(current)

        # Stop if we reached the goal.
        if current == goal:
            # Reconstruct the path from start to goal.
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            path.reverse()
            return order_visited, path

        r, c = current
        # Explore neighbors: up, down, left, right.
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            neighbor = (nr, nc)
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0:
                if neighbor not in visited:
                    parent[neighbor] = current
                    # Use only the heuristic as priority.
                    priority = manhattan_distance(neighbor, goal)
                    heapq.heappush(open_set, (priority, neighbor))

    # If no path is found, return the order visited and an empty path.
    return order_visited, []


# 	•	Priority Queue:
# The open_set is a min-heap (using heapq) that orders cells by their heuristic (Manhattan distance to the goal).
# 	•	Heuristic:
# For each neighbor, we compute the Manhattan distance to the goal. The cell with the smallest heuristic is expanded next, regardless of the cost taken to reach it.
# 	•	Path Reconstruction:
# Once the goal is reached, the algorithm reconstructs the path using a parent pointer dictionary.
# 	•	Order of Expansion:
# The order_visited list records the order in which cells are expanded, which is useful for visualization.

