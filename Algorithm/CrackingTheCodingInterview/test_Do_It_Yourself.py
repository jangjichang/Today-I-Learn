import pytest_watch

s = "abbc"
b = "cbabadcbbabbcbabaabccbabc"
answer = [0, 6, 9, 11, 12, 20, 21]


def test_simple():
    assert solution(s, b) == answer


def solution(s, b):
    idx = 0
    answer = []
    dict_s = dict()
    for i in s:
        try:
            dict_s[i] += 1
        except:
            dict_s[i] = 1
    
    while idx <= len(b) - len(s):
        dict_d = dict()
        flag = 0
        for index, value in enumerate(b[idx:idx+len(s)]):
            if value not in dict_s:
                idx += index+1
                flag = 1
                break
            try:
                dict_d[value] += 1
            except:
                dict_d[value] = 1
        if dict_d.items() & dict_s.items() == dict_s.items():
            answer.append(idx)
        if not flag:
            idx += 1
    return answer

if __name__ == "__main__":
    solution(s, b)