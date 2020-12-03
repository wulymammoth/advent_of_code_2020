mod day01;
mod day02;

fn main() {
    println!("Day 01 answer: {:?}", day01::main().unwrap());

    let (day2_pt1, day2_pt2) = day02::main();
    println!("Day 02/1 answer: {:?}", day2_pt1);
    println!("Day 02/2 answer: {:?}", day2_pt2);
}
