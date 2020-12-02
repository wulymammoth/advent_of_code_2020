use std::io::Error;

pub fn main() -> Result<u8, Error> {
    let lines: Vec<String> = advent_of_code_2020::entries("day02.txt").unwrap();
    //let entries: Vec<Tuple> = Vec::new();
    for line in lines.iter() {
        let [range, letter, password] = line.split(' ').collect();
        println!("{:?}", );
    }
    Ok(1)
}

//fn password_philosophy(entries: Vec<Tuple>) -> u8 {
    //for entry in entries.iter() {
        //let [range, letter, password] = entry;
        //println!("range: {} | letter: {} | password: {}", range, letter, password);
    //}
    //0
//}
