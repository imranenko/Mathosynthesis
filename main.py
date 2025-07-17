from files_handler import *
import setup

if __name__ == "__main__":
    
    # Generate tasks
    
    # Setups:
    # .multplication()
    # .basic_operation()
    
    tasks = setup.basic_operations()

    # Create .md and .pdf files
    create_files(tasks)