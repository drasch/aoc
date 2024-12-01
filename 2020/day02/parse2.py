file = open("input", "r")


good_passwords = 0

for line in file.readlines():
    poss, char, word = line.strip().split()

    pos_one, pos_two = poss.split("-")
    char = char[0]

    if (word[int(pos_one) - 1] == char) != (word[int(pos_two) - 1] == char):
        good_passwords += 1

print(good_passwords)

