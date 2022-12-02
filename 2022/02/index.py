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
    riggedResult: MatchResult
    riggedHand: Hand
    result: MatchResult or None = None
    score: int = -1
    riggedScore: int = -1



def char_to_Hand(char: str):
    if char == 'A' or char == 'X':
        return Hand.ROCK
    elif char == 'B' or char == 'Y':
        return Hand.PAPER
    elif char == 'C' or char == 'Z':
        return Hand.SCISSORS
    else:
        raise ValueError(f"Undefined char found: '{char}'")



def char_to_rigged_result(char: str):
    if char == 'Y':
        return MatchResult.DRAW
    elif char == 'X':
        return MatchResult.LOSE
    elif char == 'Z':
        return MatchResult.WIN
    else:
        raise ValueError(f"Undefined char found: '{char}'")



def rig_for_hand(hand: Hand, desired_result: MatchResult) -> Hand:
    if desired_result == MatchResult.LOSE:
        if hand == Hand.ROCK: return Hand.SCISSORS
        elif hand == Hand.PAPER: return Hand.ROCK
        elif hand == Hand.SCISSORS: return Hand.PAPER
    elif desired_result == MatchResult.DRAW:
        return hand
    elif desired_result == MatchResult.WIN:
        if hand == Hand.ROCK: return Hand.PAPER
        elif hand == Hand.PAPER: return Hand.SCISSORS
        elif hand == Hand.SCISSORS: return Hand.ROCK
    else:
        raise ValueError(f"Undefined desired_result: '{desired_result}'")



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
        left, right = line.strip().split(' ')

        # Part 1
        opponent = char_to_Hand(left)
        me = char_to_Hand(right)
        
        # Part 2
        riggedResult = char_to_rigged_result(right)
        riggedHand = rig_for_hand(opponent, riggedResult)

        matches.append(Match(opponent, me, riggedResult, riggedHand))

# Evaluate the results
for round in matches:
    round.result = eval_match(round.opponent, round.me)
    round.score = round.me.value + round.result.value
    # Part 2
    round.riggedScore = round.riggedHand.value + round.riggedResult.value

# Debug
# for i, round in enumerate(matches):
#     print(f"Round {i}:", round)

# Result Part 1
result_part1 = sum( round.score for round in matches )
print( "Result Part 1:", result_part1 )

assert result_part1 == 10595, f"Should be 10595! You donkey broke something."

# Result Part 2
result_part2 = sum( round.riggedScore for round in matches )
print( "Result Part 2:", result_part2 )

assert result_part2 == 9541, f"Should be 9541! You donkey broke something."
