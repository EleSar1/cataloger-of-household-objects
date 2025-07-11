from src.file_handler import load_JSON_file
from src.handle_data import explore_data
from src.object_commands import handle_object_addition, handle_object_deletion, handle_object_modification


def main() -> None:

    filename = "data/homeObjects.json"
    data = load_JSON_file(filename)

    print("Current objects in home:\n")
    explore_data(data)

    print("Press:")
    print("[1] if you want to add an object.")
    print("[2] if you want to modify an object or a category.")
    print("[3] if you want to delete an object.")

    choice = 0
    while choice not in range(1, 3+1):
        try:
            choice = int(input("-> "))
            if choice not in range(1, 3+1):
                print("Value not allowed. Enter a number between 1 and 3.")
        except ValueError:
            print("Please enter an integer.")

    if choice == 1:
        handle_object_addition(choice, filename, data)
    elif choice == 2:
        handle_object_modification(choice, filename, data)
    elif choice == 3:
        handle_object_deletion(choice, filename, data)

