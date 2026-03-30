import json
import logging
from typing import Any
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

from mathosynthesis.generators import register
from mathosynthesis.config.config import (
    PREFERRED_LANGUAGES, 
    PDF_FONT, 
    TASK_SHEET_TEMPLATE
)

logger = logging.getLogger(__name__)

def read_json(json_path: str | Path) -> dict[str, Any]:
    """Read a JSON file and return its contents as a dictionary."""
    try:
        with open(json_path, "r", encoding="utf-8") as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        raise FileNotFoundError(f"JSON file not found: {json_path}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON format in file '{json_path}': {e}")

def generate_latex(
    json_data: dict[str, Any],
    preferred_languages: list[str] | str = PREFERRED_LANGUAGES,
) -> str:
    """
    Renders the LaTeX source for a task sheet using a Jinja2 template.
    """
    if isinstance(preferred_languages, str):
        preferred_languages = [preferred_languages]
    # Prepare data for the template
    template_data = {
        "font_family": PDF_FONT,
        "task_blocks": []
    }
    
    for block_cfg in json_data.get("task_blocks", []):
        task_id = block_cfg.get("id")
        if not task_id or task_id not in register:
            logger.warning(f"Unknown task ID: {task_id}")
            continue
            
        tasks = register[task_id](block_cfg.get("settings", {}))
        
        # Determine the description based on preferred languages
        description = ""
        task_descriptions = block_cfg.get("description", {})
        for lang in preferred_languages:
            if lang in task_descriptions:
                description = task_descriptions[lang]
                break
        
        template_data["task_blocks"].append({
            "description": description,
            "columns": block_cfg.get("columns", 1),
            "tasks": tasks
        })

    # Load and render the Jinja2 template
    env = Environment(loader=FileSystemLoader(TASK_SHEET_TEMPLATE.parent))
    template = env.get_template(TASK_SHEET_TEMPLATE.name)
    return template.render(template_data)