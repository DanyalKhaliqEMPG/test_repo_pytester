import sys

from scripts.main import add, sub


def test_add():
    assert add(3, 4) == 7
    assert add(3.5, 4) == 7
    assert add(3.9, 4) == 7
    assert add(3.9, 4.1) == 8


# def test_to_sentence():
# assert main.to_sentence('apple') == 'Apple.'
# assert main.to_sentence('Apple trees') == 'Apple trees.'
# assert main.to_sentence('Apple trees.') == 'Apple trees.'

#
def test_sub():
    assert sub(3, 4) == -1


#     assert main.sub(3.5, 4) == -1
#     assert main.sub(3.9, 4) == -1
#     assert main.sub(3.1, 3) == 0
