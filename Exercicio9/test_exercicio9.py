import pytest
from concurrent.futures import ProcessPoolExecutor

@pytest.mark.parametrize("input, expected", [(1, 2), (2, 3), (3, 4)])
def test_increment(input, expected):
    assert input + 1 == expected

def increment(x):
    return x + 1

def test_parallel():
    inputs = [1, 2, 3, 4]
    expected_results = [2, 3, 4, 5]

    with ProcessPoolExecutor() as executor:
        results = executor.map(increment, inputs)

    assert list(results) == expected_results
#pip install pytest-xdist
#pytest -n 4
