import pytest_watch

progresses, speeds = [93, 30, 55], [1, 30, 5]
answer = [2, 1]


def test_simple():
    assert solution(progresses, speeds) == answer


def solution(progresses, speeds):
    days = list()
    answer = [0]
    for p, s in zip(progresses, speeds):
        day = (100 - p) // s
        if (100 - p) % s:
            day += 1
        days.append(day)
    max = days[0]
    for i in days:
        if i <= max:
            answer[-1] += 1
        else:
            max = i
            answer.append(1)
    return answer

if __name__ == "__main__":
    solution(progresses, speeds)
"""
7 3 9

days = 100 - progresses[i] / speeds[i]
if 100 - progresses[i] // speeds[i]:
    days += 1


"""