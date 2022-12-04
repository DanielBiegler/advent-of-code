# Parse into data structure
set_pairs: 'list[tuple[set,set]]' = []
with open('./input.txt', 'r') as input_file:
    for line in input_file.readlines():
        stripped = line.strip()
        
        first_str, second_str    = stripped.split(',')
        first_begin, first_end   = map( int, first_str.split("-") )
        second_begin, second_end = map( int, second_str.split("-") )
        
        first_set  = set( range( first_begin, first_end   + 1 ) )
        second_set = set( range( second_begin, second_end + 1 ) )
        
        set_pairs.append( ( first_set, second_set ) )

# Could just be a sum, but may be needed for part 2
contained_pairs: 'list[tuple[set,set]]' = []
for pair in set_pairs:
    if pair[0].issuperset(pair[1]):
        contained_pairs.append(pair)
    elif pair[0].issubset(pair[1]):
        contained_pairs.append(pair)


result_part1 = len( contained_pairs )
print("Result Part 1:", result_part1)
assert result_part1 == 490, f"Should be 490! You donkey broke something."

### Part 2

intersected_pairs: 'list[tuple[set,set]]' = []
for pair in set_pairs:
    if len( pair[0].intersection( pair[1] ) ) > 0:
        intersected_pairs.append(pair)
        
result_part2 = len( intersected_pairs )
print("Result Part 2:", result_part2)
assert result_part2 == 921, f"Should be 921! You donkey broke something."
