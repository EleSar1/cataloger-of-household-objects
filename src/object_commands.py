from src.file_handler import save_JSON_file
from src.handle_data import add_object, delete_objects, modify_objects


def type_check(func) -> function:

    def wrapper(filename, data) -> function:

        if not isinstance(filename, str):
            raise TypeError("Expected a str for 'filename' parameter, got a different type.")
        if not isinstance(data, dict):
            raise TypeError("Expected a dict for 'data' parameter, got a different type.")

        return func(filename, data)

    return wrapper


@type_check
def handle_object_addition(filename: str, data: dict) -> None:
    
    print("Please, enter")
    location_path = []
    print("The location path (e.g., 'bedroom', 'closet'):")
        
    location = None
    while location != "":
        location = input("(enter a blank line to stop) -> ")
        if location == "":
                print("Stopped.")
        else:
            location_path.append(location)

    print("\nPlease enter the name of the new object.")
    name = input("-> ")

    print("\nPlease enter the object category.")
    category = input("-> ")

    new_data = add_object(data, location_path, name, category)
        
    if new_data:
        save_JSON_file(new_data, filename)
        print("\nData saved successfully!")
    else: 
        print("\nUnexpected error: wrong location path.")


@type_check
def handle_object_modification(filename: str, data: dict) -> None:
    
    print("Press [1] to modify an object.")
    print("Press [2] to modify a category.")

    modification = 0
    while modification not in [1, 2]:
        try:
            modification = int(input("-> "))
            if modification not in [1, 2]:
                print("Number out of range, enter 1 or 2.")
        except ValueError:
            print("Input must be an integer.")

    if modification == 1:
            
        old_object = input("\nPlease enter the name of the object that you want to modify.\n-> ") 
        new_object = input("Please enter the new object name.\n-> ")

        new_data = modify_objects(data, old_object, new_object)

        if new_data:
            save_JSON_file(new_data, filename)
            print("Data saved successfully!")
        else:
            print("Error: data not found.") 
    
    elif modification == 2:
            
        old_object = input("\nPlease enter the name of the object you want to change the category for.\n-> ")
        new_category = input("Please enter the new category name.\n-> ")

        new_data = modify_objects(data, old_object, new_category=new_category)

        if new_data:
            save_JSON_file(new_data, filename)
            print("Data saved successfully!")
        else:
            print("Error: data not found.") 


@type_check
def handle_object_deletion(filename: str, data: dict) -> None:
    
    print("Which object do you want to delete?")
    key_to_delete = input("-> ")
    new_data = delete_objects(key_to_delete, data)

    if new_data:
        save_JSON_file(new_data, filename)
        print("Object eliminated!")
    else:
        print("An error occurred. Please check if the object name is correct.")