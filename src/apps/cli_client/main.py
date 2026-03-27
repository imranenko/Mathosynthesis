import logging
from pathlib import Path
import colorama

from mathosynthesis.engine import setup_environment, generate_files
from mathosynthesis.config.config import PREFERRED_LANGUAGES
from mathosynthesis.handlers.files_handler import (
    get_setup_path_by_name,
    get_setup_path_by_number,
    open_file,
    reveal_file,
    delete_file
)
from .cli_handler import parse_args, build_printable_setups, ask_setup

# CLI-only defaults
AUTO_OPEN_FILE = False
AUTO_REVEAL_FILE = False
KEEP_MD_FILE = False

colorama.init()
logger = logging.getLogger(__name__)

def select_setup(selected_setup) -> Path:
    if isinstance(selected_setup, str):
        return get_setup_path_by_name(selected_setup)
    elif isinstance(selected_setup, int):
        return get_setup_path_by_number(selected_setup)
    else:
        for line in build_printable_setups():
            print(line)
        json_path = ask_setup()
        return json_path

def handle_files(args, md_path, pdf_path):
    if args.open or AUTO_OPEN_FILE:
        open_file(pdf_path)
    if args.reveal or AUTO_REVEAL_FILE:
        reveal_file(pdf_path)
    if not (args.markdown or KEEP_MD_FILE):
        delete_file(md_path)

def main() -> None:
    setup_environment()
    args = parse_args()
    json_path = select_setup(args.setup)
    
    # Core Engine call
    md_path, pdf_path = generate_files(json_path, args.language or PREFERRED_LANGUAGES)
    
    handle_files(args, md_path, pdf_path)

if __name__ == "__main__":
    main()