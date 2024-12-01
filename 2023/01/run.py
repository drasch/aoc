words = []

with open("input") as file:
    for line in file: 
        word = line.strip()
        words.append(word)

filtered = [[c for c in word if c.isnumeric()] for word in words]

print(sum([int(word[0] + word[-1]) for word in filtered]))
