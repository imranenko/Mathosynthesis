from pathlib import Path
import logging
from mathosynthesis.handlers.files_handler import (
    get_base_path,
    create_md,
    create_pdf,
    create_folder
)
from mathosynthesis.handlers.generators_handler import read_json, generate_setup
from mathosynthesis.config.config import TASKS_DIR, LOGS_DIR
from mathosynthesis.config.logging_config import setup_logging

logger = logging.getLogger(__name__)

def setup_environment():
    create_folder(TASKS_DIR)
    create_folder(LOGS_DIR)
    setup_logging()

def generate_files(json_path: Path, preferred_languages: str):
    """
    Core function to generate Markdown and PDF files from a JSON setup.
    """
    setup_stem = json_path.stem
    base_path = get_base_path(setup_stem)
    md_path = base_path.with_suffix(".md")
    pdf_path = base_path.with_suffix(".pdf")

    json_data = read_json(json_path)
    tasks = generate_setup(json_data, preferred_languages=preferred_languages)
    create_md(tasks, md_path)
    create_pdf(md_path, pdf_path)

    return md_path, pdf_path
