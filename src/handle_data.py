def delete_objects(old_key: str, data: dict) -> dict | bool:
    """
    Recursively deletes all occurrences of a specified key from a nested dictionary.

    Parameters:
        old_key (str): The key to be removed from the dictionary.
        data (dict): The dictionary (possibly nested) from which the key should be removed.

    Returns:
        dict | bool: The updated dictionary with all occurrences of the specified key removed,
                     or False if the key was not found at any level.

    Raises:
        TypeError: If 'old_key' is not a string or 'data' is not a dictionary.
    """

    if not isinstance(old_key, str):
        raise TypeError("Expected 'old_key' to be a str.")

    if not isinstance(data, dict):
        raise TypeError("Expected 'data' to be a dict.")

    found = False

    if old_key in data:
        data.pop(old_key)
        found = True

    for value in data.values():
        if isinstance(value, dict):
            result = delete_objects(old_key, value)
            if result:
                found = True

    return data if found else False


def modify_objects(data: dict, old_object: str, new_object: str=None, new_category: str=None) -> dict | bool:

    """
    Recursively modifies an object in a nested dictionary by optionally renaming its key 
    and/or updating its 'category' field.

    Parameters:
        data (dict): The dictionary (possibly nested) containing the object.
        old_object (str): The key of the object to be modified.
        new_object (str, optional): The new key name for the object. If None, the key is not renamed.
        new_category (str, optional): The new value for the 'category' field. If None, the category is not changed.

    Returns:
        dict: The updated dictionary with the specified modifications applied.
        bool: False if the old_object was not found.
    
    Raises:
        TypeError: If any of the parameters are not of the expected type.
    """
    
    if not isinstance(data, dict):
        raise TypeError(f"Expected 'data' to be a dict.")
    if not isinstance(old_object, str):
        raise TypeError(f"Expected 'old_object' to be a str.")
    if new_object is not None and not isinstance(new_object, str):
        raise TypeError(f"Expected 'new_object' to be a str or None.")
    if new_category is not None and not isinstance(new_category, str):
        raise TypeError(f"Expected 'new_category' to be a str or None.")
    
    if old_object in data:
        if new_category is not None:
            data[old_object]["category"] = new_category
        if new_object is not None:
            data[new_object] = data.pop(old_object)
        return data
    
    for value in data.values(): 
        if isinstance(value, dict):
            result = modify_objects(value, old_object, new_object, new_category)
            if result: 
                return data
    
    return False
        

def explore_data(data: dict, level: int=0) -> None:

    """
    Recursively prints the contents of a nested dictionary in a structured and indented format.

    Parameters:
        data (dict): The dictionary to explore.
        level (int, optional): The current depth level used for indentation. Defaults to 0.

    Prints:
        Keys and values of the dictionary, indented according to their nesting level.

    Raises:
        TypeError: If any of the parameters are not of the expected type.
    """

    if not isinstance(data, dict):
        raise TypeError("Expected 'data' to be a dict.")
    if not isinstance(level, int):
        raise TypeError("Expected 'level' to be an int.")
    
    indent = "   " * level
    for key, value in data.items():

        if isinstance(value, dict):

            print(f"{indent}{key}:")
            explore_data(value, level+1)

        else: 
            print(f"{indent}{key}: {value}")


def add_object(data: dict, location_path: list, name: str, category: str) -> dict | bool:
    
    """
    Adds a new object with a specified name and category to a nested dictionary structure 
    at the given location path.

    Parameters:
        data (dict): The root dictionary containing nested structures.
        location_path (list): A list of keys representing the path to the target location.
        name (str): The name of the new object to add.
        category (str): The category of the new object.

    Returns:
        dict or bool: The updated dictionary if the object was successfully added,
                      or False if the path is invalid or the target does not support objects.
    
    Raises:
        TypeError: If any of the parameters are not of the expected type.
    """

    if not isinstance(data, dict):
        raise TypeError("Expected 'data' to be a dict.")
    if not isinstance(location_path, list):
        raise TypeError("Expected 'location_path' to be a list.")
    if not isinstance(name, str):
        raise TypeError("Expected 'name' to be a str.")
    if not isinstance(category, str):
        raise TypeError("Expected 'category' to be a str.")
    
    current = data
    for key in location_path:
        if key in current:
            current = current[key]
        else:
            return False
        
    if "objects" in current:
        current["objects"][name] = {"category": category}
        return data
    else:
        return False
