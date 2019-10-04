import pytest_watch

# input = "MCMXCIV"
# output = 1994
input = "III"
output = 3


def test_simple():
    assert solution(input) == output

def solution(s):
    roman_numerals = {
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900,
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    output = 0
    idx = 0

    while idx < len(s):
        try:
            output += roman_numerals[s[idx] + s[idx+1]]
            idx += 2
        except (KeyError, IndexError):
            output += roman_numerals[s[idx]]
            idx += 1
    return output

    

if __name__ == "__main__":
    solution(input)
