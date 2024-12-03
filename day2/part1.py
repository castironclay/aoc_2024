safe_lines: int = 0
with open("input.txt", "r") as file:
    lines = file.readlines()


def determine_safe(numbers: list[int]) -> bool:
    start: int = 1
    going_up: int = 0
    going_down: int = 0
    current_number = numbers[0]
    while start < len(numbers):
        next_number = numbers[start]
        if abs(next_number - current_number) > 3:
            break
        if next_number == current_number:
            break
        if next_number > current_number:
            print("greater")
            going_up += 1
        elif next_number < current_number:
            print("lessthan")
            going_down += 1

        # Set new values and loop again
        current_number = next_number
        start += 1
        print(start)

    # going_up or going_down should equal the length of the list minus 1 only
    # if we had a successful move between each level in the report

    if going_up == len(numbers) - 1:
        return True
    elif going_down == len(numbers) - 1:
        return True
    else:
        return False


number_safe: int = 0
for line in lines:
    line = line.strip()
    numbers: list = line.split(" ")

    # Convert items in list to integers
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])

    if determine_safe(numbers):
        number_safe += 1

print(number_safe)
