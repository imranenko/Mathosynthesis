from generators import register
import json

def read_json(json_path):
    with open(json_path, "r") as json_file:
        json_data = json.load(json_file)
        return json_data
    
def create_blocks(json_data):
    task_blocks = json_data["task_blocks"]
    lines = []
    
    # Import multicol
    lines.append("---")
    lines.append("header-includes:")
    lines.append(" - \\usepackage{multicol}")
    lines.append("---")
    
    # For-loop with task blocks
    for task_block in task_blocks:
        task_type = task_block["instruction"]
        task_settings = task_block["settings"]
        if not task_type:
            raise ValueError("Missing or invalid 'type' in setup.")
        
        task_block = register[task_type](task_settings)
        
        lines += task_block
        lines.append("\\")
    
    return lines