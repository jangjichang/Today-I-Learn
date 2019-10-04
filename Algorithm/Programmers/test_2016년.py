import pytest_watch

a, b = 5, 24
output = "TUE"


def test_simple():
    assert solution(a, b) == output

def solution(a, b):
    month = {
        '1': 31,
        '2': 29,
        '3': 31,
        '4': 30,
        '5': 31,
        '6': 30,
        '7': 31,
        '8': 31,
        '9': 30,
        '10': 31,
        '11': 30,
        '12': 31
    }
    d = {
        '0': 'FRI',
        '1': 'SAT',
        '2': 'SUN',
        '3': 'MON',
        '4': 'TUE',
        '5': 'WED',
        '6': 'THU'
    }
    mon, day = a-1, b-1
    output = 0
    for i in month:
        if int(i) <= mon:
            output += month[i]
    output += day
    output = output % 7
    output = d[str(output)]
    return output