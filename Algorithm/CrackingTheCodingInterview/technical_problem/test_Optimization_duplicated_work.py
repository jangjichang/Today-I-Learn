def solution_pre_create_possible_key_value_in_hash_table(input):
    """
    시간복잡도
    O(n^2)
    """
    hash_table = dict()
    for c in range(1, input):
        for d in range(1, input):
            result = c**3 + d**3
            try:
                hash_table[result].append((c, d))
            except:
                hash_table[result] = [(c, d)]
    for a in range(1, input):
        for b in range(1, input):
            result = a**3 + b**3
            matched_tuple = hash_table.get(result)
            for i in matched_tuple:
                print((a, b), i)


def solution_not_loop_with_c_d(input):
    """
    시간복잡도
    O(n^2)

    위의 코드에서 아래 for loop 중복되는 작업 제거
    """
    hash_table = dict()
    for c in range(1, input):
        for d in range(1, input):
            result = c**3 + d**3
            try:
                hash_table[result].append((c, d))
            except:
                hash_table[result] = [(c, d)]
    for key, value in hash_table.items():
        for i in value:
            for j in value:
                print(i, j)

if __name__ == "__main__":
    input = 100
    # solution_pre_create_possible_key_value_in_hash_table(input)
    solution_not_loop_with_c_d(input)
