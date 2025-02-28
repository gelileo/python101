# Bidirectional Search:
# Runs two simultaneous searches—one forward from the
# start and one backward from the goal—hoping they meet
# in the middle, which can reduce the search space dramatically.
#

from collections import deque
from typing import List, Tuple, Dict


def bidirectional_search(
    maze: List[List[int]], start: Tuple[int, int], goal: Tuple[int, int]
) -> Tuple[List[Tuple[int, int]], List[Tuple[int, int]]]:
    """
    Perform Bidirectional Search on a grid maze.

    :param maze: 2D list where 0 is an open cell and 1 is a wall.
    :param start: Tuple (row, col) representing the start cell.
    :param goal: Tuple (row, col) representing the goal cell.
    :return: A tuple (order_visited, path) where:
             - order_visited is a list of cells in the order they were expanded.
             - path is the final path from start to goal (inclusive).
               If no path is found, path is an empty list.
    """
    rows = len(maze)
    cols = len(maze[0])

    # Queues for forward and backward searches.
    forward_queue = deque([start])
    backward_queue = deque([goal])

    # Parent dictionaries for path reconstruction.
    forward_parents: Dict[Tuple[int, int], Tuple[int, int]] = {}
    backward_parents: Dict[Tuple[int, int], Tuple[int, int]] = {}

    # Visited sets for both directions.
    forward_visited = {start}
    backward_visited = {goal}

    # Record the order of cell expansions (from both searches).
    order_visited: List[Tuple[int, int]] = []

    meeting_point = None

    while forward_queue and backward_queue and meeting_point is None:
        # Expand one node from the forward side.
        if forward_queue:
            current_f = forward_queue.popleft()
            order_visited.append(current_f)
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = current_f[0] + dr, current_f[1] + dc
                neighbor = (nr, nc)
                if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0:
                    if neighbor not in forward_visited:
                        forward_visited.add(neighbor)
                        forward_parents[neighbor] = current_f
                        forward_queue.append(neighbor)
                        # If the backward search has already visited this cell, we have a meeting point.
                        if neighbor in backward_visited:
                            meeting_point = neighbor
                            break
            if meeting_point is not None:
                break

        # Expand one node from the backward side.
        if backward_queue:
            current_b = backward_queue.popleft()
            order_visited.append(current_b)
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = current_b[0] + dr, current_b[1] + dc
                neighbor = (nr, nc)
                if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0:
                    if neighbor not in backward_visited:
                        backward_visited.add(neighbor)
                        backward_parents[neighbor] = current_b
                        backward_queue.append(neighbor)
                        if neighbor in forward_visited:
                            meeting_point = neighbor
                            break
            if meeting_point is not None:
                break

    # If no meeting point was found, there's no path.
    if meeting_point is None:
        return order_visited, []

    # Reconstruct the path from start to the meeting point.
    path_forward: List[Tuple[int, int]] = []
    node = meeting_point
    while node != start:
        path_forward.append(node)
        node = forward_parents[node]
    path_forward.append(start)
    path_forward.reverse()

    # Reconstruct the path from the meeting point to the goal.
    path_backward: List[Tuple[int, int]] = []
    node = meeting_point
    while node != goal:
        node = backward_parents[node]
        path_backward.append(node)

    # Combine both halves to get the full path.
    full_path = path_forward + path_backward
    return order_visited, full_path


# 	•	Data Structures:
# 	•	Two queues (forward_queue and backward_queue) are used to perform BFS from the start and goal simultaneously.
# 	•	Two dictionaries (forward_parents and backward_parents) track each node’s parent in their respective search, which are used later to reconstruct the final path.
# 	•	Two sets (forward_visited and backward_visited) record the nodes that have been visited in each search.
# 	•	A list order_visited keeps a record of the cells as they are expanded (for visualization).
# 	•	Search Process:
# 	•	The algorithm alternates between expanding nodes from the forward and backward searches.
# 	•	When a node is found that appears in both forward_visited and backward_visited, a meeting point is identified.
# 	•	Path Reconstruction:
# 	•	The final path is built by reconstructing the route from the start to the meeting point using the forward parent pointers, and from the meeting point to the goal using the backward parent pointers.
# 	•	The two paths are then concatenated to form the full path.

# This bidirectional search can be very efficient compared to unidirectional BFS in many cases, as the search space can be dramatically reduced when the two frontiers meet roughly in the middle.