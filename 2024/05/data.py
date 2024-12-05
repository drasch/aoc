from collections import defaultdict


slines = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47""".split(
    "\n"
)

rules = []
printings = []

with open("input") as file:
    mode = "rules"
    for line in file:
        if mode == "rules":
            if line.strip() == "":
                mode = "printings"
                continue
            rules.append(line.strip())
        else:
            printings.append(line.strip())


def parse_rules(text_rules):
    rules = defaultdict(list)
    for rule in text_rules:
        before, after = list(map(int, rule.split("|")))
        rules[before].append(after)

    return rules


def parse_printings(text_printings):
    printings = []
    for text_printing in text_printings:
        printings.append(list(map(int, text_printing.split(","))))

    return printings


rules = parse_rules(rules)
printings = parse_printings(printings)

__all__ = ["rules", "printings"]
