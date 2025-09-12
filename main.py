from handlers import parse_args, read_json, create_blocks, create_files
from config import SETUPS_DIR

def main():
    # Use CLI argument for setup file
    args = parse_args()
    json_file = args.setup
    auto_open = args.open
    show_file = args.file

    json_path = f"{SETUPS_DIR}/{json_file}"

    # Load JSON and generate tasks
    json_data = read_json(json_path)
    
    # Generate tasks
    tasks = create_blocks(json_data)

    # Create files (PDF, MD) and get the PDF path
    create_files(tasks, auto_open=auto_open, auto_reveal=show_file)
    

if __name__ == "__main__":
    main()
    
    # Usage example
    # python main.py -s basic_operations.json -o -f
    # Run main.py using basic_operations.json setup; Open pdf-file; Find pdf-file