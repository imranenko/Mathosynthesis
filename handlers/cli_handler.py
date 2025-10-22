import argparse
from .files_handler import get_setups_list

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
        "--file", "-f",
        action="store_true",
        help="Reveal PDF file in Finder"
    )
    
    parser.add_argument(
        "--md", "-m",
        action="store_true",
        help="Keep md file after PDF creation"
    )
    
    return parser.parse_args()


def ask_setup_file():
    files = get_setups_list()
    if not files:
        print("No setup files found.")
        return None

    json_file = None
    while json_file is None:
        print("Setups:")
        for i, f in enumerate(files):
            print(f"{i + 1}. {f}")
        try:
            answer = input("Choose the number of setup: ")
            number = int(answer) - 1  # list index starts at 0
            if 0 <= number < len(files):
                json_file = files[number]
            else:
                print("Invalid number!\n")
        except ValueError:
            print("Please enter a valid number!\n")

    return json_file