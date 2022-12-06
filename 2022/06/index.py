def find_beginning(marker_length: int, stream: str) -> int:
    for i in range( len(stream) - marker_length ):
        chunk = stream[i:i+marker_length]
        deduped = set(chunk)
        if len(deduped) == marker_length:
            return i + marker_length
    raise RuntimeError("No marker found.")

# Parse
input_stream: str
with open('./input.txt', 'r') as input_file:
    input_stream = input_file.read().strip()

RESULT_PART1 = find_beginning(4, input_stream)
print("Result Part 1:", RESULT_PART1)
assert RESULT_PART1 == 1766, "Should be 1766! You donkey broke something."

RESULT_PART2 = find_beginning(14, input_stream)
print("Result Part 2:", RESULT_PART2)
assert RESULT_PART2 == 2383, "Should be 2383! You donkey broke something."
