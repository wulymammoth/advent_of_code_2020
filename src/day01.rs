use std::collections::HashSet;

pub fn main() -> (u32, u32) {
    let entries: Vec<String> = advent_of_code_2020::entries("day01.txt").unwrap();
    let mut nums: Vec<u32> = Vec::new();
    for entry in entries.iter() {
        nums.push(entry.parse::<u32>().unwrap());
    }
    let target = 2020;
    (
        report_repair(nums.clone(), target),
        report_repair_two(nums.clone(), target),
    )
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

fn report_repair_two(mut nums: Vec<u32>, target: u32) -> u32 {
    nums.sort();
    for i in 0..nums.len() - 2 {
        if i != 0 && nums[i] == nums[i - 1] {
            continue;
        }
        let mut j = i + 1;
        let mut k = nums.len() - 1;
        while j < k {
            let sum = nums[i] + nums[j] + nums[k];
            if sum == target {
                let product = nums[i] * nums[j] * nums[k];
                return product;
            } else if sum < target {
                // we need a larger summation
                j += 1;
            } else {
                // sum > target (we need something smaller)
                k -= 1;
            }
        }
    }
    0
}

#[test]
fn report_repair_pt1() {
    let nums = vec![1520, 250, 100, 500];
    assert_eq!(report_repair(nums, 2020), 760_000);

    let nums = vec![];
    assert_eq!(report_repair(nums, 2020), 0);
}

#[test]
fn report_repair_pt2() {
    let nums = vec![1520, 250, 100, 235, 756, 400];
    assert_eq!(report_repair_two(nums, 2020), 60_800_000);

    let nums = vec![1, 1, 1];
    assert_eq!(report_repair_two(nums, 2020), 0);
}

#[test]
fn report_repair_test() {
    assert_eq!(main(), (1013211, 13891280));
}
