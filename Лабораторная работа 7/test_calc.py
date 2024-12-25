from calc import calculate_with_params, write_log, load_settings
from unittest.mock import patch, mock_open
import pytest

def test_load_settings():
    mock_file = mock_open(read_data='tolerance=0.0001\nout=output.txt\n')
    with patch('builtins.open', mock_file):
        expected = {
            "tolerance": "0.0001",
            "out": "output.txt",
        }
        result = load_settings("settings.ini")
        assert result == expected

def test_write_log():
    mock_file = mock_open()
    with patch('builtins.open', mock_file):
        write_log(1, 2, action='+', result=3)
        mock_file().write.assert_called_once_with('+:(1, 2) = 3\n')

def test_write_log_invalid_path():
    with pytest.raises(Exception, match="Ошибка записи в файл"):
        write_log(1, 2, action='+', result=3, file_name='invalid/path/invalid_path.txt')
        