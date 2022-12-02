from dataclasses import dataclass
from enum import Enum

class Hand(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

class MatchResult(Enum):
    LOSE = 0
    DRAW = 3
    WIN  = 6

@dataclass
class Match:
    opponent: Hand
    me: Hand
    result: MatchResult or None = None
    score: int = -1

def char_to_Hand(char: str):
    if char == 'A' or char == 'X':
        return Hand.ROCK
    elif char == 'B' or char == 'Y':
        return Hand.PAPER
    elif char == 'C' or char == 'Z':
        return Hand.SCISSORS
    else:
        raise ValueError(f"Undefined char found: '{char}'")
    
def eval_match(opponent: Hand, me: Hand) -> MatchResult:
    if me == Hand.ROCK:
        if opponent == Hand.ROCK:
            return MatchResult.DRAW
        elif opponent == Hand.PAPER:
            return MatchResult.LOSE
        elif opponent == Hand.SCISSORS:
            return MatchResult.WIN
        else:
            raise ValueError(f"Opponent Hand Value unknown: '{opponent}'")
    elif me == Hand.PAPER:
        if opponent == Hand.ROCK:
            return MatchResult.WIN
        elif opponent == Hand.PAPER:
            return MatchResult.DRAW
        elif opponent == Hand.SCISSORS:
            return MatchResult.LOSE
        else:
            raise ValueError(f"Opponent Hand Value unknown: '{opponent}'")
    elif me == Hand.SCISSORS:
        if opponent == Hand.ROCK:
            return MatchResult.LOSE
        elif opponent == Hand.PAPER:
            return MatchResult.WIN
        elif opponent == Hand.SCISSORS:
            return MatchResult.DRAW
        else:
            raise ValueError(f"Opponent Hand Value unknown: '{opponent}'")
    else:
        raise ValueError(f"My hand is unknown: '{me}'")

matches: 'list[Match]' = []
# Parse into data structure
with open('./input.txt', 'r') as input_file:
    lines = input_file.readlines()
    for line in lines:
        theirs, mine = line.strip().split(' ')
        opponent = char_to_Hand(theirs)
        me = char_to_Hand(mine)
        matches.append(Match(opponent, me))

# Evaluate the results
for round in matches:
    round.result = eval_match(round.opponent, round.me)
    round.score = round.me.value + round.result.value

# Debug
# for i, round in enumerate(matches):
#     print(f"Round {i}:", round)

# Result Part 1
result_part1 = sum( round.score for round in matches )
print( "Result Part 1:", result_part1 )

assert result_part1 == 10595, f"Should be 10595! You donkey broke something."

#### Part 2

print("Result Part 2: <TBD>")
