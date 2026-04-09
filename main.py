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

    def is_off_grid(self, grid):
        return self.x < 0 or self.y < 0 or self.x > grid.max_x or self.y > grid.max_y

    def execute(self, instructions, grid):
        for cmd in instructions:
            if cmd == 'L':
                self.turn_left()
            elif cmd == 'R':
                self.turn_right()
            elif cmd == 'F':
                if (self.x, self.y, self.orientation) in grid.scents:
                    continue  # ignore this F instruction
                prev_x, prev_y = self.x, self.y
                self.move_forward()
                if self.is_off_grid(grid):
                    grid.scents.add((self.x, self.y, self.orientation))
                    self.x, self.y = prev_x, prev_y
                    self.lost = True
                    return

    def result(self):
        status = f"{self.x} {self.y} {self.orientation}"
        if self.lost:
            status += " LOST"
        return status
    
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
    for robot, instructions in robots:
        robot.execute(instructions, grid)
        print(robot.result())