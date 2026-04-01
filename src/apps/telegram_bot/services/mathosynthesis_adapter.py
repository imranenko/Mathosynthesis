from mathosynthesis.handlers import files_handler
from mathosynthesis.engine import generate_files
from mathosynthesis.config.config import PREFERRED_LANGUAGES

from pathlib import Path

def get_setups():
    """Retrieve setup directory content."""
    return files_handler.get_setups()

def get_setup(setup_name: str):
    """Path to setup file by name."""
    return files_handler.get_setup_path_by_name(setup_name)

def generate_pdf(json_path: str, language: str = None):
    """
    Generate LaTeX source and PDF, returning PDF path. 
    Intermediate LaTeX is deleted as the bot doesn't need it.
    """
    try:
        json_path = Path(json_path)
        
        # Use provided language or fall back to default
        if not language:
            language = PREFERRED_LANGUAGES[0] if PREFERRED_LANGUAGES else "en"
        
        # generate_files returns (tex_path, pdf_path)
        # It expects preferred_languages as a list or string
        tex_path, pdf_path = generate_files(json_path, preferred_languages=language)

        # Cleanup intermediate LaTeX source
        files_handler.delete_file(tex_path)

        return pdf_path
    except (FileNotFoundError, ValueError) as e:
        print(f"Error generating PDF for {json_path}: {e}")
        return None

def get_flat_setups(setups_dict: dict) -> list[tuple[str, str]]:
    """Flatten the setups dictionary into a list of (category, filename) tuples."""
    flat_setups = []
    category_names = (["NO_CATEGORY"] if "NO_CATEGORY" in setups_dict else []) + sorted(k for k in setups_dict if k != "NO_CATEGORY")
    for category in category_names:
        for item in setups_dict[category]:
            flat_setups.append((category, item["filename"]))
    return flat_setups

def format_setups_text(setups_dict: dict, ui_lang: str = 'en') -> str:
    """Format the setups dictionary into a user-friendly string."""
    from .translation_service import get_text
    
    header = get_text('setups_header', ui_lang)
    lines = [f"<b>{header}</b>", ""]
    index: int = 1
    category_names = (["NO_CATEGORY"] if "NO_CATEGORY" in setups_dict else []) + sorted(k for k in setups_dict if k != "NO_CATEGORY")
    for category in category_names:
        if category != "NO_CATEGORY":
            # Add a blank line before subsequent categories
            if len(lines) > 2:
                lines.append("")
            lines.append(f"<b>{category}</b>")
        for item in setups_dict[category]:
            display_name = item["name"].get(ui_lang, item["filename"])
            lines.append(f"    <b>{index}.</b> {display_name}")
            index += 1
    return "\n".join(lines)