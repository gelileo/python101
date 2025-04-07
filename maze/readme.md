## Maze Project Overview

This project is a Python-based application that uses Pygame to visualize and interact with mazes. It provides tools for solving, navigating, and editing mazes.

### Features
1. **Visualize Maze Solving Algorithms**: Demonstrates algorithms like BFS (Breadth-First Search) and DFS (Depth-First Search) to solve mazes.
2. **Interactive Maze Navigation**: Users can navigate through the maze manually.
3. **Maze Editor**: Create or modify mazes interactively and save them for later use.
4. **Save and Load Mazes**: The editor now supports saving and loading mazes as JSON files.
5. **Reset Button**: Added a reset button to clear the maze in the editor.

### Key Components
1. **`main.py`**: The entry point of the project. It provides three modes:
   - **Demo Mode**: Automatically demonstrates maze-solving algorithms.
   - **Step-by-Step Mode**: Allows users to step through the algorithm's progress.
   - **Interactive Mode**: Lets users navigate the maze manually.
2. **`constants.py`**: Defines grid dimensions, cell size, screen size, and FPS for the game loop.
3. **`colors.py`**: Contains color definitions for walls, paths, start/end points, and other UI elements.
4. **`editor.py`**: A tool to create or edit mazes interactively. Users can toggle cells between walls and paths and export the maze data.
5. **`maze_data.py`**: Contains the default maze layout and start/end positions.
6. **`mazes.py`**: Stores additional maze layouts for use in the editor or main program.
7. **`algorithms/`**: A directory containing various maze-solving algorithms like BFS, DFS, A*, and more.
8. **`config.json`**: Stores customizable settings like screen dimensions, cell size, and FPS.

### How to Run

#### Demo Mode
```bash
python3 ./main.py --mode demo --algo bfs
```

#### Step-by-Step Demo
```bash
python3 ./main.py --mode demo --algo bfs --step_by_step
```

#### Interactive Mode
```bash
python3 ./main.py --mode interactive
```

### Additional Information
- **Maze Editor**: Run `editor.py` to create or modify mazes. Use the mouse to toggle cells and export the maze layout.
- **Algorithms**: The `algorithms/` folder contains implementations of various maze-solving algorithms.
- **Configuration Management**: A `config.json` file has been added to store customizable settings like screen dimensions, cell size, and FPS.

### Implementation Details

#### `main.py`
This file serves as the entry point for running the maze-solving application. It provides three modes:
1. **Demo Mode**: Automatically demonstrates maze-solving algorithms like BFS and DFS.
2. **Step-by-Step Mode**: Allows users to step through the algorithm's progress manually.
3. **Interactive Mode**: Lets users navigate the maze manually.

**Key Functions:**
- **`draw_maze`**: Visualizes the maze, highlighting visited cells, step numbers, and the final path.
- **`run_demo`**: Demonstrates the selected algorithm by animating the exploration and final path.
- **`run_demo_step_by_step`**: Allows users to step through the algorithm's progress using keyboard inputs.
- **`run_interactive`**: Enables manual navigation of the maze, recording the player's path and marking visited cells.
- **`main`**: Parses command-line arguments to determine the mode and algorithm, then initializes the Pygame environment and runs the appropriate mode.

#### `editor.py`
This file provides a graphical interface for creating and editing mazes. Users can toggle cells between walls and paths and export the maze data.

**Key Functions:**
- **`output`**: Saves the current maze layout to a file.
- **`get_cell_position`**: Converts mouse coordinates to grid cell indices.
- **`draw_maze`**: Renders the maze grid with walls and paths.
- **`highlight_cell`**: Highlights the cell under the mouse pointer.
- **`draw_button`**: Displays an "Export" button for saving the maze.
- **`handle_mouse_click`**: Toggles cell states or triggers maze export on button click.
- **`redraw_maze`**: Updates the screen with the current maze state, button, and highlights.
- **`main`**: Parses command-line arguments to determine whether to start with a new maze, then initializes the Pygame environment and runs the editor.

### New Features
- **Save and Load Mazes**: The editor now supports saving and loading mazes as JSON files.
- **Reset Button**: Added a reset button to clear the maze in the editor.

### How to Use
#### Save and Load Mazes
- To save a maze, click the "Export" button in the editor.
- To load a maze, ensure the `maze.json` file exists and restart the editor.

#### Reset Maze
- Click the "Reset" button in the editor to clear the maze and start fresh.