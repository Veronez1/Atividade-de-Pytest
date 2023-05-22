import hypothesis
from hypothesis import given
from hypothesis.strategies import integers


def square(x):
    return x ** 2


@hypothesis.given(integers())
def test_square(x):
    result = square(x)
    assert result == x ** 2
