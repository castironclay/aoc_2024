import re

total = 0
all_matches = 0
with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    combined_line = "".join(lines)

# Remove sections between a don't() and a do()
line = re.sub(r"don't\(\).*?do\(\)", "", combined_line)
# Remove anything after a trailing don't()
line = re.sub(r"don't\(\).*$", "", line)
matches = re.findall(r"mul\(\d+,\d+\)", line)
all_matches += len(matches)
for match in matches:
    numbers = re.findall(r"\d+", match)
    value = int(numbers[0]) * int(numbers[1])
    total += value

print(f"Total Matches: {all_matches}")
print(f"Total: {total}")