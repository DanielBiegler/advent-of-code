from dataclasses import dataclass
from typing import TypedDict
from enum import Enum
import string

@dataclass
class Item:
    char: str
    prio: int

# Lookup dict
prio_for_char: 'dict[str, int]' = { char: prio for prio, char in enumerate( string.ascii_lowercase + string.ascii_uppercase, 1 ) }

@dataclass
class Rucksack:
    whole_items: 'list[Item]'
    first : 'list[Item]'
    second: 'list[Item]'

# Parse into data structure
rucksacks: 'list[Rucksack]' = []
with open('./input.txt', 'r') as input_file:
    lines = input_file.readlines()
    for line in lines:
        # Equal length is given by challenge
        stripped = line.strip()
        half = len(stripped) // 2  # round down
        
        left, right = stripped[:half], stripped[half:]
        left_items = list( Item(c, prio_for_char[c]) for c in left )
        right_items = list( Item(c, prio_for_char[c]) for c in right )
        # Part 2
        whole_items = left_items + right_items
        
        rucksacks.append( Rucksack(whole_items, left_items, right_items) )

# Find first occurance of duplicate items
shared_items: 'list[Item]' = []
for rucksack in rucksacks:
    for item in rucksack.first:
        if item in rucksack.second:
            shared_items.append( item )
            break

# Debug
# for si in shared_items:
    # print(si)

result_part1 = sum( item.prio for item in shared_items )
print("Result Part 1:", result_part1)
assert result_part1 == 8493, f"Should be 8493! You donkey broke something."

### Part 2

# Split input into chunks of n=3
rucksack_groups = [ rucksacks[i:i+3] for i in range(0, len(rucksacks), 3) ]

# Gather shared item per groups
shared_group_items: 'list[Item]' = []
for group in rucksack_groups:
    for item in group[0].whole_items:
        if item in group[1].whole_items and item in group[2].whole_items:
            shared_group_items.append(item)
            break

# Sum
result_part2 = sum( item.prio for item in shared_group_items )
print("Result Part 2:", result_part2)
assert result_part2 == 2552, f"Should be 2552! You donkey broke something."
