"""
A simpler version of gh:abstractequalsmagic/romana package for get rid of 
dependicies.

https://github.com/abstractequalsmagic/romana/
"""

ROMAN_LITERALS = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


def roman(roman_lit):
    try:
        literals = [ROMAN_LITERALS[lit] for lit in roman_lit]
    except KeyError:
        return False

    result = literals.pop(0)

    for literal in literals:
        if literal > result:
            result = literal - result
        elif literal <= result:
            result += literal

    return result
