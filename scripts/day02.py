def solve():
    fp    = 'day02.txt'
    count = 0
    with open(fp, 'r') as f:
        for line in f.readlines():
            line                    = line.strip()
            [policy, password]      = line.split(':')
            [rnge, char]            = policy.split(' ')
            [first_pos, second_pos] = rnge.split('-')
            case = ((int(first_pos), int(second_pos)), char, password)
            if valid(case): count += 1
    return count

def valid(case): # case is a tuple of `((first, second), char, password)`
    ((first_pos, second_pos), char, password) = case
    first_pos  = first_pos - 1 # offset
    second_pos = second_pos - 1 # offset
    return (char == password[first_pos]) ^ (char == password[second_pos])

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
            self.assertEqual(valid(case), expected)
