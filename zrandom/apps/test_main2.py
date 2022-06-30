from ..main2 import sub, word_count


def test_sub():
    assert sub(3, 4) == -1
    assert sub(4.5, 4) == 0
    assert sub(3.9, 4) == -1
    assert sub(4.2, 3.8) == 0


def test_word_count():
    assert word_count("arm pod race", "pod") == 1
    assert word_count("arm pod race", "lap") == 0
    assert word_count("arm arm arm", "arm") == 3
