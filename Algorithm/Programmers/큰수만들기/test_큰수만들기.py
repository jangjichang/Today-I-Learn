def make_largest_number(number, k):
    start_number = number[:len(number) - k + 1]
    largest_number = remove_one_number_to_make_largest_number(start_number)

    for i in range(len(number) - k + 1, len(number)):
        largest_number = remove_one_number_to_make_largest_number(
            largest_number + number[i])
    return largest_number


def remove_one_number_to_make_largest_number(number):
    for index in range(len(number)-1):
        if number[index] < number[index+1]:
            return number[:index] + number[index+1:]
    return number[:-1]


def test_make_largest_number():
    assert make_largest_number("192", 1) == "92"
    assert make_largest_number("192", 2) == "9"
    assert make_largest_number("1924", 2) == "94"
    assert make_largest_number("1231234", 3) == "3234"
    assert make_largest_number("4177252841", 4) == "775841"


def test_remove_one_number_to_make_largest_number():
    assert remove_one_number_to_make_largest_number("192") == "92"
    assert remove_one_number_to_make_largest_number("912") == "92"
    assert remove_one_number_to_make_largest_number("921") == "92"
    assert remove_one_number_to_make_largest_number("129") == "29"
    assert remove_one_number_to_make_largest_number("19") == "9"
    assert remove_one_number_to_make_largest_number("91") == "9"
