use std::collections::HashSet;
use std::fs::File;
use std::io::{BufRead, BufReader, Error};

pub fn main() -> Result<u32, Error> {
    let path = "day01.txt";
    let input = File::open(path)?;
    let buffered = BufReader::new(input);
    let target = 2020;
    let mut nums: Vec<u32> = Vec::new();
    for line in buffered.lines() {
        let num: u32 = line.unwrap().to_string().parse().unwrap();
        nums.push(num);
    }
    Ok(solve(nums, target))
}

fn solve(nums: Vec<u32>, target: u32) -> u32 {
    let mut set: HashSet<u32> = HashSet::new();
    for num in nums {
        let complement = target - num;
        if set.contains(&complement) {
            return complement * num;
        }
        set.insert(num);
    }
    0
}
