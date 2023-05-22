import pytest
from module_example import fetch_data, process_data


@pytest.mark.parametrize("fetch_data_return, expected_result", [
    ("Dados de teste", "Dados processados corretamente"),
    ("Outros dados de teste", "Dados processados corretamente"),
    ("", "Dados processados com sucesso!")
])
def test_process_data(mocker, fetch_data_return, expected_result):
    mocker.patch('module_example.fetch_data', return_value=fetch_data_return)
    result = process_data()
    assert result == expected_result


if __name__ == "__main__":
    pytest.main([__file__])
