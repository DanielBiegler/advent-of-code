use std::io::BufRead; // Gives us `.lines()` for the BufReader

const PATH_DATA_INPUT: &str = "../input.txt";
const UNINITTED_SUM: i32 = -1;
struct Elf {
    items: Vec<i32>,
    sum: i32
}

fn debug_print(elves: &Vec<Elf>) {
    println!("Found the following Elves:");
    for (i, e) in elves.iter().enumerate() {
        println!("| Elf #{}", i);

        for item in e.items.iter() {
            println!("|--- {}", item);
        }

        println!("  == {}\n", e.sum);
    }
}

fn main() {
    // Input data
    let mut elves: Vec<Elf> = Vec::new();

    // Parse into data structure
    let reader = std::io::BufReader::new( std::fs::File::open(PATH_DATA_INPUT).unwrap() );
    let mut current_elf_inputs = Vec::<i32>::new();
    for line in reader.lines() {
        // `lines` already trims the newline at the end but lets trim it nontheless in case of spaces
        let trimmed = line.unwrap_or_default();
        if trimmed.is_empty() {
            elves.push( Elf { items: current_elf_inputs.clone(), sum: UNINITTED_SUM } );
            current_elf_inputs.clear();
        } else {
            current_elf_inputs.push( trimmed.parse::<i32>().unwrap() )
        }
    }
    // Dont forget last one if it has no following blank line
    if !current_elf_inputs.is_empty() {
        elves.push( Elf { items: current_elf_inputs.clone(), sum: UNINITTED_SUM } );
    }

    if elves.len() == 0 {
        println!("No elves found.");
        return
    }

    // Calc sums for all elves
    elves.iter_mut().for_each( |elf| elf.sum = elf.items.iter().sum() );
    
    // Sort elves according to their sums
    elves.sort_unstable_by_key( |elf| elf.sum);

    // Debug
    // debug_print(&elves);

    // Since we sorted the elves, largest will be the last element
    let solution_01: i32 = elves.last().unwrap().sum;
    println!("Solution Part 01: {}", solution_01);
    assert_eq!(solution_01, 67027);

    // 1. Take a slice of the last three elements
    // 2. Reduce them by summing up their sums
    let solution_02: i32 = elves[ elves.len() - 3 .. elves.len() ].iter().fold(0i32, |acc, e| acc + e.sum);
    println!("Solution Part 02: {}", solution_02);
    assert_eq!(solution_02, 197291);
    
}
