def solve(zero_based_indexing=True):
    fp    = 'day02.txt'
    count = 0
    with open(fp, 'r') as f:
        for line in f.readlines():
            line                    = line.strip()
            [policy, password]      = line.split(':')
            [rnge, char]            = policy.split(' ')
            [first_pos, second_pos] = rnge.split('-')
            case = ((int(first_pos), int(second_pos)), char, password)
            if valid(case, zero_based_indexing): count += 1
    return count

def valid(case, zero_based_indexing=True): # case is a tuple of `((first, second), char, password)`
    ((first_pos, second_pos), char, password) = case
    first_idx = first_pos if zero_based_indexing else first_pos - 1
    second_idx = second_pos if zero_based_indexing else second_pos - 1
    return (char == password[first_idx]) ^ (char == password[second_idx])

if __name__ == '__main__':
    print(solve())

import unittest

class TestValidator(unittest.TestCase):
    def test(self):
        cases = [
            [((1, 3), 'a', 'abcde'), True],
            [((1, 3), 'b', 'cdefg'), False],
            [((2, 9), 'c', 'ccccccccc'), False],
        ]
        for [case, expected] in cases:
            self.assertEqual(valid(case, False), expected)

class TestSolver(unittest.TestCase):
    def test_one_based_indexing(self):
        self.assertEqual(solve(False), 407)

    def test_zero_based_indexing(self):
        self.assertEqual(solve(), 593)
