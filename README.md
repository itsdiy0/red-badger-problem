# Martian Robots

Solution to the Red Badger Martian Robots problem.

## How to run
```bash
python main.py < input.txt
```

## Approach

- Grid stores bounds and scent positions as a set of (x, y, orientation) tuples
- Robot class handles movement, rotation and instruction execution
- Scent system prevents future robots from falling off at previously lost positions