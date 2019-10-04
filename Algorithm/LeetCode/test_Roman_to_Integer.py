import pytest_watch

input = "MCMXCIV"
output = 1994


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
    
    while True:
        if idx > len(s)-1:
            return output
        else:
            if s[idx] == 'I':
                if idx == len(s)-1:
                    output += 1
                    return output
                if s[idx+1] == 'V':
                    output += 4
                    idx += 2
                elif s[idx+1] == 'X':
                    output += 9
                    idx += 2
                else:
                    output +=1
                    idx += 1
            elif s[idx] == 'X':
                if idx == len(s)-1:
                    output += 10
                    return output
                if s[idx+1] == 'L':
                    output += 40
                    idx += 2
                elif s[idx+1] == 'C':
                    output += 90
                    idx += 2
                else:
                    output += 10
                    idx += 1
            elif s[idx] == 'C':
                if idx == len(s)-1:
                    output += 100
                    return output
                if s[idx+1] == 'D':
                    output += 400
                    idx += 2
                elif s[idx+1] == 'M':
                    output += 900
                    idx += 2
                else:
                    output += 100
                    idx += 1
            else:
                if s[idx] == 'V':
                    output += 5
                    idx += 1
                elif s[idx] == 'L':
                    output += 50
                    idx += 1
                elif s[idx] == 'D':
                    output += 500
                    idx += 1
                elif s[idx] == 'M':
                    output += 1000
                    idx += 1

if __name__ == "__main__":
    solution(input)
