import pytest_watch

N, trust = 11, [[1,8],[1,3],[2,8],[2,3],[4,8],[4,3],[5,8],[5,3],[6,8],[6,3],[7,8],[7,3],[9,8],[9,3],[11,8],[11,3]]
output = -1


def test_simple():
    assert solution(N, trust) == output

def solution(N, trust):
    if N == 1:
        return 1
    answer = -1
    graph = [[] for _ in range(N+1)]
    for pair in trust:
        graph[pair[0]].append(pair[1])
    for idx, value in enumerate(graph):
        if idx != 0 and len(value) == 0:
            for jdx, jvalue in enumerate(graph[1:]):
                if idx != jdx+1:
                    if idx not in jvalue:
                        answer = -1
                        break
                    else:
                        answer = idx
            if answer != -1:
                return answer
    return answer


if __name__ == "__main__":
    solution(N, trust)
