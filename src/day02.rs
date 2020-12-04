type Range = (usize, usize);

pub fn main() -> (u32, u32) {
    let lines: Vec<String> = advent_of_code_2020::entries("day02.txt").unwrap();

    let mut count_part_1 = 0;
    let mut count_part_2 = 0;

    // NOTE: debugging
    let mut cnt = 0;

    for line in lines {
        let line: Vec<&str> = line.split(' ').collect();
        let range: Vec<&str> = line[0].split('-').collect();
        let range: Range = (
            range[0].parse::<usize>().unwrap(),
            range[1].parse::<usize>().unwrap(),
        );
        let ltr: char = line[1].chars().nth(0).unwrap();
        let password = line[2];

        // NOTE: debugging
        if cnt < 1 { println!("first password {}", password) }

        // part 1
        if validator_one(range, ltr, password) {
            count_part_1 += 1;
        }

        // part 2
        if validator_two(range, ltr, password) {
            count_part_2 += 1;

            // NOTE: debugging
            cnt += 1;
            //if cnt <= 1 {
                //println!("{}", password);
            //}
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
    let mut found_position_one = false;
    if let Some(c) = chars.nth(first) {
        found_position_one = c == letter;
    }
    let mut found_position_two = false;
    if let Some(c) = chars.nth(second) {
        found_position_two = c == letter;
    }

    found_position_one ^ found_position_two
}
