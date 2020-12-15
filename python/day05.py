import collections, unittest

def seat(boarding_pass):
    '''
    1. first, determine the row [0, 128); first 7 chars
    2. second, determine the column [0, 8); last 3 chars

    - binary-search w/o the 'search'
    '''
    row_boarding_pass, col_boarding_pass = boarding_pass[:7], boarding_pass[-3:]

    # determine row
    lo, hi, row = 0, 127, -1
    for half in row_boarding_pass:
        mid = (lo + hi) // 2
        front, back = mid, mid + 1
        if half == 'F':
            hi = front
        elif half == 'B':
            lo = back
        row = (lo + hi) // 2

    # determine column
    lo, hi, col = 0, 7, -1
    for half in col_boarding_pass:
        mid = (lo + hi) // 2
        left, right = mid, mid + 1
        if half == 'L': # lower/left half
            hi = mid
            col = left
        elif half == 'R': # 'R' upper/right half
            lo = mid
            col = right
        else:
            raise 'fugged up'

    return (row, col), row * 8 + col

def part1(boarding_passes):
    highest_seat_id = -1
    for i, boarding_pass in enumerate(boarding_passes):
        (row, col), seat_id = seat(boarding_pass)
        highest_seat_id = max(highest_seat_id, seat_id)
    return highest_seat_id

Case = collections.namedtuple('Case', ['pass_encoding', 'location', 'id'])

class TestSeatId(unittest.TestCase):
    def setUp(self):
        self.scenarios = [
            Case('BFFFBBFRRR', (70, 7), 567), # 4-7 -> 6-7 -> 7
            Case('FFFBBBFRRR', (14, 7), 119),
            Case('BBFFBBFRLL', (102, 4), 820),
        ]

    def test(self):
        for case in self.scenarios:
            boarding_pass, expected_location, expected_seat_id = case
            location, seat_id = seat(boarding_pass)
            self.assertEqual(location, expected_location)
            self.assertEqual(seat_id, expected_seat_id)

class TestBinaryBoarding(unittest.TestCase):
    def test(self):
        with open('day05.txt', 'r') as f:
            boarding_passes = [line.strip() for line in f.readlines()]
        self.assertEqual(part1(boarding_passes), 953)
