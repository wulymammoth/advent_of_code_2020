pub fn main() -> (u32, u32) {
    (part_one(), 0)
}

fn part_one() -> u32 {
    let lines: Vec<String> = advent_of_code_2020::entries("day02.txt").unwrap();
    let mut total_count = 0;
    for line in lines {
        let line: Vec<&str> = line.split(' ').collect();
        let range: Vec<&str> = line[0].split('-').collect();
        let range: (i8, i8) = (range[0].parse::<i8>().unwrap(), range[1].parse::<i8>().unwrap());
        let ltr: Vec<&str> = line[1].split(':').collect();
        let ltr: char = ltr[0].parse().unwrap();
        let password = line[2];
        let mut count = 0;
        for ch in password.chars() {
            if ch == ltr {
                count += 1;
            }
        }
        let (lo, hi) = range;
        if lo <= count && count <= hi {
            total_count += 1;
        }
    }
    total_count
}
