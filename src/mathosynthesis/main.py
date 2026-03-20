import logging
from pathlib import Path

import colorama

from .handlers import (
    parse_args,
    read_json,
    generate_setup,
    ask_setup,
    open_file,
    reveal_file,
    delete_file,
    get_base_path,
    create_md,
    create_pdf,
    create_folder,
    get_setups,
    build_printable_setups,
    get_setup_path_by_name,
    get_setup_path_by_number
)
from .config.config import (
    AUTO_OPEN_FILE,
    AUTO_REVEAL_FILE,
    KEEP_MD_FILE,
    PREFERRED_LANGUAGES,
    TASKS_DIR,
    LOGS_DIR,
    SETUPS_DIR,
)
from .config.logging_config import setup_logging

colorama.init()
logger = logging.getLogger(__name__)

def main() -> None:
    # Create tasks and log folders if don't exist
    create_folder(TASKS_DIR)
    create_folder(LOGS_DIR)
    
    # Setup logging
    setup_logging()
    
    # Use CLI argument or defaults
    args = parse_args()
    selected_setup = args.setup if args.setup is not None else None
    auto_open = args.open if args.open is not None else AUTO_OPEN_FILE
    auto_reveal = args.reveal if args.reveal is not None else AUTO_REVEAL_FILE
    keep_md = args.markdown if args.markdown is not None else KEEP_MD_FILE
    preferred_languages = args.language if args.language is not None else PREFERRED_LANGUAGES

    if isinstance(selected_setup, str):
        json_path = get_setup_path_by_name(selected_setup)
    elif isinstance(selected_setup, int):
        json_path = get_setup_path_by_number(selected_setup)
    else:
        printable_setups = build_printable_setups()
        for line in printable_setups:
            print(line)
        
        selected_setup = ask_setup()
        
        json_path = Path(SETUPS_DIR) / selected_setup

    # Get file paths
    setup_stem = json_path.stem
    base_path = get_base_path(setup_stem)
    md_path = base_path.with_suffix(".md")
    pdf_path = base_path.with_suffix(".pdf")
    
    # Load JSON
    try:
        json_data = read_json(json_path)
    except (FileNotFoundError, ValueError) as e:
        logger.error(f"Coudn't load JSON file: {e}")
        return
    
    # Generate setup and tasks file
    tasks = generate_setup(json_data, preferred_languages=preferred_languages)
    create_md(tasks, md_path)
    create_pdf(md_path, pdf_path)
    
    # Handle files
    if auto_open:
        open_file(pdf_path)
    if auto_reveal:
        reveal_file(pdf_path)
    if not keep_md:
        delete_file(md_path)

if __name__ == "__main__":
    main()