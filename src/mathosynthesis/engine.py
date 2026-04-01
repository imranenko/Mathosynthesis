from pathlib import Path
import logging
from mathosynthesis.handlers.files_handler import (
    get_base_path,
    create_tex,
    create_pdf,
    create_folder
)
from mathosynthesis.handlers.generators_handler import read_json, generate_latex
from mathosynthesis.config.config import TASKS_DIR, LOGS_DIR
from mathosynthesis.config.logging_config import setup_logging

logger = logging.getLogger(__name__)

def setup_environment():
    create_folder(TASKS_DIR)
    create_folder(LOGS_DIR)
    setup_logging()

def generate_files(json_path: Path, preferred_languages: str):
    """
    Core function to generate LaTeX source and PDF files from a JSON setup.
    """
    setup_stem = json_path.stem
    base_path = get_base_path(setup_stem)
    tex_path = base_path.with_suffix(".tex")
    pdf_path = base_path.with_suffix(".pdf")

    json_data = read_json(json_path)
    
    # Core logic: generate LaTeX instead of Markdown strings
    latex_content = generate_latex(json_data, preferred_languages=preferred_languages)
    
    create_tex(latex_content, tex_path)
    create_pdf(tex_path, pdf_path)

    return tex_path, pdf_path
