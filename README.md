# Cataloger of Household Objects

A Python tool to manage a nested dictionary structure representing objects in different rooms of a house.  
It allows you to **add**, **modify**, and **delete** objects and their categories in a JSON data file.

---

## Features

- **Load and save JSON data** representing rooms and their objects.
- **Explore** and print the nested data structure in a readable format.
- **Add** new objects with a specified name and category at a defined location path.
- **Modify** existing objects by renaming them or changing their category.
- **Delete** objects by their name from any level in the nested structure.
- Recursive and robust handling of nested dictionaries with error checking.

---

## File Structure

- `data_handler/handle_data.py`  
  Contains functions to manipulate the nested dictionary data: adding, modifying, deleting objects, and printing the data.

- `data_handler/file_handler.py`  
  Handles loading and saving of JSON files, with corruption handling (initializes default data if the file is corrupted).

- `data/homeObjects.json`  
  Sample JSON file storing the nested home objects data.

- `main.py`  
  The main script that runs a command-line interface (CLI) allowing the user to interactively manage home objects.

---

## How to Run

1. **Clone the repository:**

   git clone https://github.com/yourusername/cataloger-of-household-objects.git  
   cd cataloger-of-household-objects

2. **Ensure Python 3.7+ is installed** on your system.

3. **Run the main script:**

   python main.py

4. **Follow the on-screen prompts:**

   - View current objects in the home.
   - Choose an action:  
     `[1] Add an object`  
     `[2] Modify an object or category`  
     `[3] Delete an object`

5. **Input required details** like location path, object name, and category as requested.

6. **The changes are saved automatically** in `data/homeObjects.json`.

---

## Example JSON Structure

{
    "livingRoom": {
        "objects": {
            "TV": {
                "category": "electronic"
            },
            "sofa": {
                "category": "furniture"
            }
        }
    },
    "bedroom": {
        "objects": {
            "bed": {
                "category": "furniture"
            },
            "book": {
                "category": "personal"
            }
        },
        "closet": {
            "objects": {
                "jacket": {
                    "category": "clothing"
                },
                "shoes": {
                    "category": "footwear"
                }
            }
        }
    }
}

---

## Requirements

- Python 3.7 or higher

---

## Error Handling

- Raises `TypeError` if wrong parameter types are passed to core functions.
- If the JSON file is missing or corrupted, it will be initialized with a default empty structure.
- Prompts the user to enter valid input types in the CLI.