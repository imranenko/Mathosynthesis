from tasks_handler import create_tasks, read_json
from files_handler import create_files


if __name__ == "__main__":
    
    # Choose json file
    json_path = "setups/basic_operations.json"
    
    # Open json file
    json_data = read_json(json_path)
    tasks = create_tasks(json_data)
    
    # Create .md and .pdf files
    create_files(tasks, auto_open=False)