
import time

def test_addition():
    assert 2 + 2 == 4

def test_subtraction():
    assert 5 - 3 == 2

def test_multiplication():
    assert 4 * 3 == 12

def test_long_running():
    time.sleep(2)  # Simulando um teste que leva 2 segundos para ser executado
    assert 10 / 2 == 5
