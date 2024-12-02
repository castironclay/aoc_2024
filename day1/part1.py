left_list: list = []
right_list: list = []
total: int = 0

with open("part1_input.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        # 0 and 3 indices
        left_list.append(line.split(" ")[0].strip())
        right_list.append(line.split(" ")[3].strip())

left_list = sorted(left_list)
right_list = sorted(right_list)

for index, number in enumerate(left_list):
    total += abs(int(number) - int(right_list[index]))

print(total)
