use std::fs::File;
use std::io::{BufRead, BufReader, Error};

pub fn entries(path: &str) -> Result<Vec<String>, Error> {
    let input = File::open(path)?;
    let buffered = BufReader::new(input);
    let mut lines = Vec::new();
    for line in buffered.lines() {
        lines.push(line.unwrap());
    }
    Ok(lines)
}
