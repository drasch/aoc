from data import rules, printings


def key_for_sort(rules):
    class Page:
        num = None

        def __init__(self, num):
            self.num = num

        def __lt__(self, other):
            return other.num in rules[self.num]

    return Page


def find_failed_rules(page, printing, rules):
    return [after for after in rules[page] if after in printing]


def check_page_order(page, printing, rules):
    return len(find_failed_rules(page, printing, rules)) == 0


print(
    "part 1: "
    + str(
        sum(
            [
                printing[len(printing) // 2]
                for printing in printings
                if all(
                    [
                        check_page_order(page, printing[: index + 1], rules)
                        for index, page in enumerate(printing[1:])
                    ]
                )
            ]
        )
    )
)

sum = 0
for printing in printings:
    if not all(
        [
            check_page_order(page, printing[: index + 1], rules)
            for index, page in enumerate(printing[1:])
        ]
    ):
        klass = key_for_sort(rules)
        reordered = sorted(printing, key=klass)
        sum += reordered[len(reordered) // 2]

print(f"part 2: {sum}")
