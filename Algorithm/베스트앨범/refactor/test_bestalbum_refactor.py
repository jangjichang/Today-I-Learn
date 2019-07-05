genres = ["classic", "pop", "classic", "classic", "pop"] # , "hiphop", "hiphop"
plays = [500, 600, 150, 800, 2500] # , 1000, 500
returns = [4, 1, 3, 0]


def test_simple():
    assert solution(genres, plays) == returns


def solution(genres, plays):
    genres_sum = dict()
    for i in zip(genres, plays, range(0, len(genres))):
        genres_sum[(i[0])] = genres_sum.get(i[0], 0) + i[1]
    genres_sum = sorted(genres_sum.items(), key=lambda x: x[1], reverse=True)
    answers = list()
    for genre in genres_sum:
        temp = gather_specific_genre(zip(genres, plays, range(0, len(genres))), list(), genre)
        add_max_two(temp, answers)
    return answers


def gather_specific_genre(zipped, temp, genre):
    for genre_plays in zipped:
        temp = check_value_then_append(genre_plays, genre, temp)
    temp = sorted(temp, key=lambda x: x[1], reverse=True)
    return temp


def check_value_then_append(origin, target, result):
    if origin[0] == target[0]:
        result.append(origin)
    return result


def add_max_two(temp, results):
    results.append(temp[0][2])
    temp.pop(0)
    if temp:
        results.append(temp[0][2])
    return results


if __name__ == '__main__':
    solution(genres, plays)
