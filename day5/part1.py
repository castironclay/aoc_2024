file = open("real.txt", "r").readlines()

rules = []
manuals = []

good_pages: list = []
bad_pages: list = []

for line in file:
    if "|" in line:
        rules.append(line.strip().split("|"))
    elif line == "\n":
        pass
    else:
        manuals.append(line.strip().split(","))


def check_rules(page, rules) -> bool:
    valid = False
    for rule in rules:
        try:
            if page.index(rule[0]) > page.index(rule[1]):
                valid = False
                break
            else:
                valid = True
        except ValueError:
            pass

    return valid


for pages in manuals:
    if check_rules(pages, rules):
        good_pages.append(pages)


total: int = 0
for good in good_pages:
    item = int(good[len(good)//2])
    total += item

print(total)
