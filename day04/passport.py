fields = [field.split()[0] for field in """byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)""".split("\n")]

fields = set(fields) - {"cid"}

file = open("input", "r")
contents = file.read()

valid_records = 0

for record in contents.split("\n\n"):
    raw_fields = record.split()
    print(raw_fields)
    included_fields = {raw_field.split(":")[0] for raw_field in raw_fields}
    print(included_fields)
    print(fields)
    print("\n")

    if fields.issubset(included_fields):
        valid_records += 1

print(valid_records)
