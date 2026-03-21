import argparse
import logging

import colorama
from pathlib import Path

from .files_handler import get_setups
from ..config import SETUPS_DIR

logger = logging.getLogger(__name__)

def _str_to_bool(value: str) -> bool:
    """
    Convert a string representation of truth to a boolean.

    Args:
        value: String to convert, e.g., "true", "False", "1", "no".

    Returns:
        Boolean True or False corresponding to the input string.

    Raises:
        argparse.ArgumentTypeError: If the input string is not a valid boolean representation.
    """
    val = str(value).lower()
    if val in ("true", "1", "yes", "y"):
        return True
    elif val in ("false", "0", "no", "n"):
        return False
    else:
        raise argparse.ArgumentTypeError("Boolean value expected (True/False).")

def _str_or_int(value: str):
    """
    Parse a value that can be either a string or an integer.

    If the value represents an integer, return it as int,
    otherwise return it as string.
    """
    try:
        return int(value)
    except ValueError:
        return str(value)

def parse_args() -> argparse.Namespace:
    """
    Parse command-line arguments for the math task generator CLI.

    Returns:
        An argparse.Namespace object containing parsed command-line options:
        - setup: JSON setup filename (str).
        - open: Whether to open the PDF after creation (bool).
        - reveal: Whether to reveal the PDF file in Finder (bool).
        - markdown: Whether to keep the markdown file after PDF creation (bool).
        - language: List of languages for generated tasks (list of str).
    """
    parser = argparse.ArgumentParser(
        description="Generate math tasks from a setup file and optionally open the results"
    )
    
    parser.add_argument(
        "--setup", "-s",
        type=_str_or_int,
        help="Name or number of the JSON setup file (e.g., basic_operations.json)"
    )
    
    parser.add_argument(
        "--open", "-o",
        nargs="?", # optional to specify boolean
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

def build_printable_setups() -> list[str]:
    """
    Build a formatted list of strings representing available setup files grouped by category.

    Args:
        setups_dict: Dictionary mapping category names to lists of setup filenames.

    Returns:
        List of formatted strings ready to be printed to the console.
    """
    RESET = colorama.Style.RESET_ALL
    BLUE = colorama.Fore.BLUE
    
    setups_dict = get_setups()
    if not setups_dict:
        raise ValueError("No setups available.")

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
    
def ask_setup() -> Path:
    """
    Prompt the user to select a setup file from available categories and return its full path.

    Args:
        setups_dict: Dictionary mapping category names to lists of setup filenames.

    Returns:
        Full path (string) to the chosen setup file, including category folder.

    The function handles invalid input by prompting repeatedly.
    """
    setups_dict = get_setups()
    if not setups_dict:
        raise ValueError("No setups available.")
    
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
                logger.warning(f"INVALID INPUT NUMBER!\n")
        except ValueError:
            logger.warning(f"INVALID INPUT NUMBER!\n")
    
    # Find the category that contains the chosen file (excluding "NO_CATEGORY")
    chosen_category = ""
    for cat in available_categories:
        if cat == "NO_CATEGORY":
            continue
        if chosen_file in setups_dict[cat]:
            chosen_category = cat
            break
    
    chosen_path = Path(f"{SETUPS_DIR}/{chosen_category}/{chosen_file}")
    return chosen_path
