citations = [4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6]
result = 6


def test_simple():
    assert solution(citations) == result


def solution(citations):
    # citations = sorted(citations, reverse=True)
    # answer = 0
    for value in range(max(citations), 0, -1):
        up = 0
        for i in citations:
            if value <= i:
                up += 1
            if value == up:
                answer = value
                return answer


def solution(citations):
    answer = 0
    length = len(citations)
    h = 0
    k = 0
    citations.sort()

    for i in range(0, length):
        h = citations[i]
        k = length - i
        if k <= h:
            answer = k
            break
    return answer
