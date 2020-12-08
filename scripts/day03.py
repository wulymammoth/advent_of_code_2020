def solve():
    fp = "day03.txt"
    with open(fp, 'r') as f:
        lines = [line.strip() for line in f.readlines()]

def part1(lines):
    num_lines         = len(lines)
    line_length       = len(lines[0])
    trees_encountered = 0

    def traverse(i, j, remaining):
        nonlocal trees_encountered

        # terminal condition
        if i == num_lines:
            return

        if remaining == 0: # remaining is zero
            if lines[i][j] == '#':
                trees_encountered += 1
            j = 0 if j == line_length - 1 else j + 1
            traverse(i, j, 3)
        elif remaining == 1: # remaining > 0
            traverse(i + 1, j, remaining - 1)
        else: # remaining is 2 or greater
            j = 0 if j == line_length - 1 else j + 1
            traverse(i, j + 1, remaining - 1)

    traverse(0, 0, 0)

    return trees_encountered

if __name__ == '__main__':
    solve()

import unittest

class TestTobogganTrajectory(unittest.TestCase):
    def test_simple(self):
        fp = "day03.txt"
        with open(fp, 'r') as f:
            lines = [line.strip() for line in f.readlines()]

        lines = lines[:3]
        for line in lines: print(line)
        self.assertEqual(part1(lines), 2)

    def test_full(self):
        fp = "day03.txt"
        with open(fp, 'r') as f:
            lines = [line.strip() for line in f.readlines()]

        self.assertEqual(part1(lines), 2)
