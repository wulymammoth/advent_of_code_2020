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

    def test_basic(self):
        valid_passports = 2
        self.assertEqual(part1(self.batch), valid_passports)

    def test_full(self):
        with open('day04.txt', 'r') as f:
            batch = [line.strip() for line in f.readlines()]
        self.assertEqual(part1(batch), 204) # too low
