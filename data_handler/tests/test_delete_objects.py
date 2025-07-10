import pytest
from data_handler.handle_data import delete_objects


def test_delete_top_level_key():

    """Test 1: Delete a top-level key from the dictionary"""

    data = {"apple": {"category": "fruit"}, "banana": {"category": "fruit"}}
    expected = {"banana": {"category": "fruit"}}
    result = delete_objects("apple", data)
    assert result == expected


def test_delete_nested_key():

    """Test 2: Delete a key nested inside multiple dictionary levels"""

    data = {
        "kitchen": {
            "pantry": {
                "box": {"category": "storage"},
                "can": {"category": "food"}
            }
        }
    }
    expected = {
        "kitchen": {
            "pantry": {
                "can": {"category": "food"}
            }
        }
    }

    result = delete_objects("box", data)
    assert result == expected


def test_delete_multiple_occurrences():
    
    """Test 3: Delete multiple occurrences of the same key at different nesting levels"""

    data = {
        "box": {"category": "top"},
        "room": {
            "box": {"category": "nested"},
            "drawer": {
                "box": {"category": "deep"}
            }
        }
    }
    expected = {
        "room": {
            "drawer": {}
        }
    }

    result = delete_objects("box", data)
    assert result == expected


def test_key_not_found():

    """Test 4: Return False when the key to delete is not found anywhere in the dictionary"""

    data = {"apple": {"category": "fruit"}}
    result = delete_objects("pear", data)
    assert result is False


def test_type_error_old_key():

    """Test 5: Raise TypeError if 'old_key' parameter is not a string"""

    with pytest.raises(TypeError):
        delete_objects(123, {"apple": {"category": "fruit"}})


def test_type_error_data_not_dict():

    """Test 6: Raise TypeError if 'data' parameter is not a dictionary"""
    
    with pytest.raises(TypeError):
        delete_objects("apple", ["not", "a", "dict"])