import pytest
from main import two_sum

@pytest.mark.parametrize("lst, target, expected", [
    ([1, 2, 3, 4, 5], 5, (0, 3)),
    ([2, 7, 11, 15], 9, (0, 1)),
    ([3, 2, 4], 6, (1, 2)),
    ([1, 1, 1, 1], 2, (0, 0)),
    ([], 5, ()),
    ([1, 2, 3], 10, ())
])
def test_two_sum(lst, target, expected):
    assert two_sum(lst, target) == expected
