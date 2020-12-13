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

import unittest

class TestTobogganTrajectory(unittest.TestCase):
    def test_basic(self):
        lines = [
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
                '.#..#...#.#'
            ]
        ]
        self.assertEqual(part1(lines), 7)

    def test_full(self):
        fp = "day03.txt"
        with open(fp, 'r') as f:
            lines = [line.strip() for line in f.readlines()]

        self.assertEqual(part1(lines), 294)
