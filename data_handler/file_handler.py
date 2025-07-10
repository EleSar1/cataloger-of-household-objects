import os
import json


def load_JSON_file(filename: str) -> dict:

    """
    Load data from a JSON file. If the file is missing or contains invalid JSON,
    it initializes the file with an empty dictionary and saves it.

    Parameters:
        filename (str): Path to the JSON file to load.

    Returns:
        dict: The data loaded from the JSON file. If the file is corrupted,
              an empty dictionary is returned and saved to the file.
    """

    if not isinstance(filename, str):
        raise TypeError("Expected a string, got a non-string.")

    try:
        with open(filename, mode="r") as file:
            file_info = json.load(file)
    
    except json.JSONDecodeError:
        print("File JSON is corrupted. Will be initialized again.")
        file_info = {
            "kitchen": {
                "objects": {}
            }, 
            "livingRoom": {
                "objects": {}
            }, 
            "bathroom": {
                "objects": {}
            },
            "bedroom": {
                "objects": {}
            }
        }
        
        save_JSON_file(file_info, filename)
        
    return file_info


def save_JSON_file(data: dict, filename: str):

    """
    Saves a dictionary to a JSON file with indentation for readability.

    Parameters:
        data (dict): The data to be saved to the JSON file.
        filename (str): The name of the file where the data will be saved.
    """
    
    if not isinstance(data, dict):
        raise TypeError("Expected 'data' to be a dictionary.")
    if not isinstance(filename, str):
        raise TypeError("Expected 'filename' to be a string.")
    
    with open(filename, mode="w") as file:
        json.dump(data, file, indent=4)