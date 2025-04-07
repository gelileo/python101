# Completed code for Lesson 7
# This code tests if the maze is solvable using BFS.

from bfs import bfs
from maze_data import MAZE1, START_POSITION, END_POSITION

def test_maze_solvability():
    """
    Test if the maze is solvable using BFS.
    """
    path = bfs(MAZE1, START_POSITION, END_POSITION)
    if path:
        print("Maze is solvable.")
        print("Path:", path)
    else:
        print("Maze is not solvable.")

if __name__ == "__main__":
    test_maze_solvability()