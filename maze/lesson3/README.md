# Lesson 3: Interactive Mode

## Objectives
- Enable users to navigate the maze manually.
- Learn how to handle keyboard inputs in Pygame.

## Lecture

In this lecture, we will:
1. Explore the concept of interactive mode in a maze-solving application.
2. Learn how to handle keyboard inputs in Pygame to navigate the maze.
3. Understand how to track the player's position and update the maze dynamically.

### Key Topics:
- Pygame event handling for keyboard inputs.
- Updating the player's position based on valid moves.
- Visualizing the player's path in the maze.

### Sample Code Segments

#### Pygame Event Handling for Keyboard Inputs
```python
for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            print("Up arrow pressed")
        elif event.key == pygame.K_DOWN:
            print("Down arrow pressed")
        elif event.key == pygame.K_LEFT:
            print("Left arrow pressed")
        elif event.key == pygame.K_RIGHT:
            print("Right arrow pressed")
```

#### Updating the Player's Position Based on Valid Moves
```python
player_pos = [1, 1]  # Starting position
maze = [
    [1, 1, 1, 1],
    [1, 0, 0, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 1],
]

new_pos = [player_pos[0] - 1, player_pos[1]]  # Move up
if maze[new_pos[0]][new_pos[1]] == 0:  # Check if the new position is valid
    player_pos = new_pos
    print("Player moved to", player_pos)
else:
    print("Invalid move")
```

#### Visualizing the Player's Path in the Maze
```python
visited = []
player_pos = [1, 1]
visited.append(tuple(player_pos))

# Draw visited cells
for cell in visited:
    rect = pygame.Rect(cell[1] * CELL_SIZE, cell[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, (0, 255, 0), rect)  # Green for visited cells

pygame.display.flip()
```

## Homework
- Add a feature to highlight the player's path.