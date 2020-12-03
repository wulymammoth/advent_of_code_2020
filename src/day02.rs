type Range = (i8, i8);

pub fn main() -> (u32, u32) {
    let lines: Vec<String> = advent_of_code_2020::entries("day02.txt").unwrap();
    let mut count_part_1 = 0;
    let mut count_part_2 = 0;

    for line in lines {
        let line: Vec<&str> = line.split(' ').collect();
        let range: Vec<&str> = line[0].split('-').collect();
        let range: Range = (
            range[0].parse::<i8>().unwrap(),
            range[1].parse::<i8>().unwrap(),
        );
        let ltr: Vec<&str> = line[1].split(':').collect();
        let ltr: char = ltr[0].parse().unwrap();
        let password = line[2];

        // part 1
        if validator_one(range, ltr, password) {
            count_part_1 += 1;
        }

        // part 2
        if validator_two(range, ltr, password) {
            count_part_2 += 1;
        }
    }

    (count_part_1, count_part_2)
}

fn validator_one(range: Range, letter: char, password: &str) -> bool {
    let mut count = 0;
    for ch in password.chars() {
        if ch == letter {
            count += 1;
        }
    }
    let (lo, hi) = range;
    lo <= count && count <= hi
}

// offset by 1 (not zero-indexed)
// between the positional ranges, one of the positions must contain the specified char (letter)
// - take a slice and check within that slice that the character exists
// - to avoid slicing, we can just index into the string slice and check for the letter
fn validator_two(range: Range, letter: char, password: &str) -> bool {
    let mut chars = password.chars();
    let (first, second) = range;
    let position_one = (first - 1) as usize; // offset (not zero-indexed)
    let position_two = (second - 1) as usize; // offset (not zero-indexed)
    let mut found_position_one = false;
    if let Some(c) = chars.nth(position_one) {
        found_position_one = c == letter;
    }
    let mut found_position_two = false;
    if let Some(c) = chars.nth(position_two) {
        found_position_two = c == letter;
    }

    found_position_one ^ found_position_two
}
