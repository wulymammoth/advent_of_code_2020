REQUIRED_FIELDS = [
    'byr', # birth year
    'iyr', # issue year
    'eyr', # expiration year
    'hgt', # height
    'hcl', # hair color
    'ecl', # eye color
    'pid', # passport ID
    'cid', # country ID
]

EYE_COLORS = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

def valid_height(height):
    digits = []
    for i, char in enumerate(height):
        if char.isdigit():
            digits.append(char)
        elif char.isalpha():
            if i < 3: # we must have '#' and at least two digits
                return False
            suffix = height[i:]
            if suffix not in ['cm', 'in']:
                return False
            h = int(''.join(digits))
            return 150 <= h <= 193 if suffix == 'cm' else 50 <= h <= 76
        else: # non-alphanumeric
            return False
    return False

def valid_hair_color(hair):
    'number followed by exactly six chars that are 0-9 or a-f' # assuming case sensitivity here
    prefix, suffix = hair[:len(hair)-6], hair[-6:]
    if prefix[0] != '#':
        return False
    for char in prefix:
        if not char.isdigit():
            return False
    for char in suffix:
        if not char.isalnum():
            return False
        if char.isalpha() and ord(char) not in range(ord('a'), ord('f') + 1):
            return False
    return True

def valid_passport_id(pid):
    if len(pid) < 9:
        return False
    for digit in pid:
        if not digit.isdigit():
            return False
    return True

VALIDATORS = {
    'byr': lambda year: len(year) >= 4 and 1920 <= int(year) <= 2002,
    'iyr': lambda year: len(year) >= 4 and 2010 <= int(year) <= 2020,
    'eyr': lambda year: len(year) >= 4 and 2020 <= int(year) <= 2030,
    'hgt': valid_height,
    'hcl': valid_hair_color,
    'ecl': lambda eye_color: eye_color in EYE_COLORS,
    'pid': valid_passport_id
}

def valid(document):
    for req_field in REQUIRED_FIELDS:
        if req_field not in document and req_field != 'cid':
            return False
    return True

def add_fields(passport, line):
    for pair in line.split(' '):
        field, value = pair.split(':')
        passport[field] = value
    return passport

def passports(batch):
    '''parses out all the passports
    find EOB or empty line made up an empty string'''
    num_lines, collection, current_passport = len(batch), [], {}
    for line in batch:
        if len(line) == 0: # end of current passport
            collection.append(current_passport)
            current_passport = {} # reset
        else:
            current_passport = add_fields(current_passport, line)
    if current_passport:
        collection.append(current_passport)
    return collection

def part1(batch):
    return len(list(filter(valid, passports(batch))))

def part2(batch):
    return len(list(filter(valid, passports(batch))))

import unittest

class TestPassportProcessing(unittest.TestCase):
    def setUp(self):
        self.batch = [
            'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd',
            'byr:1937 iyr:2017 cid:147 hgt:183cm', # valid passport (all eight fields are present)
            '',
            'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884',
            'hcl:#cfa07d byr:1929', # invalid (missing height field)
            '',
            'hcl:#ae17e1 iyr:2013',
            'eyr:2024',
            'ecl:brn pid:760753108 byr:1931',
            'hgt:179cm', # valid even though missing country ID (cid) field / North Pole credentials
            '',
            'hcl:#cfa07d eyr:2025 pid:166559648',
            'iyr:2011 ecl:brn hgt:59in' # invalid; missing `cid` and `byr` fields
        ]

    def test_part1_basic(self):
        valid_passports = 2
        self.assertEqual(part1(self.batch), valid_passports)

    def test_part1_full(self):
        with open('day04.txt', 'r') as f:
            batch = [line.strip() for line in f.readlines()]
        self.assertEqual(part1(batch), 204) # too low

    def test_byr_validator(self):
        self.assertTrue(VALIDATORS['byr']('2002'))
        self.assertFalse(VALIDATORS['byr']('2003'))

    def test_hgt_validator(self):
        self.assertTrue(VALIDATORS['hgt']('60in'))
        self.assertTrue(VALIDATORS['hgt']('190cm'))
        self.assertFalse(VALIDATORS['hgt']('190in'))
        self.assertFalse(VALIDATORS['hgt']('190'))

    @unittest.skip
    def test_hcl_validator(self):
        self.assertTrue(VALIDATORS['hcl']('#123abc'))
        self.assertFalse(VALIDATORS['hcl']('123abc'))
        self.assertFalse(VALIDATORS['hcl']('#123abz'))

    @unittest.skip
    def test_pid_validator(self):
        self.assertTrue(VALIDATORS['pid']('000000001'))
        self.assertFalse(VALIDATORS['pid']('0123456789'))

    @unittest.skip
    def test_part2_full(self):
        pass
