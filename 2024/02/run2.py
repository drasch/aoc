lines = []

with open("input") as file:
    for line in file: 
        line = line.strip()
        lines.append(line)

dlines = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
""".split("\n")


lines = [[int(num) for num in line.split()] for line in lines if len(line) > 0]

is_sorted = lambda l: all(l[i] <= l[i+1] for i in range(len(l) - 1))

is_safe_dist = lambda l: all(abs(l[i]-l[i+1]) in {1, 2, 3} for i in range(len(l) - 1))

is_safe = lambda l: is_safe_dist(l) and (is_sorted(l) or is_sorted(list(reversed(l))))

lists_minus_one = lambda l: [l[0:i] + l[i+1:] for i in range(len(l))] 

is_safe_fixer = lambda l: any([is_safe(l_test) for l_test in [l] + lists_minus_one(l)])

# for l in lines:
#     print(l)
#     print(is_sorted(l))
#     print(is_sorted(list(reversed(l))))
#     print(is_safe_dist(l))

print(len([1 for l in lines if is_safe_fixer(l)]))
