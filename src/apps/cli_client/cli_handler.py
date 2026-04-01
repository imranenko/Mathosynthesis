import argparse
import logging
import colorama
from pathlib import Path

from mathosynthesis.handlers.files_handler import get_setups
from mathosynthesis.config.config import SETUPS_DIR

logger = logging.getLogger(__name__)

def _str_to_bool(value: str) -> bool:
    """Convert string truth to boolean."""
    val = str(value).lower()
    if val in ("true", "1", "yes", "y"):
        return True
    elif val in ("false", "0", "no", "n"):
        return False
    else:
        raise argparse.ArgumentTypeError("Boolean value expected (True/False).")

def _str_or_int(value: str):
    """Parse string or integer."""
    try:
        return int(value)
    except ValueError:
        return str(value)

def parse_args() -> argparse.Namespace:
    """Parse CLI arguments for math task generation."""
    parser = argparse.ArgumentParser(
        description="Generate math tasks (PDF) via LaTeX from a JSON setup file."
    )
    
    parser.add_argument(
        "--setup", "-s",
        type=_str_or_int,
        help="Name or number of the JSON setup file (e.g., basic_operations.json)"
    )
    
    parser.add_argument(
        "--open", "-o",
        nargs="?",
        const=True,
        type=_str_to_bool,
        help="Open PDF file after creation"
    )
    
    parser.add_argument(
        "--file", "-f",
        nargs="?",
        const=True,
        type=_str_to_bool,
        help="Reveal PDF file in system file manager"
    )
    
    parser.add_argument(
        "--latex", "-tex",
        nargs="?",
        const=True,
        type=_str_to_bool,
        help="Keep intermediate .tex source file after PDF creation"
    )
    
    parser.add_argument(
        "--language", "-lang",
        nargs='+',
        type=str,
        help="Specify the language for the generated tasks (e.g., en de)."
    )
    
    return parser.parse_args()

def build_printable_setups() -> list[str]:
    """Build formatted list of available setups for the console."""
    RESET = colorama.Style.RESET_ALL
    BLUE = colorama.Fore.BLUE
    
    setups_dict = get_setups()
    if not setups_dict:
        raise ValueError("No setups available.")

    lines = []
    lines.append(f"\n{BLUE}=== SETUPS ==={RESET}\n")
    index: int = 1
    for category in list(setups_dict.keys()):
        if category != "NO_CATEGORY":
            lines.append(f"{BLUE}== {category} =={RESET}")

        for item in setups_dict[category]:
            display_name = item["name"].get("en", item["filename"])
            lines.append(f"    {BLUE}{index}.{RESET} {display_name}")
            index += 1

        lines.append("")
    return lines
    
def ask_setup() -> Path:
    """Prompt user to select a setup and return its path."""
    setups_dict = get_setups()
    if not setups_dict:
        raise ValueError("No setups available.")
    
    available_paths = []
    for category in list(setups_dict.keys()):
        for item in setups_dict[category]:
            available_paths.append(item["path"])
    
    chosen_path = None
    while chosen_path is None:
        try:
            choice = input(f"Choose the number of the setup (1-{len(available_paths)}): ")
            selected_index = int(choice) - 1
            if 0 <= selected_index < len(available_paths):
                chosen_path = available_paths[selected_index]
            else:
                logger.warning(f"Invalid choice! Please pick a number from 1 to {len(available_paths)}.")
        except ValueError:
            logger.warning("Please enter a valid number.")
    
    return chosen_path
