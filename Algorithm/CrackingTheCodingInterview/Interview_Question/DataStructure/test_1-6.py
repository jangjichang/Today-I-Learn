import pytest_watch

input =  "abcdefgggggggg"
# output = 'abcdefggggggg'
output = "a1b1c1d1e1f1g8"


def test_simple():
    assert solution(input) == output

def solution(input):
    output = ""
    continuous = 1
    for idx, value in enumerate(input[:-1]):
        if idx == len(input)-2:
            if value == input[idx+1]:
                output = output + value + str(continuous+1)
                if len(output) > len(input):
                    return input
                return output
            else:
                output = output + input[idx-1] + str(continuous)
                continuous = 1
                output = output + input[idx+1] + str(continuous)
                if len(output) > len(input):
                    return input
                return output
        else:
            if value == input[idx+1]:
                continuous += 1
            else:
                output = output + value + str(continuous)
                continuous = 1
        
