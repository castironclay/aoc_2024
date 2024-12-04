import re

total = 0
all_matches = 0
with open("input.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    # Remove sections between a don't() and a do()
    line = re.sub(r"don't\(\).*?do\(\)", "", line)
    # Remove trailing part of line after don't()
    ## If there was a trailing do() then this section would exist
    ## Can safetly assume there is no trailing do()
    line = re.sub(r"don't\(\).*$", "", line)
    print(line)
    matches = re.findall(r"mul\(\d+,\d+\)", line)
    all_matches += len(matches)
    for match in matches:
        numbers = re.findall(r"\d+", match)
        value = int(numbers[0]) * int(numbers[1])
        total += value

print(f"Total Matches: {all_matches}")
print(f"Total: {total}")
# 106266128
