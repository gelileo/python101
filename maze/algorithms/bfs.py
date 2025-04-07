# algorithms/bfs.py
# Approach: Breadth-First Search (BFS) begins at a source node and explores all its 
# immediate neighbors first, then moves on to the neighbors of those nodes, 
# effectively working level by level. A queue is typically used to keep track 
# of nodes to visit next. BFS guarantees finding the shortest path in an 
# unweighted graph or grid.

from collections import deque


def bfs(maze, start, goal):
    """
    Perform a Breadth-First Search (BFS) on the maze to find the shortest path.

    BFS is a graph traversal algorithm that explores all nodes at the current 
    depth level before moving on to nodes at the next depth level. It uses a 
    queue to keep track of nodes to visit next.

    :param maze: 2D list (rows x cols) representing the grid. 
                 0 indicates an open cell, 1 indicates a wall.
    :param start: Tuple (row, col) representing the starting position.
    :param goal: Tuple (row, col) representing the goal position.
    :return: A tuple containing:
             - A list of visited cells in order (for visualization purposes).
             - The final path as a list of (row, col) tuples from start to goal.
               If no path is found, the path list will be empty.
    """
    rows = len(maze)
    cols = len(maze[0])
    visited = [[False] * cols for _ in range(rows)]  # Tracks visited cells
    parent = dict()  # Maps each cell to its predecessor for path reconstruction

    queue = deque([start])  # Initialize the queue with the starting position
    visited[start[0]][start[1]] = True  # Mark the start cell as visited

    order_visited = []  # Keeps track of the order in which cells are visited

    while queue:
        current = queue.popleft()  # Dequeue the next cell to process
        order_visited.append(current)  # Add the cell to the visited order list

        if current == goal:
            # Goal reached, reconstruct the path
            path = []
            node = goal
            while node in parent:
                path.append(node)
                node = parent[node]
            path.append(start)  # Add the start cell to complete the path
            path.reverse()  # Reverse the path to start from the beginning
            return order_visited, path

        r, c = current
        # Explore neighbors (up, down, left, right)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc  # Calculate the neighbor's position
            if 0 <= nr < rows and 0 <= nc < cols:  # Check bounds
                if maze[nr][nc] == 0 and not visited[nr][nc]:  # Check if open and unvisited
                    visited[nr][nc] = True  # Mark neighbor as visited
                    parent[(nr, nc)] = current  # Set current cell as predecessor
                    queue.append((nr, nc))  # Enqueue the neighbor

    # If no path is found, return the visited order and an empty path
    return order_visited, []
