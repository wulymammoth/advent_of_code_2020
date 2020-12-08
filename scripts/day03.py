def solve():
    fp = "day03.txt"
    with open(fp, 'r') as f:
        lines = [line.strip() for line in f.readlines()]

def part1(lines):
    num_lines         = len(lines)
    line_length       = len(lines[0])
    trees_encountered = 0

    def traverse(i, j, downs, rights):
        nonlocal trees_encountered

        # termination condition
        if i == num_lines:
            return

        if downs == 0 and rights == 0:
            if lines[i][j] == '#':
                trees_encountered += 1
            traverse(i, j + 1, 1, 2) # move right
        elif downs > 1 and rights > 1 and j != line_length - 1:
            traverse(i, j + 1, downs, rights - 1)
        elif downs > 1 and rights > 1 and j == line_length - 1: # move right
            traverse(i, 0, downs, rights - 1)
        elif downs > 1 and rights == 0: # move down
            traverse(i + 1, j, downs - 1, rights)
        else: # downs is 0 and rights is 0
            pass


    traverse(0, 0, 1, 3)

    return trees_encountered

if __name__ == '__main__':
    solve()

import unittest

class TestTobogganTrajectory(unittest.TestCase):
    def test(self):
        fp = "day03.txt"
        with open(fp, 'r') as f:
            lines = [line.strip() for line in f.readlines()]

        lines = lines[:3]
        for line in lines: print(line)
        self.assertEqual(part1(lines), 2)
