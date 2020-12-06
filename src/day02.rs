type Range = (usize, usize);

pub fn main() -> (u32, u32) {
    let lines: Vec<String> = advent_of_code_2020::entries("day02.txt").unwrap();

    let mut count_part_1 = 0;
    let mut count_part_2 = 0;

    for line in lines {
        let line: Vec<&str> = line.split(' ').collect();
        let range: Vec<&str> = line[0].split('-').collect();
        let range: Range = (
            range[0].parse::<usize>().unwrap(),
            range[1].parse::<usize>().unwrap(),
        );
        let ltr: char = line[1].chars().nth(0).unwrap();
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

fn validator_two(range: Range, letter: char, password: &str) -> bool {
    let (first, second) = range;

    let mut chars = password.chars();
    let mut position_one_found = false;
    for i in 0..first {
        if i == first-1 {
            position_one_found = chars.next().unwrap() == letter;
        } else {
            chars.next();
        }
    }

    chars = password.chars(); // reset
    let mut position_two_found = false;
    for j in 0..second {
        if j == second-1 {
            position_two_found = chars.next().unwrap() == letter;
        } else {
            chars.next();
        }
    }

    position_one_found ^ position_two_found
}

#[test]
fn second_validation() {
    assert_eq!(validator_two((1, 3), 'a', "abcde"), true);
    assert_eq!(validator_two((1, 3), 'b', "cdefg"), false);
    assert_eq!(validator_two((2, 9), 'c', "ccccccccc"), false);
}

#[test]
fn test_day_2() {
    assert_eq!(main(), (493, 593));
}
