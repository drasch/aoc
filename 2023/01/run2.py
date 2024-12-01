import re

conversion = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

conversion = conversion | {str(c): c for c in range(1,10)}

words = []

with open("input") as file:
    for line in file: 
        word = line.strip()
        words.append(word)

filtered = [[conversion[token] for token in re.findall("(?=("+"|".join(conversion.keys())+"))", word)] for word in words]
print(filtered[0])
print(sum([int(str(word[0]) + str(word[-1])) for word in filtered]))
