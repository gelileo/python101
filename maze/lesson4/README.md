# Lesson 4: Argument Parsing

## Objectives
- Learn how to use command-line arguments to control the program.
- Add argument parsing to allow users to select modes (e.g., demo, interactive).

## Lecture

In this lecture, we will:
1. Understand what command-line arguments are and why they are useful.
2. Learn how to use Python's `argparse` module to handle arguments.
3. Explore how to use arguments to control the behavior of a program.

### Key Concepts/Topics

#### What are Command-Line Arguments?
Command-line arguments are extra pieces of information you can pass to a program when you run it. For example:
```bash
python main.py --mode demo
```
Here, `--mode demo` is a command-line argument that tells the program to run in demo mode.

#### Using the `argparse` Module
The `argparse` module makes it easy to handle command-line arguments in Python.

**Code Example: Basic Argument Parsing**
```python
import argparse

# Create the parser
parser = argparse.ArgumentParser(description="Maze Project")

# Add arguments
parser.add_argument("--mode", choices=["demo", "interactive"], default="demo", help="Choose the mode")

# Parse the arguments
args = parser.parse_args()
print("Mode:", args.mode)
```

#### Controlling Program Behavior with Arguments
You can use the parsed arguments to control what your program does.

**Code Example: Using Arguments to Control Behavior**
```python
if args.mode == "demo":
    print("Running in demo mode")
    # Add code to run the demo
elif args.mode == "interactive":
    print("Running in interactive mode")
    # Add code to run the interactive mode
```

#### Adding More Arguments
You can add more arguments to make your program more flexible.

**Code Example: Adding More Arguments**
```python
parser.add_argument("--algo", choices=["bfs", "dfs"], default="bfs", help="Choose the algorithm for demo mode")
parser.add_argument("--step_by_step", action="store_true", help="Run the demo one step at a time")

args = parser.parse_args()
print("Algorithm:", args.algo)
print("Step-by-step mode:", args.step_by_step)
```

### Simple Example: Using argparse
Let's start with a simple example to understand how `argparse` works. Imagine you want to create a program that greets a user by their name and age.

**Code Example: Greeting Program**
```python
import argparse

# Create the parser
parser = argparse.ArgumentParser(description="Greeting Program")

# Add arguments
parser.add_argument("--name", required=True, help="Your name")
parser.add_argument("--age", type=int, required=True, help="Your age")

# Parse the arguments
args = parser.parse_args()

# Use the arguments
print(f"Hello, {args.name}! You are {args.age} years old.")
```

**How to Run:**
```bash
python greeting.py --name Alice --age 12
```
**Output:**
```
Hello, Alice! You are 12 years old.
```

## Homework
- Add an argument to specify the maze file to load.