import re

total = 0
all_matches = 0
with open("input.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    matches = re.findall(r"mul\(\d+,\d+\)", line)
    all_matches += len(matches)
    for match in matches:
        print(match)
        numbers = re.findall(r"\d+", match)
        value = int(numbers[0]) * int(numbers[1])
        total += value

print(f"Total Matches: {all_matches}")
print(f"Total: {total}")
