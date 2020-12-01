input = []
with open("input", "r") as f:
    input = f.readlines()

numbers = [int(line) for line in input]

for i1, n1 in enumerate(numbers):
    for i2, n2 in enumerate(numbers):
        if n1+n2 == 2020:
            print(n1*n2)
            break
    else:
        continue
    break
