# Lesson 5: Understanding Maze-Solving Algorithms

## Objectives
- Learn the basics of maze-solving algorithms like BFS and DFS.
- Implement a simple BFS algorithm to find a path in a grid.

## Lecture

In this lecture, we will:
1. Understand what the Breadth-First Search (BFS) algorithm is and why it is useful.
2. Learn how BFS explores a maze step by step to find the shortest path.
3. See how BFS keeps track of visited cells and reconstructs the path.
4. Introduce the concept of a queue and how it is used in BFS.

### Key Concepts/Topics

#### What is BFS?
BFS is like exploring a maze level by level. Imagine you are standing at the start of a maze, and you want to find the shortest way to the end. BFS helps you do this by checking all possible paths one step at a time.

#### How BFS Works
1. Start at the beginning of the maze.
2. Look at all the neighboring cells you can move to.
3. Move to each neighbor one by one, but don’t visit the same cell twice.
4. Keep doing this until you reach the end of the maze.

#### Why BFS Finds the Shortest Path
BFS explores all possible paths step by step, so the first time it reaches the end, it has found the shortest way there.

#### Introducing the Queue
A queue is a data structure that works like a line of people waiting for something. The first person in line is the first to be served. This is called "First In, First Out" (FIFO).

**Code Example: Using a Queue**
```python
from collections import deque

# Create a queue
queue = deque()

# Add items to the queue
queue.append("A")
queue.append("B")
queue.append("C")
print("Queue after adding items:", list(queue))

# Remove items from the queue
first_item = queue.popleft()
print("Removed:", first_item)
print("Queue after removing an item:", list(queue))
```

#### Initializing the BFS Algorithm
```python
from collections import deque

# Initialize the BFS queue and visited set
queue = deque([start])
visited = set()
visited.add(start)
parent = {start: None}
```

#### Exploring Neighbors in BFS
```python
# Explore neighbors
for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    nr, nc = current[0] + dr, current[1] + dc
    neighbor = (nr, nc)

    if (
        0 <= nr < len(maze)
        and 0 <= nc < len(maze[0])
        and maze[nr][nc] == 0  # Check if the cell is a path
        and neighbor not in visited
    ):
        queue.append(neighbor)
        visited.add(neighbor)
        parent[neighbor] = current
```

#### Reconstructing the Path
```python
# Reconstruct the path from end to start
path = []
current = end
while current:
    path.append(current)
    current = parent[current]
path.reverse()  # Reverse the path to get it from start to end
print("Path:", path)
```

## Homework
- Modify the BFS implementation to print the path.