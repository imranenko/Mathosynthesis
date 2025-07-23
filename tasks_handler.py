from generators.addition import *
from generators.subtraction import *
from generators.multiplication import *
from generators.division import *

import json

instruction = {
    "addition": Addition.generate_task,
    "addition_missing": Addition.generate_with_missing_element,
    "subtraction": Subtraction.generate_task,
    "subtraction_missing": Subtraction.generate_with_missing_element,
    "multiplication": Multiplication.generate_task,
    "multiplication_missing": Multiplication.generate_with_missing_element,
    "division": Division.generate_task,
    "division": Division.generate_with_missing_element
}

def read_json(json_path):
    with open(json_path, "r") as json_file:
        json_data = json.load(json_file)
        return json_data
    
def create_tasks(json_data):
    task_blocks = json_data["task_blocks"]
    tasks = []
    
    # For-loop with task blocks
    for task_block in task_blocks:
        task_type = task_block["instruction"]
        task_settings = task_block["settings"]
        if not task_type:
            raise ValueError("Missing or invalid 'type' in task block.")
        
        task_block = instruction[task_type](task_settings)
        
        tasks += task_block
        tasks += "\n"
    
    return tasks