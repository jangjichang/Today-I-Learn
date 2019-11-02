import pytest_watch
import heapq

scoville = [1, 2, 3, 9, 10, 12]
K = 7
output = 2


def test_simple():
    assert solution(scoville, K) == output

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        if scoville[0] >= K:
            return answer
        if len(scoville) == 2:
            least_hot = heapq.heappop(scoville)
            next_least_hot = heapq.heappop(scoville)
            if least_hot + next_least_hot*2 < K:
                return -1
            return answer+1
        least_hot = heapq.heappop(scoville)
        next_least_hot = heapq.heappop(scoville)
        heapq.heappush(scoville, least_hot + next_least_hot*2)
        answer += 1