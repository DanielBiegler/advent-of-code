from dataclasses import dataclass, field
from enum import Enum
import re
from collections import deque

class FileType(Enum):
    DIR  = 0
    DATA = 1

@dataclass
class Node:  # needed?
    type: FileType
    name: str
    size: int or None
    parent: 'Node' or None  # root has no parent
    children: 'list[Node]' = field(default_factory=lambda:[])

SIZE_AT_MOST = 100_000

# Matches each command and groups with output
# `ls` includes its output in the group for processing
REGEX_COMMANDS = r'(?:^\$ (?P<command>cd|ls).*?(?=\$|\Z))'   # flags=gsm
# Matches argument of the changing directory
REGEX_COMMAND_CD = r'^\$ cd (\S+)'
# Matches specific info inside the command, either `dir` or `ls`
# Allows checking if theres a dir or file
REGEX_COMMAND_LS = r'^(?:(?P<size>\d+) (?P<filename>\S+)|dir (?P<dirname>\S+))'

# Isnt the folder always before? Can we use this property?
# Not in an easy way, because we need to count directories multiple times
# Thats kinda dumb imo.. but thats the challenge
# /          == 200bytes
# /foo.txt   == 100bytes
# /a/bar.txt == 100bytes
# Solution: 300bytes
# Because: / contains (directly) foo and (indirectly) bar + the a directory (100)
# Maybe this gets fixed with part2

# TODO got the parsing down but needs(?) to be put into a tree structure for iteration

fs = Node( FileType.DIR, "/", None, None )  # TODO doesnt get used
with open('./test.txt', 'r') as input_file:
    history = input_file.read()
    directory_stack = deque()  # current directory is on top (right)
    # Grouping of commands with their output
    for matched_command in re.finditer(REGEX_COMMANDS, history, re.DOTALL+re.MULTILINE):
        command = matched_command.groupdict()["command"]
        # Could have captured the cd argument in the first regex but
        # Splitting the logic up is more readable and allows separate regex per command
        # This'd be useful if part2 needs more arguments or different commands
        # This costs one more matching per `cd` but thats ok since we dont know
        if command == "cd":
            cd_arg = re.match(REGEX_COMMAND_CD, matched_command.group()).group(1)
            print(f"GOING INTO '{cd_arg}'")
            if cd_arg == "..":  # go back
                directory_stack.pop()  # will raise error if empty, thats ok lets crash
            else:
                directory_stack.append(cd_arg)
            print("Stack:", directory_stack)

        elif command == "ls":
            groups = tuple( re.finditer(REGEX_COMMAND_LS, matched_command.group(), re.MULTILINE) )
            print(f'Listing {len(groups)} files in folder "{directory_stack[-1]}":')
            for g in groups:
                print("  -", g.groupdict())

        else:
            raise RuntimeError(f'Unexpected Command found: "{command}"')
        print("-"*30)
        print("-"*30)
        print("-"*30)

# Debug
print("FS:", fs)