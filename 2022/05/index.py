from collections import deque
from dataclasses import dataclass
import re
import copy

@dataclass
class Command:
    amount: int
    src: int  # indices into stacks
    dst: int  # indices into stacks

REGEX_STACK_PER_GROUP = r"^(?:\[(\w)\]|^   )(?: \[(\w)\]|    )?(?: \[(\w)\]|    )?(?: \[(\w)\]|    )?(?: \[(\w)\]|    )?(?: \[(\w)\]|    )?(?: \[(\w)\]|    )?(?: \[(\w)\]|    )?(?: \[(\w)\]|    )?"
REGEX_COMMANDS = r"move (?P<amount>\d+) from (?P<from>\d+) to (?P<to>\d+)"

# Parse into data structures
# There can be at most 9 stacks, just init them and delete unused ones later
# Ofc just initing the containers you need is better but oh well.. /shrug
stacks: list[deque] = [ deque() for i in range(9) ]
commands: list[Command] = []
with open('./input.txt', 'r') as input_file:
    # files arent too big, just load into ram and run regex over instead line-by-line
    input_content = input_file.read()
    # Get all stacks, make em zero indexed instead of one
    for match in re.findall( REGEX_STACK_PER_GROUP, input_content, re.MULTILINE ):
        # match is a row including all stacks
        for i, char in enumerate(match):
            if char != "":
                stacks[i].appendleft(char)

    # Get all commands, make indices zero indexed
    for match in re.findall( REGEX_COMMANDS, input_content, re.MULTILINE ):
        amount, src, dst = map( int, match )
        commands.append( Command( amount, src-1, dst-1 ) )
    
    # Potential Inplace-delete unused deques in our stacks, not a tuple cuz we dont know part2
    stacks[:] = [ s for s in stacks if len(s) > 0 ]


# Part 2: We will need to run different commands for part 2 so its easiest to copy
# Reversing the operations would be possible to avoid reallocations but oh well
part2_stacks = copy.deepcopy(stacks)


# Part 1 Commands
for c in commands:
    for i in range(c.amount):
        stacks[c.dst].append( stacks[c.src].pop() )

top_most_items = tuple( s[-1] for s in stacks )
RESULT_PART1 = ''.join( top_most_items )
print("Result Part 1:", RESULT_PART1)
assert RESULT_PART1 == 'VQZNJMWTR', "Should be 'VQZNJMWTR'! You donkey broke something."


# Part 2 Commands
# Deques bite us in the ass because they dont have easy operations for moving multiples
# Converting to lists is lots of allocations but it works and we can use slices then /shrug
for c in commands:
    src = list(part2_stacks[c.src])
    slice_to = -c.amount - 1  # negative cuz we iterate backwards and minus one because zero indexed
    to_move_boxes = ( src[:slice_to:-1] )[::-1] # After slicing reverse it, since we iterated backwards

    part2_stacks[c.dst].extend(to_move_boxes)
    for i in range(c.amount): # remove copied boxes
        # Deque might be empty so gotta check, else exception
        if part2_stacks[c.src]:
            part2_stacks[c.src].pop()

top_most_items = tuple( s[-1] for s in part2_stacks )
RESULT_PART2 = ''.join( top_most_items )
print("Result Part 2:", RESULT_PART2)
assert RESULT_PART2 == 'NLCDCLVMQ', "Should be 'NLCDCLVMQ'! You donkey broke something."
