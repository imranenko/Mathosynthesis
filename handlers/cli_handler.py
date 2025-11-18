import argparse
from .files_handler import get_setups
from config import SETUPS_DIR
import colorama
colorama.init()

def _str_to_bool(value):
    val = str(value).lower()
    if val in ("true", "1", "yes", "y"):
        return True
    elif val in ("false", "0", "no", "n"):
        return False
    else:
        raise argparse.ArgumentTypeError("Boolean value expected (True/False).")

def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate math tasks from a setup file and optionally open the results"
    )
    
    parser.add_argument(
        "--setup", "-s",
        type=str,
        help="Name of the JSON setup file (e.g., basic_operations.json)"
    )
    
    parser.add_argument(
        "--open", "-o",
        nargs="?", # optionally to specify boolean
        const=True, # if not specified, store True
        type=_str_to_bool, # if specified, converts input to boolean
        help="Open PDF file after creation"
    )
    
    parser.add_argument(
        "--reveal", "-r",
        nargs="?",
        const=True,
        type=_str_to_bool,
        help="Reveal PDF file in Finder"
    )
    
    parser.add_argument(
        "--markdown", "-md",
        nargs="?",
        const=True,
        type=_str_to_bool,
        help="Keep md file after PDF creation"
    )
    
    parser.add_argument(
        "--language", "-lang",
        nargs='+', # one or more arguments
        type=str,
        help="Specify the language for the generated tasks."
    )
    
    return parser.parse_args()


def build_printable_setups(setups_dict):
    RESET = colorama.Style.RESET_ALL
    BLUE = colorama.Fore.BLUE

    category_names = list(setups_dict.keys())
    lines = []
    lines.append(f"\n{BLUE}=== SETUPS ==={RESET}\n")
    index = 1
    for category in category_names:
        files_in_category = setups_dict[category]
        if category != "NO_CATEGORY":
            lines.append(f"{BLUE}== {category} =={RESET}")

        for filename in files_in_category:
            lines.append(f"    {BLUE}{index}.{RESET} {filename}")
            index += 1

        lines.append("")
    return lines

def ask_setup(setups_dict: dict):
    RESET = colorama.Style.RESET_ALL
    RED = colorama.Fore.RED
    
    available_categories = list(setups_dict.keys())
    available_setups = []
    for category in available_categories:
        available_setups.extend(setups_dict[category])
    
    chosen_file = None
    while chosen_file is None:
        try:
            choice = input("Choose the number of the setup: ")
            selected_index = int(choice) - 1
            if 0 <= selected_index < len(available_setups):
                chosen_file = available_setups[selected_index]
            else:
                print(f"{RED}INVALID INPUT NUMBER!{RESET}\n")
        except ValueError:
            print(f"{RED}INVALID INPUT NUMBER!{RESET}\n")
    
    # Find the category that contains the chosen file (excluding "NO_CATEGORY")
    chosen_category = ""
    for cat in available_categories:
        if cat == "NO_CATEGORY":
            continue
        if chosen_file in setups_dict[cat]:
            chosen_category = cat
            break
    
    chosen_path = f"{SETUPS_DIR}/{chosen_category}/{chosen_file}"
    return chosen_path
