from handlers import parse_args, read_json, generate_setup, create_files, ask_setup_file
from config import SETUPS_DIR

def main():
    # Use CLI argument for setup file
    args = parse_args()
    setup_file = args.setup
    auto_open = args.open
    show_file = args.file

    
    if not setup_file:
        setup_file = ask_setup_file()
        
    json_path = f"{SETUPS_DIR}/{setup_file}"

    # Load JSON and generate tasks
    json_data = read_json(json_path)
    
    # Generate tasks
    tasks = generate_setup(json_data)

    # Create files (PDF, MD) and get the PDF path
    create_files(tasks, auto_open=auto_open, auto_reveal=show_file)
    

if __name__ == "__main__":
    main()
    
    # Usage examples:
    # python main.py
    # python main.py -s basic_operations.json -o -f
    # Run main.py using basic_operations.json setup; Open pdf-file; Find pdf-file