import unittest
from main import Robot, Grid

class TestRobot(unittest.TestCase):

    def test_turn_right_from_north(self):
        robot = Robot(1, 1, 'N')
        robot.turn_right()
        self.assertEqual(robot.orientation, 'E')

    def test_turn_left_from_north(self):
        robot = Robot(1, 1, 'N')
        robot.turn_left()
        self.assertEqual(robot.orientation, 'W')

    def test_move_forward_north(self):
        robot = Robot(1, 1, 'N')
        robot.move_forward()
        self.assertEqual(robot.y, 2)

    def test_move_forward_east(self):
        robot = Robot(1, 1, 'E')
        robot.move_forward()
        self.assertEqual(robot.x, 2)

    def test_robot_falls_off_grid(self):
        grid = Grid(5, 3)
        robot = Robot(3, 3, 'N')
        robot.execute('F', grid)
        self.assertTrue(robot.lost)

    def test_scent_prevents_fall(self):
        grid = Grid(5, 3)
        robot1 = Robot(3, 3, 'N')
        robot1.execute('F', grid)
        robot2 = Robot(3, 3, 'N')
        robot2.execute('F', grid)
        self.assertFalse(robot2.lost)

    def test_sample_input(self):
        grid = Grid(5, 3)
        r1 = Robot(1, 1, 'E')
        r1.execute('RFRFRFRF', grid)
        self.assertEqual(r1.result(), '1 1 E')
        r2 = Robot(3, 2, 'N')
        r2.execute('FRRFLLFFRRFLL', grid)
        self.assertEqual(r2.result(), '3 3 N LOST')
        r3 = Robot(0, 3, 'W')
        r3.execute('LLFFFLFLFL', grid)
        self.assertEqual(r3.result(), '2 3 S')

if __name__ == '__main__':
    unittest.main()