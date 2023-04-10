

# Padlock Code - 1st Challenge
def first_challenge():
    """code = 1 + 2 + 3 + 4 + … + 38 + 39 + 40"""
    code = 0
    for i in range(1, 41):
        code += i
    print(f"Code: {code}")


# Padlock Code - 2nd Challenge

def second_challenge():
    """code = Total number of 3-digit combinations where digit1 < digit2 < digit3

e.g. 123 and 358 count as valid combinations whereas 321 or 011 are invalid combinations."""
    code = 0
    for digit1 in range(0, 10):
        for digit2 in range(0, 10):
            for digit3 in range(0, 10):
                if digit1 < digit2 and digit2 < digit3:
                    code += 1
    print(f"Code: {code}")

# Padlock Code - 2nd Challenge


def third_challenge():
    """code = Total number of 3-digit combinations where digit1, digit2 and digit3 are all even numbers

e.g. 024 and 886 count as valid combinations whereas 124 or 456 are invalid combinations."""
    code = 0
    for digit1 in range(0, 10):
        for digit2 in range(0, 10):
            for digit3 in range(0, 10):
                if digit1 % 2 == 0 and digit2 % 2 == 0 and digit3 % 2 == 0:
                    code += 1
    print(f"Code: {code}")

# Padlock Code - 2nd Challenge


def fourth_challenge():
    """code = Total number of 3-digit combinations where the sum of all three digits (digit1 + digit2 + digit3) is an odd number

e.g. 034 and 555 count as valid combinations whereas 123 or 468 are invalid combinations."""
    code = 0
    for digit1 in range(0, 10):
        for digit2 in range(0, 10):
            for digit3 in range(0, 10):
                sum = digit1 + digit2 + digit3
                if sum % 2 != 0:
                    code += 1
    print(f"Code: {code}")

 # Padlock Code - 2nd Challenge


def fifth_challenge():
    """code = Total number of 3-digit combinations where at least two digits are equal.

e.g. 030 and 558 count as valid combinations whereas 123 or 468 are invalid combinations."""
    code = 0
    for digit1 in range(0, 10):
        for digit2 in range(0, 10):
            for digit3 in range(0, 10):
                if digit1 == digit2 or digit2 == digit3 or digit3 == digit1:
                    code += 1
    print(f"Code: {code}")


first_challenge()
second_challenge()
third_challenge()
fourth_challenge()
fifth_challenge()
