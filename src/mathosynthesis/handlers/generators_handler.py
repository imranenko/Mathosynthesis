import json
from typing import Any
from pathlib import Path

from mathosynthesis.generators import register
from mathosynthesis.config.config import PREFERRED_LANGUAGES

def read_json(json_path: str | Path) -> dict[str, Any]:
    """Read a JSON file and return its contents as a dictionary.

    Args:
        json_path: Path to the JSON file.

    Returns:
        Dictionary representing the JSON contents.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the JSON is invalid.
    """
    try:
        with open(json_path, "r", encoding="utf-8") as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        raise FileNotFoundError(f"JSON file not found: {json_path}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON format in file '{json_path}': {e}")

def generate_setup(
    json_data: dict[str, Any],
    preferred_languages: list[str] = PREFERRED_LANGUAGES,
    ) -> list[str]:
    """Generate task blocks from JSON configuration and return formatted lines.

    Args:
        json_data: Parsed JSON data with task block configurations.
        preferred_languages: List of language codes to select descriptions.

    Returns:
        A list of formatted strings representing the generated setup.
        
    Raises:
        ValueError: If required keys are missing in task blocks.
    """ 
    task_blocks = json_data["task_blocks"]
    lines = []
    
    # Import Packages
    lines.extend([
        "---",
        "header-includes:",
        " - \\usepackage{multicol}",
        " - \\usepackage{siunitx}",
        " - \\renewcommand{\\labelenumi}{\\arabic{enumi})}",
        "---"
    ])
    
    # Create blocks
    for task_block in task_blocks:
        task_id = task_block.get("id")
        task_settings = task_block.get("settings")
        task_columns = task_block.get("columns")
        task_descriptions = task_block.get("description")
        
        if task_id is None or task_settings is None or task_columns is None:
            raise ValueError("Missing required keys in task block!")
        
        # Create tasks for block and corresponding blocks
        tasks = register[task_id](task_settings)
        block = _generate_block(tasks, task_columns)
        
        # Choose language and add description
        if task_descriptions is not None:
            supported_languages = task_descriptions.keys()
            for lang in preferred_languages:
                if lang in supported_languages:
                    description = task_descriptions.get(lang)
                    lines.append(description)
                    break
        
        lines.extend(block)
        lines.append("\\")
    
    return lines

def _generate_block(tasks: list[str], columns: int = 2) -> list[str]:
    """Generate LaTeX formatted block of tasks.

    Args:
        tasks: List of task strings.
        columns: Number of columns to format the tasks into.

    Returns:
        A list of strings containing LaTeX code for the task block.
    """
    if columns > 1:
        lines = []
        lines.append(f"\\begin{{multicols}}{{{columns}}}")
        lines.append("\\begin{enumerate}")
        
        for task in tasks:
            lines.append(f"\\item ${task}$")
        
        lines.append("\\end{enumerate}")
        lines.append("\\end{multicols}")
        
        return lines
    
    else: # NOTE: for columns <= 0, by default: 1 column
        lines = []
        lines.append("\\begin{enumerate}")
        
        for task in tasks:
            lines.append(f"\\item ${task}$")
        
        lines.append("\\end{enumerate}")
        
        return lines