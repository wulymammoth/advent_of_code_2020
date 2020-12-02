use std::collections::HashSet;
use std::io::Error;

pub fn main() -> Result<u32, Error> {
    let mut entries: Vec<String> = advent_of_code_2020::entries("day01.txt").unwrap();
    let mut nums: Vec<u32> = Vec::new();
    for entry in entries.iter_mut() {
        nums.push(entry.parse::<u32>().unwrap());
    }
    let target = 2020;
    Ok(report_repair(nums, target))
}

fn report_repair(nums: Vec<u32>, target: u32) -> u32 {
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
