# Finds the shortest path in weighted graphs by always 
# expanding the node with the smallest accumulated cost. 
# These are great when your maze (or graph) has weighted edges.

import heapq
from typing import List, Tuple, Dict


def dijkstra(
    maze: List[List[int]], start: Tuple[int, int], goal: Tuple[int, int]
) -> Tuple[List[Tuple[int, int]], List[Tuple[int, int]]]:
    """
    Perform Dijkstra’s Algorithm / Uniform Cost Search on a grid maze.

    :param maze: 2D list where 0 represents an open cell and 1 represents a wall.
    :param start: Tuple (row, col) for the start cell.
    :param goal: Tuple (row, col) for the goal cell.
    :return: A tuple (order_visited, path) where:
             - order_visited is the list of cells in the order they were expanded.
             - path is the final path from start to goal (inclusive). If no path is found,
               path will be an empty list.

    The algorithm uses the following components:
    - Priority Queue:
      A heap (via heapq) is used to always expand the node with the lowest accumulated cost first.
    - Costs Dictionary:
      Keeps track of the best (lowest) cost to reach each cell.
    - Parent Dictionary:
      Used for path reconstruction once the goal is reached.
    - Order of Visited Cells:
      The list order_visited is appended each time a cell is expanded. This is useful for visualizing the search process.
    - Loop Termination:
      Once the goal cell is popped from the priority queue, the algorithm reconstructs the final path and returns it along with the order of expansion. If no path is found, an empty path is returned.
    """
    rows = len(maze)
    cols = len(maze[0])

    # Priority queue holds entries of the form (cost, (row, col))
    pq: List[Tuple[int, Tuple[int, int]]] = []
    heapq.heappush(pq, (0, start))

    # Keep track of the best cost found so far for each cell
    costs: Dict[Tuple[int, int], int] = {start: 0}

    # For reconstructing the path: maps a cell to its predecessor
    parent: Dict[Tuple[int, int], Tuple[int, int]] = {}

    # Order in which nodes are expanded (useful for visualization)
    order_visited: List[Tuple[int, int]] = []

    # Set of visited nodes to prevent re-expanding them
    visited = set()

    while pq:
        current_cost, current = heapq.heappop(pq)

        if current in visited:
            continue

        visited.add(current)
        order_visited.append(current)

        # Stop if we reached the goal
        if current == goal:
            # Reconstruct path by following parent pointers
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            path.reverse()
            return order_visited, path

        r, c = current
        # Explore neighbors in the four cardinal directions
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            neighbor = (nr, nc)
            if 0 <= nr < rows and 0 <= nc < cols:
                if maze[nr][nc] == 0:  # Only consider open cells.
                    new_cost = current_cost + 1  # Uniform cost: 1 per move.
                    if neighbor not in costs or new_cost < costs[neighbor]:
                        costs[neighbor] = new_cost
                        parent[neighbor] = current
                        heapq.heappush(pq, (new_cost, neighbor))

    # If no path is found, return the order of visited nodes and an empty path.
    return order_visited, []
