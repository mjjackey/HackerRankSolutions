import pytest
from test1 import unique_substring_num

@pytest.mark.parametrize(
    "s, k, expected",
    [
        ("abcabc", 3, 3),
        ("aaaa", 2, 1),
        ("abcdefg", 4, 4),
        ("abcabcabc", 2, 3),
        ("", 1, 0),
        ("a", 0, 1),
        ("a", 1, 1),
        ("a", 2, 0),
        ("abc", 3, 1),
        ("abc", 4, 0),
        ("abcabcabc", 9, 1),
        ("abcabcabc", 10, 0),
    ]
)

def test_unique_substring_num(s, k, expected):
    assert unique_substring_num(s, k) == expected

