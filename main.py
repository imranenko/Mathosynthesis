from handlers import parse_args, read_json, generate_setup, create_files, ask_setup
from config import SETUPS_DIR
# from config import AUTO_OPEN_FILE, AUTO_SHOW_FILE, KEEP_MD_FILE

def main():
    # Use CLI argument for setup file
    args = parse_args()
    setup_file = args.setup
    auto_open = args.open
    auto_reveal = args.reveal
    keep_md = args.md

    # Ask for a setup if not given
    if not setup_file:
        setup_path = ask_setup()
    
    # Load JSON
    json_data = read_json(setup_path)
    
    # Generate setup
    tasks = generate_setup(json_data)

    # Create files (PDF, MD) and get the PDF path
    create_files(tasks, keep_md=keep_md, auto_open=auto_open, auto_reveal=auto_reveal)
    

if __name__ == "__main__":
    main()
    
    # Usage examples:
    # python main.py
    # python main.py -s basic_operations.json -o -f
    # Run main.py using basic_operations.json setup; Open pdf-file; Find pdf-file