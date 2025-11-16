import subprocess
import os

import datetime

from config import TASKS_FOLDER, TASK_NAME, SETUPS_DIR, WEEK_DATE_FORMAT, PDF_FONT

# By default:
# Uses ISO 8601 timestamp with week date format
# Uses '-' instead of ':' for supported file naming
# Example: 2025-W29-5T13-42-06
def _get_timestamp(week_date_format=WEEK_DATE_FORMAT):
    now = datetime.datetime.now()
    if week_date_format:
        iso_year, iso_week, iso_weekday = now.isocalendar()
        time_str = now.strftime("%H-%M-%S")
        datetime_stamp = f"{iso_year}-W{iso_week}-{iso_weekday}T{time_str}"
    else:
        datetime_stamp = now.strftime("%Y-%m-%dT%H-%H-%M-%S")
    return datetime_stamp

def _create_folder(folder_dir=TASKS_FOLDER):
    try:
        os.makedirs(folder_dir, exist_ok=True)
    except OSError as e:
        print(f"Error creating folder: {e}")

def _create_md(content, file_name):
    with open(file_name, 'w') as file:
        for line in content:
            file.write(line + '\n') 

def _create_pdf(md_file_path, pdf_file_path):
    create_pdf_command = [
        "pandoc",
        md_file_path,
        "-o", pdf_file_path,
        "--pdf-engine=xelatex",  # use Unicode-compatible engine
        "-V", "documentclass=extarticle",  # allows larger font sizes
        "-V", "fontsize=17pt",  # Supports only default font-sizes: 10pt, 11pt, 12pt, 14pt, 17pt, 20pt
        "-V", "geometry=margin=1.5cm",
        "-V", "papersize=a4",
        "-V", "pagestyle=empty", # to remove page numbers
        "--variable", f"mainfont={PDF_FONT}"
    ]
    try:
        subprocess.run(create_pdf_command, check=True)
        print(f"PDF created: {pdf_file_path}")
    except subprocess.CalledProcessError:
        print("Error: Pandoc conversion failed.")

def _open_file(file_path):
    open_pdf_command = [
        "open",
        file_path
        ]
    try:
        subprocess.run(open_pdf_command, check=True)
    except subprocess.CalledProcessError:
        print("Error: Could not open file")

def _delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"Deleted: {file_path}")
    except FileNotFoundError:
        print("Error: File not found.")
    except OSError as e:
        print(f"Error deleting file: {e}")
      
def _reveal_file(file_path):
    try:
        subprocess.run(["open", "-R", file_path], check=True)
    except OSError as e:
        print(f"Error: Could not reveal file in Finder")
            
def create_files( #TODO: Split into smaller functions. Move some to main.py
    content: list[str],
    file_name: str = TASK_NAME,
    keep_md: bool = False,
    auto_open: bool = False,
    auto_reveal: bool = False,
    ):
    """Creates a Markdown and PDF file with the given content, optionally opens or reveals it"""
    _create_folder() # Create tasks folder
    
    timestamp = _get_timestamp()
    md_file_path = f"{TASKS_FOLDER}/{file_name}_{timestamp}.md"
    pdf_file_path = f"{TASKS_FOLDER}/{file_name}_{timestamp}.pdf"
    
    _create_md(content, md_file_path)
    _create_pdf(md_file_path, pdf_file_path)
    
    if not keep_md:
        _delete_file(md_file_path)
    
    if auto_open:
        _open_file(pdf_file_path)
    
    if auto_reveal:
        _reveal_file(pdf_file_path)

def get_setups() -> dict[str, list[str]]:
    """Return dictionary mapping setup categories to their .json files."""
    setups = {}

    # List all items in the parent folder
    all_items = sorted(os.listdir(SETUPS_DIR)) # all_items = ['setup1.json', 'addition']

    # Separate files and folders
    files = [f for f in all_items if os.path.isfile(os.path.join(SETUPS_DIR, f)) and f.endswith('.json')]
    folders = [d for d in all_items if os.path.isdir(os.path.join(SETUPS_DIR, d))]

    # Add files in setups
    if files:
        setups['NO_CATEGORY'] = files

    # Add files in each category folder
    for folder in folders:
        folder_path = os.path.join(SETUPS_DIR, folder)
        child_files = sorted([f for f in os.listdir(folder_path) if f.endswith('.json')])
        if child_files:
            setups[folder] = child_files

    return setups