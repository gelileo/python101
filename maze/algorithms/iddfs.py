# Iterative Deepening Depth-First Search (IDDFS):
# Combines the space-efficiency of DFS with the optimality 
# of BFS by repeatedly executing a depth-limited DFS with
# increasing limits.
from typing import List, Tuple, Optional


def iddfs(
    maze: List[List[int]],
    start: Tuple[int, int],
    goal: Tuple[int, int],
    max_depth: int = 50,
) -> Tuple[List[Tuple[int, int]], List[Tuple[int, int]]]:
    """
    Perform Iterative Deepening Depth-First Search (IDDFS) on a grid maze.

    :param maze: 2D list representing the maze (0 for open cell, 1 for wall).
    :param start: Tuple (row, col) for the start cell.
    :param goal: Tuple (row, col) for the goal cell.
    :param max_depth: Maximum depth to search.
    :return: A tuple (order_visited, path) where:
             - order_visited is a list of cells in the order they were expanded.
             - path is the final path from start to goal (inclusive). If no path is found,
               path will be an empty list.
    """
    rows = len(maze)
    cols = len(maze[0])
    overall_order_visited: List[Tuple[int, int]] = []  # Records all nodes expanded

    def dls(
        node: Tuple[int, int],
        goal: Tuple[int, int],
        depth: int,
        path: List[Tuple[int, int]],
    ) -> Optional[List[Tuple[int, int]]]:
        """
        Depth-Limited Search (DLS): a recursive DFS that stops at a given depth.
        Avoids cycles by not revisiting nodes on the current path.
        """
        overall_order_visited.append(node)
        if node == goal:
            return path

        if depth <= 0:
            return None

        r, c = node
        # Explore neighbors: up, down, left, right.
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            neighbor = (nr, nc)
            # Check bounds and ensure the cell is open.
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0:
                # Avoid cycles: only explore neighbors not already in the current path.
                if neighbor not in path:
                    result = dls(neighbor, goal, depth - 1, path + [neighbor])
                    if result is not None:
                        return result
        return None

    # Iteratively increase the depth limit.
    for depth_limit in range(max_depth + 1):
        result = dls(start, goal, depth_limit, [start])
        if result is not None:
            return overall_order_visited, result

    # No path found within max_depth.
    return overall_order_visited, []


	# 1.	Depth-Limited Search (DLS):
	# •	The inner function dls performs a depth-first search but stops once the specified depth limit is reached.
	# •	It avoids cycles by ensuring that a neighbor is not already in the current path.
	# •	Each time a node is expanded, it is appended to overall_order_visited for visualization purposes.
	# •	If the goal is found, the current path (which includes the nodes from start to goal) is returned.
	# 2.	Iterative Deepening:
	# •	The outer loop calls dls with increasing depth limits—from 0 up to max_depth.
	# •	Once a valid path is found, the function returns both the order in which nodes were expanded and the final path.
	# •	If no path is found within the maximum depth limit, an empty path is returned.
	# 3.	Usage:
	# •	You can integrate this function with your maze visualization system to display the order of expansion and the final path discovered by IDDFS.