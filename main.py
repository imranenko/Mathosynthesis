from handlers import parse_args, read_json, generate_setup, ask_setup, open_file, reveal_file, delete_file, get_base_path, create_md, create_pdf, create_folder
from config import AUTO_OPEN_FILE, AUTO_REVEAL_FILE, KEEP_MD_FILE, PREFERRED_LANGUAGES, TASKS_DIR
from pathlib import Path

def main():
    # Use CLI argument for setup file
    args = parse_args()
    setup_path = args.setup
    auto_open = args.open
    auto_reveal = args.reveal
    keep_md = args.markdown
    preferred_languages = args.language

    # Use config settings for auto_open, auto_reveal, keep_md
    if auto_open is None:
        auto_open = AUTO_OPEN_FILE
    if auto_reveal is None:
        auto_reveal = AUTO_REVEAL_FILE
    if keep_md is None:
        keep_md = KEEP_MD_FILE
    if preferred_languages is None:
        preferred_languages = PREFERRED_LANGUAGES

    # Get file paths
    if not setup_path:
        setup_path = Path(ask_setup())

    setup_stem = setup_path.stem
    base_path = Path(get_base_path(setup_stem))
    md_path = base_path.with_suffix(".md")
    pdf_path = base_path.with_suffix(".pdf")
    
    # Load JSON
    json_data = read_json(setup_path)
    
    # Generate setup
    tasks = generate_setup(
        json_data,
        preferred_languages=preferred_languages
        )

    # Create tasks folder if not exists
    create_folder(TASKS_DIR)
    
    # Create files
    create_md(tasks, md_path)
    create_pdf(md_path, pdf_path)
    
    # Handle files
    if auto_open:
        open_file(pdf_path)
    if auto_reveal:
        reveal_file(pdf_path)
    if not keep_md:
        delete_file(md_path)
    

if __name__ == "__main__":
    main()
    
    # Usage examples:
    # python main.py
    # python main.py -s basic_operations.json -o -f
    # Run main.py using basic_operations.json setup; Open pdf-file; Find pdf-file