# Parse data
from collections import defaultdict
with open('data\\day5_input.txt', 'r') as f:
    data = f.read().splitlines()

blank_line = data.index('')
rules_text = data[:blank_line]
orderings_text = data[blank_line+1:]

# # Example data
# rules_text = """47|53
# 97|13
# 97|61
# 97|47
# 75|29
# 61|13
# 75|53
# 29|13
# 97|29
# 53|29
# 61|53
# 97|53
# 61|29
# 47|13
# 75|47
# 97|75
# 47|61
# 75|61
# 47|29
# 75|13
# 53|13""".splitlines()

# orderings_text = """75,47,61,53,29
# 97,61,53,29,13
# 75,29,13
# 75,97,47,61,53
# 61,13,29
# 97,13,75,29,47""".splitlines()

# keys are pages which must come first; values are pages which must come after
rules = defaultdict(list) 
# So if a key appears in the proposed ordering, there should be no entries in the values list before it. 
for rule_text in rules_text:
    prior,after = [int(x) for x in rule_text.split('|')]
    rules[prior].append(after)

orderings = [[int(x) for x in ordering.split(',')] for ordering in orderings_text]

middle_pages=[]
invalid_orderings = []
for ordering in orderings:
    valid = True
    for idx, entry in enumerate(ordering):
        if entry in rules.keys():
            prior_pages = ordering[:idx]
            for prior_page in prior_pages:
                if prior_page in rules[entry]:
                    valid = False
                    break
            else:
                continue
    if valid:
        middle_page = ordering[(len(ordering)+1)//2-1]
        middle_pages.append(middle_page)
    else:
        invalid_orderings.append(ordering)

print(sum(middle_pages))

# Part 2
# Sort the incorrect orderings so that they become correct, and again sum the middle pages
middle_pages=[]
for ordering in invalid_orderings:
    for idx, entry in enumerate(ordering):
        if entry in rules.keys():
            prior_pages = ordering[:idx]
            pages_to_move = [p for p in prior_pages if p in rules[entry]]
            # Reassemble the ordering
            prior_pages = [p for p in prior_pages if p not in pages_to_move]
            ordering = prior_pages + [entry] + pages_to_move + ordering[idx+1:]
    middle_pages.append(ordering[(len(ordering)+1)//2-1])

print(sum(middle_pages))