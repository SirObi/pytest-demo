from myapp.addition import add_two_numbers


def test_add_two_numbers_integers():
    assert add_two_numbers(2, 4) == 6
