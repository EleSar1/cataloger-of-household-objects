import pytest
from src.handle_data import explore_data


def test_nested_structure_output(capsys):

    """Test 1: checks correct output formatting for a nested dictionary"""
    data = {'level1': {'level2': {'level3': {'key': 'value'}}}}

    explore_data(data)

    stdout, _ = capsys.readouterr()
    expected = 'level1:\n   level2:\n      level3:\n         key: value\n'
    assert stdout == expected


def test_empty_dict(capsys):

    """Test 2: checks correct output formatting for an empty dictionary"""

    explore_data({})

    stdout, _ = capsys.readouterr()
    assert stdout == ''


def test_mixed_dict(capsys):

    """Test 3: checks correct output formatting for a dictionary with both nested and flat keys"""

    explore_data({'key1': {'key2': 1}, 'key3': 2})

    stdout, _ = capsys.readouterr()
    expected = 'key1:\n   key2: 1\nkey3: 2\n'
    assert stdout == expected


def test_not_nested_dict(capsys):

    """Test 4: checks correct output formatting for a dictionary with flat keys"""

    explore_data({'key1': 1, 'key2': 2, 'key3': 3})

    stdout, _ = capsys.readouterr()
    expected =  'key1: 1\nkey2: 2\nkey3: 3\n'
    assert stdout == expected


def test_invalid_data_type():

    """Test 5: raises TypeError when 'data' is not a dictionary."""

    with pytest.raises(TypeError, match="Expected 'data' to be a dict."):
        explore_data("not a dict")


def test_invalid_level_type():

    """Test 6: raises TypeError when 'level' is not an integer."""
    
    with pytest.raises(TypeError, match="Expected 'level' to be an int."):
        explore_data({}, level="not an int")