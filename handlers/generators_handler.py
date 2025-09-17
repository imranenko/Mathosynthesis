from generators import register
import json

def read_json(json_path):
    with open(json_path, "r") as json_file:
        json_data = json.load(json_file)
        return json_data
    
def generate_setup(json_data):
    task_blocks = json_data["task_blocks"]
    lines = []
    
    # Import multicol
    lines.append("---")
    lines.append("header-includes:")
    lines.append(" - \\usepackage{multicol}")
    lines.append("---")
    
    # Create blocks
    for task_block in task_blocks:
        task_type = task_block["type"]
        task_settings = task_block["settings"]
        task_columns = task_block["columns"]
        if not task_type:
            raise ValueError("Missing or invalid 'type' in setup.")
        
        # Create tasks for block
        tasks = register[task_type](task_settings)
        
        # Create block with columns
        block = generate_block(tasks, task_columns)
        
        # Add block
        lines += block
        lines.append("\\")
    
    return lines

def generate_block(tasks, columns=2):
        lines = []
        lines.append(f"\\begin{{multicols}}{{{columns}}}")
        lines.append("\\begin{enumerate}")
        
        for task in tasks:
            lines.append(f"\\item ${task}$")
        
        lines.append("\\end{enumerate}")
        lines.append("\\end{multicols}")
        
        return lines