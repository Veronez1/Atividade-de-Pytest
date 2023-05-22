import pytest
from unittest.mock import MagicMock


class CustomDependency:
    def custom_operation(self):
        return 99


def perform_operation(dependency):
    result = dependency.custom_operation()
    return result


def test_perform_operation():
    mock_dependency = MagicMock(spec=CustomDependency)
    mock_dependency.custom_operation.return_value = 99

    result = perform_operation(mock_dependency)

    assert result == 99
    mock_dependency.custom_operation.assert_called_once()
