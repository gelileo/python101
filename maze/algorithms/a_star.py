# Enhances Dijkstra’s by incorporating a heuristic
# (often Manhattan distance for grid mazes) to estimate
# the remaining cost to the goal, which can significantly
# speed up the search.
import heapq
from typing import List, Tuple, Dict


def manhattan_distance(a: Tuple[int, int], b: Tuple[int, int]) -> int:
    """Compute the Manhattan distance between two cells."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def a_star(
    maze: List[List[int]], start: Tuple[int, int], goal: Tuple[int, int]
) -> Tuple[List[Tuple[int, int]], List[Tuple[int, int]]]:
    """
    Perform A* search on a grid-based maze.

    :param maze: 2D list where 0 represents an open cell and 1 represents a wall.
    :param start: Tuple (row, col) for the start cell.
    :param goal: Tuple (row, col) for the goal cell.
    :return: A tuple (order_visited, path) where:
             - order_visited is the list of cells in the order they were expanded.
             - path is the final path from start to goal (inclusive). If no path is found, path is an empty list.
    """
    rows = len(maze)
    cols = len(maze[0])

    # Priority queue: elements are (priority, cost_so_far, cell)
    # Priority = cost_so_far + heuristic (Manhattan distance)
    open_set = []
    initial_priority = manhattan_distance(start, goal)
    heapq.heappush(open_set, (initial_priority, 0, start))

    # Dictionary to record the best cost to reach each cell.
    cost_so_far: Dict[Tuple[int, int], int] = {start: 0}

    # For reconstructing the path: maps cell -> predecessor cell.
    parent: Dict[Tuple[int, int], Tuple[int, int]] = {}

    # Record the order in which cells are expanded.
    order_visited: List[Tuple[int, int]] = []

    # Set to track expanded cells.
    visited = set()

    while open_set:
        current_priority, current_cost, current = heapq.heappop(open_set)

        # Skip already visited nodes.
        if current in visited:
            continue

        visited.add(current)
        order_visited.append(current)

        # If goal is reached, reconstruct the path.
        if current == goal:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            path.reverse()
            return order_visited, path

        r, c = current
        # Explore neighbors (up, down, left, right)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            neighbor = (nr, nc)
            # Check bounds and that the neighbor is not a wall.
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0:
                new_cost = current_cost + 1  # Cost for each move is 1.
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    priority = new_cost + manhattan_distance(neighbor, goal)
                    parent[neighbor] = current
                    heapq.heappush(open_set, (priority, new_cost, neighbor))

    # If no path is found, return the order of visited nodes and an empty path.
    return order_visited, []


# 	•	Priority Queue:
# The open_set is a priority queue (min-heap) where each entry is a tuple:
# (priority, cost_so_far, cell)
# The priority is the sum of the cost so far and the Manhattan distance from the cell to the goal.
# 	•	Cost Tracking:
# The cost_so_far dictionary tracks the lowest cost found so far to reach each cell.
# 	•	Path Reconstruction:
# Once the goal is reached, the function reconstructs the path by following the parent pointers from the goal back to the start.
# 	•	Order of Expansion:
# The list order_visited records the order in which cells are expanded. This is useful for visualizing the search process.
