import pytest_watch
import heapq


stock = 10
dates = [5, 10]
supplies = [1, 100]
k = 100
output = 1


def test_simple():
    assert solution(stock, dates, supplies, k) == output

def solution(stock, dates, supplies, k):
    answer = 0
    idx = 0
    h = list()
    while stock < k:
        for i in range(idx, len(dates)):
            if stock < dates[i]:
                break
            else:
                heapq.heappush(h, (-supplies[i], supplies[i]))
                idx = i+1
        stock += heapq.heappop(h)[1]
        answer += 1       
    return answer

if __name__ == "__main__":
    print(solution(stock, dates, supplies, k))