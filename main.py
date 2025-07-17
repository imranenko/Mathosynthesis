from files_handler import create_files
import setup

if __name__ == "__main__":
    
    # Generate tasks
    
    # Setups:
    # - .multplication()
    # - .basic_operation()
    
    tasks = setup.multiplication()

    # Create .md and .pdf files
    create_files(tasks, open_pdf_after_create=True)