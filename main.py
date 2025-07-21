from files_handler import create_files
import setup

if __name__ == "__main__":
    
    # Generate tasks
    
    tasks = setup.multiplication_intermidiate()

    # Create .md and .pdf files
    create_files(tasks, auto_open=True)