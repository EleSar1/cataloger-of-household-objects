import json
import os
import pytest
from data_handler.file_handler import load_JSON_file


def test_load_valid_JSON():

    """Test 1: Load a valid JSON file and check if the content is correctly read"""

    filename = "test_valid.json"
    with open(filename, mode="w") as f:
        json.dump({"test": 123}, f)

    data = load_JSON_file(filename)
    assert data == {"test": 123}

    os.remove(filename)


def test_load_invalid_JSON_initialize_file():


    """Test 2: Load an invalid JSON file, expect the function to initialize it with a default structure
           and verify that the file is overwritten with the default content"""

    filename = "test_invalid.json"
    with open(filename, mode="w") as f:
        f.write("{ invalid")

    data = load_JSON_file(filename)

    expected_structure = {
        "kitchen": {"objects": {}},
        "livingRoom": {"objects": {}},
        "bathroom": {"objects": {}},
        "bedroom": {"objects": {}}
    }

    assert data == expected_structure

    with open(filename, mode="r") as f:
        saved = json.load(f)

    assert saved == expected_structure

    os.remove(filename)


def test_type_error_on_non_string_filename():
    
    """Test 3: Raise TypeError when the filename parameter is not a string"""
    
    with pytest.raises(TypeError):
        load_JSON_file(123)