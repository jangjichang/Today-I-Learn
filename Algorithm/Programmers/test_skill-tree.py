def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        filtered_skill_tree = []
        for character in skill_tree:
            if character in skill:
                filtered_skill_tree.append(character)
        if skill.startswith(''.join(filtered_skill_tree)):
            answer += 1
    return answer


def test_solution():
    assert solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]) == 2
