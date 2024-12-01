import re

def match_height(val):
    match = re.fullmatch(r"(\d{2,3})(in|cm)", val)
    return match and (
            (match.group(2) == "cm" and 150 <= int(match.group(1)) <= 193) or
            (match.group(2) == "in" and 59 <= int(match.group(1)) <= 76)
    )


fields = {
        "byr": lambda val: 1920 <= int(val) <= 2002 and val == str(int(val)),
        "iyr": lambda val: 2010 <= int(val) <= 2020 and val == str(int(val)),
        "eyr": lambda val: 2020 <= int(val) <= 2030 and val == str(int(val)),
        "hgt": match_height,
        "hcl": lambda val: re.fullmatch(r"#[0-9a-f]{6}", val),
        "ecl": lambda val: val in set("amb blu brn gry grn hzl oth".split()),
        "pid": lambda val: re.fullmatch(r"\d{9}", val),
        "cid": lambda _: True
}

file = open("input", "r")
contents = file.read()

valid_records = 0

for record in contents.split("\n\n"):
    raw_fields = record.split()
    vals = dict([raw_field.split(":") for raw_field in raw_fields])
    print(vals)

    if (
            (set(fields.keys()) - {"cid"}).issubset(set(vals.keys()))
            and all([fields[key](vals[key]) for key in vals.keys()])
    ):
        print("VALID")
        valid_records += 1

    print("\n")

print(valid_records)
