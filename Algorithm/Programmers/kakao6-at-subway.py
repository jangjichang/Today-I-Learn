# m = 4   # 높이
# n = 5   # 너비
# board = ["CCBDE",
#          "AAADE",
#          "AAABF",
#          "CCBBF"]
m = 6
n = 6
board = ["TTTANT",
         "RRFACC",
         "RRRFCC",
         "TRRRAA",
         "TTMMMF",
         "TMMTTJ"]

def board2table(m, n, board):
    t = [[0 for x in range(m)] for y in range(n)]
    for i in range(m):
        for j in range(n):
            t[j][i] = board[i][j]
    return t


def crashable(n, m, table):
    sameblock = list()
    for i in range(m - 1):
        for j in range(n - 1):
            if table[i][j] != '#':
                if table[i][j] == table[i][j + 1] and table[i][j] == table[i + 1][j + 1] and table[i][j] == \
                        table[i + 1][j]:
                    if {i: j} not in sameblock:
                        sameblock.append({i: j})
                    if {i + 1: j} not in sameblock:
                        sameblock.append({i + 1: j})
                    if {i: j + 1} not in sameblock:
                        sameblock.append({i: j + 1})
                    if {i + 1: j + 1} not in sameblock:
                        sameblock.append({i + 1: j + 1})

    for k in sameblock:
        for key, value in k.items():
            table[key][value] = '#'

    for i in table:
        space = i.count('#')
        if space:
            for j in range(space):
                i.remove('#')
            for k in range(space):
                i.insert(0, '#')

    returnvalue = len(sameblock)
    sameblock.clear()
    return returnvalue


def sol(m, n, t):
    check = crashable(m, n, t)
    if not check:
        return 0
    else:
        return check + sol(m, n, t)


def solution(m, n, board):
    m = m
    n = n
    board = board
    t = board2table(m, n, board)
    answer = sol(m, n, t)
    return answer


print(solution(m, n, board))