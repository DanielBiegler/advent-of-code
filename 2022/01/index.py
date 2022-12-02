elves_sums = []

with open('./input.txt', 'r') as input_file:
    current_sum = 0
    for line in input_file:
        stripped = line.strip()
        if stripped == '':
            elves_sums.append(current_sum)
            current_sum = 0
        else:
            current_sum += int(stripped)
    # add last one
    elves_sums.append(current_sum)

result_part1 = max(elves_sums)
print("Part 1 Result:", result_part1)
assert result_part1 == 67027, f"Should be 67027! You donkey broke something."

# Problem Part 2
# Now find the sum of the top three elves

result_part2 = sum(sorted(elves_sums)[-3::])
print("Part 2 Result:", result_part2)

assert result_part2 == 197291, f"Should be 197291! You donkey broke something."
