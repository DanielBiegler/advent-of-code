from dataclasses import dataclass
import string

# Lookup dict for priority values
prio_for_char: 'dict[str, int]' = { char: prio for prio, char in enumerate( string.ascii_lowercase + string.ascii_uppercase, 1 ) }

@dataclass
class Rucksack:
    whole_items: 'set[str]'
    first : 'set[str]'
    second: 'set[str]'

# Parse into data structure
rucksacks: 'list[Rucksack]' = []
with open('./input.txt', 'r') as input_file:
    lines = input_file.readlines()
    for line in lines:
        # Equal length is given by challenge
        stripped = line.strip()
        half = len(stripped) // 2  # round down
        
        left_items = set( stripped[:half] )
        right_items = set( stripped[half:] )
        # Part 2
        whole_items = set( stripped )
        rucksacks.append( Rucksack(whole_items, left_items, right_items) )

# Find first occurance of duplicate items
shared_items: 'list[str]' = []
for r in rucksacks:
    shared_item = r.first.intersection(r.second).pop()
    shared_items.append(shared_item)

result_part1 = sum( prio_for_char[item] for item in shared_items )
print("Result Part 1:", result_part1)
assert result_part1 == 8493, f"Should be 8493! You donkey broke something."

### Part 2

# Split input into chunks of n=3
rucksack_groups = [ rucksacks[i:i+3] for i in range(0, len(rucksacks), 3) ]

# Gather shared item per groups
shared_group_items: 'list[str]' = []
for group in rucksack_groups:
    shared_item = group[0].whole_items.intersection( *(group[1].whole_items, group[2].whole_items) ).pop()
    shared_group_items.append(shared_item)

# Sum
result_part2 = sum( prio_for_char[item] for item in shared_group_items )
print("Result Part 2:", result_part2)
assert result_part2 == 2552, f"Should be 2552! You donkey broke something."
