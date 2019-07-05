"""

"""
genres = ["classic", "pop", "classic", "classic", "pop"] # , "hiphop", "hiphop"
plays = [500, 600, 150, 800, 2500] # , 1000, 500
returns = [4, 1, 3, 0]


def test_simple():
    assert solution(genres, plays) == returns


def solution(genres, plays):
    # zipped = zip(genres, plays, range(0, len(genres)))
    answer = dict()
    for i in zip(genres, plays, range(0, len(genres))):
        if answer.get(i[0]) is None:
            answer[str(i[0])] = int(i[1])
        else:
            answer[str(i[0])] += int(i[1])
    answer = sorted(answer.items(), key=lambda x: x[1], reverse=True)
    returns = list()
    for genre in answer:
        temp = list()
        for genre_plays in zip(genres, plays, range(0, len(genres))):
            if genre_plays[0] == genre[0]:
                temp.append(genre_plays)
        temp = sorted(temp, key=lambda x: x[1], reverse=True)
        # print(temp)
        if len(temp) >= 2:
            returns.append(temp[0][2])
            returns.append(temp[1][2])
        elif len(temp) == 1:
            returns.append(temp[0][2])

    # print(answer)
    return returns


if __name__ == '__main__':
    solution(genres, plays)
