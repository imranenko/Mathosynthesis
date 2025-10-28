from generators import register
import json
from typing import Any

def read_json(json_path: str) -> dict[str, Any]:
    """Read a JSON file from the given path and return its contents as a dictionary."""
    try:
        with open(json_path, "r", encoding="utf-8") as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        raise FileNotFoundError(f"JSON file not found: {json_path}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON format in file '{json_path}': {e}")


def generate_setup(json_data: dict[str, Any]) -> list[str]:
    """Generates a setup using the JSON data and returns created lines."""
    task_blocks = json_data["task_blocks"]
    lines = []
    
    # MULTICOL SUPPORT
    lines.extend([
        "---",
        "header-includes:",
        " - \\usepackage{multicol}",
        "---"
    ])
    
    # Create blocks
    for task_block in task_blocks:
        task_type = task_block.get("type")
        task_settings = task_block.get("settings")
        task_columns = task_block.get("columns")
        
        if task_type is None or task_settings is None or task_columns is None:
            raise ValueError("Missing required keys in task block!")
        
        # Create tasks for block and corresponding blocks
        tasks = register[task_type](task_settings)
        block = _generate_block(tasks, task_columns)
        
        lines.extend(block)
        lines.append("\\")
    
    return lines

def _generate_block(tasks, columns=2):
    if columns > 1:
        lines = []
        lines.append(f"\\begin{{multicols}}{{{columns}}}")
        lines.append("\\begin{enumerate}")
        
        for task in tasks:
            lines.append(f"\\item ${task}$")
        
        lines.append("\\end{enumerate}")
        lines.append("\\end{multicols}")
        
        return lines
    
    else: # NOTE: for columns <= 0, 1 set as deafult
        lines = []
        lines.append("\\begin{enumerate}")
        
        for task in tasks:
            lines.append(f"\\item ${task}$")
        
        lines.append("\\end{enumerate}")
        
        return lines