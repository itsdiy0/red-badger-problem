# Martian Robots

Solution to the Red Badger Martian Robots programming challenge.

## How to run
```bash
python main.py < input.txt
```

## How to run tests
```bash
python -m unittest test_main.py
```

## Approach
I broke the problem down into two core components: a Grid and a Robot.
The Grid holds the boundary coordinates and a set of scent positions. I used a set for scents because lookup is O(1) and order doesn't matter.
The Robot holds its position and orientation, and has methods for turning, moving forward, and executing a full instruction string. Orientation is stored as a string (N, E, S, W) ordered clockwise in a list, which makes left and right turns a simple index shift with modulo wrapping rather than a chain of if/else statements.
The scent system works by recording the last valid position and orientation of any robot that falls off the grid. Before any forward move, the robot checks whether its current position and orientation exist in the scent set. If it does, the instruction is ignored.

## Tech choices
Pure Python with no external dependencies. The problem is small enough that a single file solution is appropriate. I chose Python as it is my strongest language and the standard library provides everything needed including unittest for testing.