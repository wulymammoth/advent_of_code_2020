def part1(lines):
    total_lines       = len(lines)
    line_length       = len(lines[0])
    trees_encountered = 0

    i, j, remaining = 0, 0, 4
    while i < total_lines:
        if j == line_length: # reset to beginning of the line (row)
            j = 0

        if remaining == 0:
            if lines[i][j] == '#':
                trees_encountered += 1
            remaining = 4 # reset

        if remaining == 1: # go down
            i += 1
        else: # remaining is zero or greater than one
            j += 1
        remaining -= 1

    return trees_encountered

def part2(lines, slope):
    total_lines       = len(lines)
    line_length       = len(lines[0])
    trees_encountered = 0
    right, down       = slope
    steps             = right + down

    i, j, remaining = 0, 0, steps
    while i < total_lines:
        if j == line_length: # reset to beginning of the line (row)
            j = 0

        if remaining == 0:
            if lines[i][j] == '#':
                trees_encountered += 1
            remaining = steps # reset

        if remaining <= steps - right: # NOTE: big gotcha here (less than or equal not just equal)
            i += 1
        else: # remaining is zero or greater than one
            j += 1
        remaining -= 1

    return trees_encountered


import unittest
import functools

class TestTobogganTrajectory(unittest.TestCase):
    def setUp(self):
        self.lines_basic = [
            list(line) for line in [
                '..##.......',
                '#...#...#..',
                '.#....#..#.',
                '..#.#...#.#',
                '.#...##..#.',
                '..#.##.....',
                '.#.#.#....#',
                '.#........#',
                '#.##...#...',
                '#...##....#',
                '.#..#...#.#',
            ]
        ]
        self.slopes = [
            (1, 1),
            (3, 1),
            (5, 1),
            (7, 1),
            (1, 2)
        ]

    def test_part1_basic(self):
        self.assertEqual(part1(self.lines_basic), 7)

    def test_part1_full(self):
        fp = "day03.txt"
        with open(fp, 'r') as f:
            lines = [line.strip() for line in f.readlines()]

        self.assertEqual(part1(lines), 294)

    def test_part2_basic(self):
        ans = [part2(self.lines_basic, slope) for slope in self.slopes]
        self.assertEqual(ans, [2, 7, 3, 4, 2])

    def test_part2_full(self):
        fp = "day03.txt"
        with open(fp, 'r') as f:
            lines = [line.strip() for line in f.readlines()]

        ans = [part2(lines, slope) for slope in self.slopes]
        expected = [75, 294, 79, 85, 39]
        self.assertEqual(ans, expected)
        self.assertEqual(functools.reduce(lambda product, trees: product * trees, expected), 5774564250)
