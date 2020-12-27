input = open("day4-input.txt", "r")
passports = input.read().split("\n\n")

required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def validity_test(passport_fields: dict) -> bool:
    missing_field = False
    for field in required_fields:
        if field not in passport_fields:
            missing_field = True
            break
    return not (missing_field)


def process_fields(passport: str) -> list:
    extract1 = passport.split(" ")
    fields = []
    for i in extract1:
        fields = fields + i.split("\n")
    return fields


### Part 1 ###
valid_passports = 0
for passport in passports:
    # Extract all relevant parameters
    fields = process_fields(passport)

    # Determine if passport contains all necessary fields
    passport_fields = dict(f.split(":") for f in fields)
    validity = validity_test(passport_fields)
    if validity == True:
        valid_passports = valid_passports + 1

print(f"Part 1: The number of valid passports is {valid_passports}")


### Part 2 ###
valid_and_verified_passports = 0
for passport in passports:
    # Extract all relevant parameters
    fields = process_fields(passport)

    # Determine if passport has all required fields
    passport_fields = dict(f.split(":") for f in fields)
    validity = validity_test(passport_fields)

    # Proceed to validation checks
    if validity == True:
        # Birth year validation
        verification_status = True
        birth_year = int(passport_fields["byr"])
        if birth_year < 1920 or birth_year > 2002:
            verification_status = False

        # Issue year validation
        if verification_status == True:
            issue_year = int(passport_fields["iyr"])
            if issue_year < 2010 or issue_year > 2020:
                verification_status = False

        # Expiration year validation
        if verification_status == True:
            expiration_year = int(passport_fields["eyr"])
            if expiration_year < 2020 or expiration_year > 2030:
                verification_status = False

        # Height validation
        if verification_status == True:
            height = passport_fields["hgt"]
            unit = height[-2:]
            try:
                measurement = int(height[:-2])
                if unit == "cm":
                    if measurement < 150 or measurement > 193:
                        verification_status = False
                elif unit == "in":
                    if measurement < 59 or measurement > 76:
                        verification_status = False
                else:
                    verification_status = False
            except ValueError:
                verification_status = False

        # Hair color validation
        if verification_status == True:
            hair_color = passport_fields["hcl"]
            if hair_color[0] != "#":
                verification_status = False
            if len(hair_color) != 7:
                verification_status = False
            approved_char = (
                "0",
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "a",
                "b",
                "c",
                "d",
                "e",
                "f",
            )
            for c in hair_color[1:]:
                if c not in approved_char:
                    verification_status = False

        # Eye color validation
        if verification_status == True:
            eye_color = passport_fields["ecl"]
            approved_colors = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
            if eye_color not in approved_colors:
                verification_status = False

        # Passport ID validation
        if verification_status == True:
            passport_id = passport_fields["pid"]
            if len(passport_id) != 9:
                verification_status = False
            try:
                id = int(passport_id)
            except ValueError:
                verification_status = False

        if verification_status == True:
            valid_and_verified_passports = valid_and_verified_passports + 1

print(
    f"Part 2: The number of valid and verified passports is {valid_and_verified_passports}"
)
