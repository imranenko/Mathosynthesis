import argparse
from .files_handler import get_setups
from config import SETUPS_DIR

def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate math takss from a setup file and opetionally open the results"
    )
    
    parser.add_argument(
        "--setup", "-s",
        type=str,
        help="Name of the JSON setup file (e.g., basic_operations.json)"
    )
    
    parser.add_argument(
        "--open", "-o",
        action="store_true",
        help="Open PDF file after creation"
    )
    
    parser.add_argument(
        "--reveal", "-r",
        action="store_true",
        help="Reveal PDF file in Finder"
    )
    
    parser.add_argument(
        "--md", "-m",
        action="store_true",
        help="Keep md file after PDF creation"
    )
    
    return parser.parse_args()


def ask_setup():
    setups = get_setups()
    if not setups:
        print("No setups files found.")
        return None
    
    category_names = list(setups.keys())
    files = []
    for category_name in category_names:
        files.extend(setups[category_name])
    printables = []
    counter = 0
    
    printables.append("\n=== SETUPS ===\n")
    
    for category_name in category_names:
        category_files = setups[category_name]
        
        if category_name != 'NO_CATEGORY':
            printables.append(f"== {category_name} ==")

        for i, file in enumerate(category_files, start=counter):
            printables.append(f"    {i+1}. {file}")
        counter += len(category_files)
        printables.append("")

    chosen_file = None
    while not chosen_file:  
        for printable in printables:
            print(printable)   
        try:
            answer = input("Choose the number of setup: ")
            chosen_number = int(answer) - 1
            if 0 <= chosen_number < len(files):
                chosen_file = files[chosen_number]
            else:
                print("INVALID INPUT NUMBER!") # red
        except ValueError:
            print("PLEASE ENTER A VALID NUMBER\n") # red

    chosen_category = ""
    for category_name in category_names:
        if chosen_file in setups[category_name] and category_name != "NO_CATEGORY":
            chosen_category = category_name
            break

    chosen_path = f"{SETUPS_DIR}/{chosen_category}/{chosen_file}"
    return chosen_path