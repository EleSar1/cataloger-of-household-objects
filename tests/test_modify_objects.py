import pytest
from src.handle_data import modify_objects


def test_change_category_only():
    
    """Test 1: Change only the category of an existing object"""
    
    data = {"apple": {"category": "fruit"}}
    expected = {"apple": {"category": "food"}}
    
    result = modify_objects(data, "apple", new_category="food")
    assert result == expected


def test_rename_key_only():
    
    """Test 2: Rename the key of an existing object without changing its category"""

    data = {"apple": {"category": "fruit"}}
    expected = {"banana": {"category": "fruit"}}
    
    result = modify_objects(data, "apple", new_object="banana")
    assert result == expected


def test_rename_and_change_category():

    """Test 3: Rename the key and change the category of an existing object"""

    data = {"apple": {"category": "fruit"}}
    expected = {"banana": {"category": "food"}}
    
    result = modify_objects(data, "apple", "banana", "food")
    assert result == expected


def test_key_not_found():

    """Test 4: Return False if the key to modify is not found anywhere in the nested dictionary"""

    data = {"apple": {"category": "fruit"}}
    
    result = modify_objects(data, "pear", "peach", "food")
    assert result is False


def test_nested_object_modification():

    """Test 6: Raise TypeError if parameters are not as expected"""

    data = {
        "kitchen": {
            "pantry": {
                "box": {"category": "storage"}
            }
        }
    }
    expected = {
        "kitchen": {
            "pantry": {
                "crate": {"category": "food"}
            }
        }
    }

    result = modify_objects(data, "box", "crate", "food")
    assert result == expected



def test_type_errors():
    
    """Test 6: Raise TypeError if parameters are not as expected"""

    # Should raise TypeError because 'data' is not a dictionary
    with pytest.raises(TypeError):
        modify_objects([], "box")

    # Should raise TypeError because 'old_object' is not a string
    with pytest.raises(TypeError):
        modify_objects({}, 123)

    # Should raise TypeError because 'new_object' is not a string or None
    with pytest.raises(TypeError):
        modify_objects({}, "box", new_object=456)

    # Should raise TypeError because 'new_category' is not a string or None
    with pytest.raises(TypeError):
        modify_objects({}, "box", new_category=789)