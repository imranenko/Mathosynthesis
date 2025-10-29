import argparse
from .files_handler import get_setups
from config import SETUPS_DIR

def _str_to_bool(value):
    val = str(value).lower()
    if val in ("true", "1", "yes", "y"):
        return True
    elif val in ("false", "0", "no", "n"):
        return False
    else:
        raise argparse.ArgumentTypeError("Boolean value expected (True/False).")

def parse_args() -> argparse.Namespace:
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
        "--md", "-m",
        nargs="?",
        const=True,
        type=_str_to_bool,
        help="Keep md file after PDF creation"
    )
    
    return parser.parse_args()


def ask_setup() -> tuple[str, str] | None: # TODO isn't optimized well
    """Prompt the user to choose a setup file and return its path and file name."""
    

    try:
        import colorama
        colorama.init()
        RESET = colorama.Style.RESET_ALL
        RED = colorama.Fore.RED
        GREEN = colorama.Fore.GREEN
        YELLOW = colorama.Fore.YELLOW
        BLUE = colorama.Fore.BLUE
    except ImportError:
        RESET = RED = GREEN = YELLOW = BLUE = ""
    
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
    
    printables.append(f"\n{BLUE}=== SETUPS ==={RESET}\n")
    
    for category_name in category_names:
        category_files = setups[category_name]
        
        if category_name != 'NO_CATEGORY':
            printables.append(f"{BLUE}== {category_name} =={RESET}")

        for i, file in enumerate(category_files, start=counter):
            printables.append(f"    {BLUE}{i+1}.{RESET} {file}")
        counter += len(category_files)
        printables.append("")
        
        for printable in printables:
            print(printable)   

    # Prompt user
    chosen_file = None
    while not chosen_file:  
        try:
            answer = input("Choose the number of setup: ")
            chosen_number = int(answer) - 1
            if 0 <= chosen_number < len(files):
                chosen_file = files[chosen_number]
            else:
                print(f"{RED}INVALID INPUT NUMBER!{RESET}\n") # red
        except ValueError:
            print(f"{RED}INVALID INPUT NUMBER!{RESET}\n") # red

    chosen_category = ""
    for category_name in category_names:
        if chosen_file in setups[category_name] and category_name != "NO_CATEGORY":
            chosen_category = category_name
            break

    chosen_path = f"{SETUPS_DIR}/{chosen_category}/{chosen_file}"
    
    return chosen_path, chosen_file