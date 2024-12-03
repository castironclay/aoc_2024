safe_lines: int = 0
with open("input.txt", "r") as file:
    lines = file.readlines()

unsafe_reports: list = []
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
            going_up += 1
        elif next_number < current_number:
            going_down += 1

        # Set new values and loop again
        current_number = next_number
        start += 1

    # going_up or going_down should equal the length of the list minus 1 only
    # if we had a successful move between each level in the report
    safe: bool = False

    if going_up == len(numbers) - 1:
        safe = True
    elif going_down == len(numbers) - 1:
        safe = True

    if safe:
        return safe
    else:
        # Create new list of unsafe reports
        unsafe_reports.append(numbers)

def fix_report(numbers: list[int]) -> bool:
    print(numbers)
    # Loop through list removing an index and testing to see if it is now safe
    # Only remove a single item from the list
    # Otherwise same code as first function
    for i in range(len(numbers)):
        this_round = numbers.copy()
        this_round.pop(i) 
        current_number = this_round[0]
        start: int = 1
        going_up: int = 0
        going_down: int = 0
        while start < len(this_round):
            next_number = this_round[start]
            if abs(next_number - current_number) > 3:
                break
            if next_number == current_number:
                break
            if next_number > current_number:
                going_up += 1
            elif next_number < current_number:
                going_down += 1

            # Set new values and loop again
            current_number = next_number
            start += 1

        # going_up or going_down should equal the length of the list minus 1 only
        # if we had a successful move between each level in the report
        safe: bool = False

        if going_up == len(this_round) - 1:
            safe = True
        elif going_down == len(this_round) - 1:
            safe = True

        if safe:
            return safe



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

for report in unsafe_reports:
    if fix_report(report):
        number_safe += 1

print(number_safe)