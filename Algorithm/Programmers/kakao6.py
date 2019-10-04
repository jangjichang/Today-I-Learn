

import collections

m = 6
n = 6
board = ["TTTANT",
         "RRFACC",
         "RRRFCC",
         "TRRRAA",
         "TTMMMF",
         "TMMTTJ"]


def crashable(m, n, board):
    table = [[0 for x in range(n)] for y in range(m)]
    for i in range(m):
        for j in range(n):
            table[i][j] = board[i][j]

    sameblock = list()
    for j in range(m-1):
        for i in range(n-1):
            if table[i][j] != '#':
                if table[i][j] == table[i][j+1] and table[i][j] == table[i+1][j+1] and table[i][j] == table[i+1][j]:
                    if {i: j} not in sameblock:
                        sameblock.append({i: j})
                    if {i+1: j} not in sameblock:
                        sameblock.append({i+1: j})
                    if {i: j+1} not in sameblock:
                        sameblock.append({i: j+1})
                    if {i+1: j+1} not in sameblock:
                        sameblock.append({i+1: j+1})

    for k in sameblock:
        for key, value in k.items():
            table[key][value] = '#'

    for q in table:
        space = q.count('#')
        for i in range(space):
            q.remove('#')

        for j in range(space):
            q.append('#')

    for i in range(m):
        str = ""
        for j in range(n):
            str += table[i][j]
        board[i] = str

    returnvalue = len(sameblock)
    sameblock.clear()
    return returnvalue








def solution(m, n, board):
    check = crashable(m, n, board)
    if not check:
        return 0
    else:
        return check + solution(m, n, board)


print(solution(m,n,board))


# def board2table(m, n, board):
#     table = [[0 for x in range(n)] for y in range(m)]
#     for i in range(m):
#         for j in range(n):
#             table[i][j] = board[i][j]
#     return table





# def crashable(m, n, board):
#     table = [[0 for x in range(n)] for y in range(m)]
#     for i in range(m):
#         for j in range(n):
#             table[i][j] = board[i][j]
#
#     sameblock = list()
#     for i in range(m-1):
#         for j in range(n-1):
#             if table[i][j] == table[i][j+1] and table[i][j] == table[i+1][j+1] and table[i][j] == table[i+1][j]:
#                 if {i: j} not in sameblock:
#                     sameblock.append({i: j})
#                 if {i+1: j} not in sameblock:
#                     sameblock.append({i+1: j})
#                 if {i: j+1} not in sameblock:
#                     sameblock.append({i: j+1})
#                 if {i+1: j+1} not in sameblock:
#                     sameblock.append({i+1: j+1})
#
#     for k in sameblock:
#         for key, value in k.items():
#             table[key][value] = '#'
#
#     for q in table:
#         space = q.count('#')
#         for i in range(space):
#             q.remove('#')
#
#         for j in range(space):
#             q.append('#')
#     returnvalue = len(sameblock)
#     sameblock.clear()
#     return returnvalue
#
#
# def solution(m, n, board):
#     check = crashable(m, n, board)
#     if not check:
#         return 0
#     else:
#         return check + solution(m, n, board)
#
#
# print(solution(m,n,board))