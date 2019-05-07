import pytest


"""
각 단어를 순회하며 끝말잇기에 적합한지 확인한다. 끝 알파벳과 시작 알파벳이 같은지 확인.
적합하지 않은 단어를 찾으면 인덱스를 구한다.
인덱스를 몇번째 사람이 몇번째에 말하는지로 변환한다.
"""



def test_simple():
    assert [3, 3] == solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])
    assert [0, 0] == solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"])
    assert [1, 3] == solution(2, ["hello", "one", "even", "never", "now", "world", "draw"])


def solution(n, words):
    index = 0
    checked = []
    for i in words:
        if i in checked:
            return [index % n + 1, index // n + 1]
        else:
            checked.append(i)
            if len(checked) >= 2:
                if checked[-2][-1] != checked[-1][0]:
                    return [index % n + 1, index // n + 1]
        index += 1
    return [0, 0]
