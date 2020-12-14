import collections, unittest

def part1(encoding):
    '''
    1. first, determine the row [0, 128); first 7 chars
    2. second, determine the column [0, 8); last 3 chars

    - binary-search w/o the 'search'
    '''
    row_encoding, col_encoding = encoding[:7], encoding[-3:]

    # determine row
    lo, hi = 0, 127
    row = -1
    for half in row_encoding:
        row = (lo + hi) // 2
        if half == 'F': # front (take lower/left half)
            hi = row
        else: # back (take upper/right half)
            lo = row

    # determine column
    lo, hi = 0, 7
    col = -1
    for half in col_encoding:
        mid = (lo + hi) // 2
        if half == 'L': # lower/left half
            hi = mid
            col = hi
        else: # upper/right half
            lo = mid
            col = lo

    seat_id = row * 8 + col

    return (row, col), seat_id

Case = collections.namedtuple('Case', ['pass_encoding', 'location', 'id'])

class TestBinaryBoarding(unittest.TestCase):
    def setUp(self):
        self.scenarios = [
            Case('BFFFBBFRRR', (70, 7), 567),
            # Case('FFFBBBFRRR', (14, 7), 119),
            # Case('BBFFBBFRLL', (102, 4), 820),
        ]

    def test_part1_basic(self):
        for case in self.scenarios:
            encoding, expected_location, expected_seat_id = case
            loc, seat_id = part1(encoding)
            self.assertEqual(loc, expected_location)
            self.assertEqual(seat_id, expected_seat_id)
