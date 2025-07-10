import json
import os 
from data_handler.file_handler import save_JSON_file
import pytest


def test_save_JSON_file_ok():

    """Test 1: Verify that the save_JSON_file function correctly saves the given data to a JSON file"""

    filename = "test_output.json"
    
    data = {
        "kitchen": {"objects": {}},
        "livingRoom": {"objects": {}},
        "bathroom": {"objects": {}},
        "bedroom": {"objects": {}}
    }

    save_JSON_file(data, filename)

    assert os.path.exists(filename)

    with open(filename, mode="r") as f:
        saved_data = json.load(f)

    assert saved_data == data

    os.remove(filename)


def test_type_error():
    
    """Test 2: Ensure that save_JSON_file raises a TypeError when invalid argument types are passed"""

    with pytest.raises(TypeError):
        save_JSON_file(123, 456)