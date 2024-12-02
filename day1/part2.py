left_list: list = []
right_list: list = []
total: int = 0

with open("part2_input.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        # 0 and 3 indices
        left_list.append(line.split(" ")[0].strip())
        right_list.append(line.split(" ")[3].strip())

for number in left_list:
    matching = [x for i, x in enumerate(right_list) if x == number]
    total += int(number) * len(matching)

print(total)
