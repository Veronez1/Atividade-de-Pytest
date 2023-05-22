import pytest


class TestExample:
    configurations = [
        {'param1': 1, 'param2': -1},
        {'param1': 2, 'param2': -2},
        {'param1': 3, 'param2': -3}
    ]

    @pytest.mark.parametrize('config', configurations)
    class TestMultiplication:
        @staticmethod
        def multiply(a, b):
            return a * b

        @staticmethod
        def neg_multiply(a, b):
            return -abs(TestMultiplication.multiply(a, b))

        def test_multiplication_positive(self, config):
            param1 = config['param1']
            param2 = config['param2']
            assert TestMultiplication.multiply(param1, param2) == TestMultiplication.multiply(param2, param1)

        def test_multiplication_negative(self, config):
            param1 = config['param1']
            param2 = config['param2']
            assert TestMultiplication.multiply(param1, param2) == TestMultiplication.neg_multiply(param1, param2)
