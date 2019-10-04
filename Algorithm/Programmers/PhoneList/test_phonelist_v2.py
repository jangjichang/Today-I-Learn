phone_book = [["119", "97674223", "1195524421"],
              ["123", "456", "789"],
              ["12", "123", "1235", "567", "88"]]

result = [False,
          True,
          False]


def test_simple():
    for i in range(len(phone_book)):
        assert sol(phone_book[i]) == result[i]


def sol(pb):
    pb = sorted(pb)
    for key, value in enumerate(pb):
        for values in pb[key+1:]:
            if values.startswith(value):
                return False
    return True

def value_check(value, pb):
    for values in pb:
        if values.startswith(value):
            return False

