file = open("input", "r")


good_passwords = 0

for line in file.readlines():
    counts, char, word = line.strip().split()

    count_low, count_high = counts.split("-")
    char = char[0]

    num = word.count(char)
    if num>=int(count_low) and num <=int(count_high):
        good_passwords+=1

print(good_passwords)

