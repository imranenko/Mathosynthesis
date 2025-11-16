from handlers import parse_args, read_json, generate_setup, create_files, ask_setup
from config import AUTO_OPEN_FILE, AUTO_REVEAL_FILE, KEEP_MD_FILE, PREFERRED_LANGUAGES

def main():
    # Use CLI argument for setup file
    args = parse_args()
    setup_path = args.setup
    auto_open = args.open
    auto_reveal = args.reveal
    keep_md = args.markdown
    preferred_languagess = args.language

    # Ask for a setup if not given
    if not setup_path:
        setup_path, setup_name = ask_setup()
        
    # Use config settings for auto_open, auto_reveal, keep_md
    if auto_open is None:
        auto_open = AUTO_OPEN_FILE
    if auto_reveal is None:
        auto_reveal = AUTO_REVEAL_FILE
    if keep_md is None:
        keep_md = KEEP_MD_FILE
    if preferred_languagess is None:
        preferred_languagess = PREFERRED_LANGUAGES
    # Create files (PDF, MD) and get the PDF path
    if setup_name[-5:] == '.json':
       file_name = setup_name[:-5]
    
    # Load JSON
    json_data = read_json(setup_path)
    
    # Generate setup
    tasks = generate_setup(
        json_data,
        preferred_languagess=preferred_languagess
        )

    # Create file
    create_files(
        tasks,
        file_name=file_name,
        keep_md=keep_md,
        auto_open=auto_open,
        auto_reveal=auto_reveal,
        )
    
    # NOTE: Could move open/reveal/etc file here?
    # File path needed; Should create in main.py
    

if __name__ == "__main__":
    main()
    
    # Usage examples:
    # python main.py
    # python main.py -s basic_operations.json -o -f
    # Run main.py using basic_operations.json setup; Open pdf-file; Find pdf-file