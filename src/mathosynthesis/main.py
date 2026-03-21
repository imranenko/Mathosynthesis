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


def setup_environment():
    create_folder(TASKS_DIR)
    create_folder(LOGS_DIR)
    setup_logging()


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


def generate_files(json_path, preferred_languages):
    setup_stem = json_path.stem
    base_path = get_base_path(setup_stem)
    md_path = base_path.with_suffix(".md")
    pdf_path = base_path.with_suffix(".pdf")

    json_data = read_json(json_path)
    tasks = generate_setup(json_data, preferred_languages=preferred_languages)
    create_md(tasks, md_path)
    create_pdf(md_path, pdf_path)

    return md_path, pdf_path


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
    json_path = select_setup(args)
    md_path, pdf_path = generate_files(json_path, args.language or PREFERRED_LANGUAGES)
    
    handle_files(args, md_path, pdf_path)

if __name__ == "__main__":
    main()