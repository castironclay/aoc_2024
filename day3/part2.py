import re

total = 0
all_matches = 0
with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    combined_line = "".join(lines)
    print(combined_line)

# Remove sections between a don't() and a do()
line = re.sub(r"don't\(\).*?do\(\)", "", combined_line)
# Remove trailing part of line after don't()
## If there was a trailing do() then this section would exist
## Can safetly assume there is no trailing do()
line = re.sub(r"don't\(\).*$", "", line)
matches = re.findall(r"mul\(\d+,\d+\)", line)
all_matches += len(matches)
for match in matches:
    numbers = re.findall(r"\d+", match)
    value = int(numbers[0]) * int(numbers[1])
    total += value

print(f"Total Matches: {all_matches}")
print(f"Total: {total}")
# 106266128