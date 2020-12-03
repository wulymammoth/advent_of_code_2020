use std::io::Error;

pub fn main() -> Result<u32, Error> {
    let lines: Vec<String> = advent_of_code_2020::entries("day02.txt").unwrap();
    let mut total_count = 0;
    for line in lines {
        let line: Vec<&str> = line.split(' ').collect();
        let rng: Vec<&str> = line[0].split('-').collect();
        let rng: (i8, i8) = (rng[0].parse::<i8>().unwrap(), rng[1].parse::<i8>().unwrap());
        let ltr: Vec<&str> = line[1].split(':').collect();
        let ltr: char = ltr[0].parse().unwrap();
        let password = line[2];
        let mut count = 0;
        for ch in password.chars() {
            if ch == ltr {
                count += 1;
            }
        }
        let (lo, hi) = rng;
        if lo <= count && count <= hi {
            total_count += 1;
        }
    }
    Ok(total_count)
}
