file = open("input.txt", "r").readlines()

# Search string
string1 = "XMAS"
string2 = "SAMX"

# Total
xmas_count: int = 0


# Search left and right
for line in file:
    if string1 in line:
        xmas_count += 1
    if string2 in line:
        xmas_count += 1

# Search up and down
for idx_l, line in enumerate(file):
    for idx_c, column in enumerate(line):
        try:
            if (
                file[idx_l][idx_c] == "X"
                and file[idx_l + 1][idx_c] == "M"
                and file[idx_l + 2][idx_c] == "A"
                and file[idx_l + 3][idx_c] == "S"
            ):
                xmas_count += 1
            if (
                file[idx_l][idx_c] == "S"
                and file[idx_l + 1][idx_c] == "A"
                and file[idx_l + 2][idx_c] == "M"
                and file[idx_l + 3][idx_c] == "X"
            ):
                xmas_count += 1
        except IndexError:
            pass

# Search diagonal
for idx_l, line in enumerate(file):
    line = line.strip()
    for idx_c, column in enumerate(line):
        # Down and right: XMAS
        try:
            if (
                file[idx_l][idx_c]
                + file[idx_l + 1][idx_c + 1]
                + file[idx_l + 2][idx_c + 2]
                + file[idx_l + 3][idx_c + 3]
                == "XMAS"
            ):
                xmas_count += 1
        except IndexError:
            pass
        # Down and right: SAMX
        try:
            if (
                file[idx_l][idx_c]
                + file[idx_l + 1][idx_c + 1]
                + file[idx_l + 2][idx_c + 2]
                + file[idx_l + 3][idx_c + 3]
                == "SAMX"
            ):
                xmas_count += 1
        except IndexError:
            pass

        # Down and left: XMAS
        try:
            if idx_c >= 3:
                if (
                    file[idx_l][idx_c]
                    + file[idx_l + 1][idx_c - 1]
                    + file[idx_l + 2][idx_c - 2]
                    + file[idx_l + 3][idx_c - 3]
                    == "XMAS"
                ):
                    xmas_count += 1
        except IndexError:
            pass

        # Down and left: SAMX
        try:
            if idx_c >= 3:
                if (
                    file[idx_l][idx_c]
                    + file[idx_l + 1][idx_c - 1]
                    + file[idx_l + 2][idx_c - 2]
                    + file[idx_l + 3][idx_c - 3]
                    == "SAMX"
                ):
                    xmas_count += 1
        except IndexError:
            pass

print(f"Total: {xmas_count}")
