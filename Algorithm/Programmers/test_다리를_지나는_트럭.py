import pytest_watch

bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]
answer = 8

def test_simple():
    assert solution(bridge_length, weight, truck_weights) == answer

def solution(bridge_length, weight, truck_weights):
    truck_on_a_bridge = []
    truck_past_the_bridge = []
    for i in range(10000*10000*10000):
        if not truck_weights and not truck_on_a_bridge:
            return i
        for i in truck_on_a_bridge:
            i[1] += 1
        for idx, value in enumerate(truck_on_a_bridge[:]):
            if value[1] == bridge_length:
                truck_on_a_bridge.pop(0)
            else:
                break
        if truck_weights:
            if truck_on_a_bridge_sum(truck_on_a_bridge) + truck_weights[0] <= weight:
                truck_on_a_bridge.append([truck_weights[0], 0])
                truck_weights.pop(0)

def truck_on_a_bridge_sum(truck_on_a_bridge):
    sum = 0
    for pair in truck_on_a_bridge:
        sum += pair[0]
    return sum

if __name__ == "__main__":
    a = solution(bridge_length, weight, truck_weights)
    print(a)