ORIENTATIONS = ['N', 'E', 'S', 'W']  

class Grid:
    def __init__(self, max_x, max_y):
        self.max_x = max_x
        self.max_y = max_y
        self.scents = set()

class Robot:
    def __init__(self, x, y, orientation):
        self.x = x
        self.y = y
        self.orientation = orientation
        self.lost = False

    def turn_left(self):
        idx = ORIENTATIONS.index(self.orientation)
        self.orientation = ORIENTATIONS[(idx - 1) % 4]

    def turn_right(self):
        idx = ORIENTATIONS.index(self.orientation)
        self.orientation = ORIENTATIONS[(idx + 1) % 4]

    def move_forward(self):
        if self.orientation == 'N':
            self.y += 1
        elif self.orientation == 'S':
            self.y -= 1
        elif self.orientation == 'E':
            self.x += 1
        elif self.orientation == 'W':
            self.x -= 1

def parse_input(data):
    lines = [line.strip() for line in data.strip().splitlines() if line.strip()]
    max_x, max_y = map(int, lines[0].split())
    grid = Grid(max_x, max_y)
    robots = []
    i = 1
    while i < len(lines):
        x, y, orientation = lines[i].split()
        instructions = lines[i + 1]
        robots.append((Robot(int(x), int(y), orientation), instructions))
        i += 2
    return grid, robots


if __name__ == "__main__":
    import sys
    data = sys.stdin.read()
    grid, robots = parse_input(data)
    print(grid.max_x, grid.max_y)
    for robot, instructions in robots:
        print(robot.x, robot.y, robot.orientation, instructions)