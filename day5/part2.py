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


def check_rules(page) -> bool:
    valid = False
    for rule in rules:
        try:
            if page.index(rule[0]) > page.index(rule[1]):
                valid = False
                break
            else:
                valid = True
        except ValueError:
            valid = True

    return valid


def fix_pages(page) -> list:
    for rule in rules:
        try:
            if page.index(rule[0]) > page.index(rule[1]):
                # swap items in list
                page[page.index(rule[0])], page[page.index(rule[1])] = (
                    page[page.index(rule[1])],
                    page[page.index(rule[0])],
                )
        except ValueError:
            pass
    if check_rules(page):
        print(page)
        return page
    else:
        return fix_pages(page)


for pages in manuals:
    if check_rules(pages):
        good_pages.append(pages)
    else:
        bad_pages.append(pages)

fixed_pages: list = []
for page in bad_pages:
    print(f"Fixed: {fix_pages(page)}")
    fixed_pages.append(fix_pages(page))

print(fixed_pages)

# Find middle
total: int = 0
for fixed in fixed_pages:
    item = int(fixed[len(fixed) // 2])
    total += item

print(total)
