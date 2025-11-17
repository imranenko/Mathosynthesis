import subprocess
import os

import datetime

from config import TASKS_DIR, SETUPS_DIR, WEEK_DATE_FORMAT, PDF_FONT

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

def create_folder(folder_dir):
    try:
        os.makedirs(folder_dir, exist_ok=True)
    except OSError as e:
        print(f"Error creating folder: {e}")

def create_md(content, file_name):
    with open(file_name, 'w') as file:
        for line in content:
            file.write(line + '\n') 

def create_pdf(md_file_path, pdf_file_path):
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

def open_file(file_path):
    open_pdf_command = [
        "open",
        file_path
        ]
    try:
        subprocess.run(open_pdf_command, check=True)
    except subprocess.CalledProcessError:
        print("Error: Could not open file")

def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"Deleted: {file_path}")
    except FileNotFoundError:
        print("Error: File not found.")
    except OSError as e:
        print(f"Error deleting file: {e}")
      
def reveal_file(file_path):
    try:
        subprocess.run(["open", "-R", file_path], check=True)
    except OSError as e:
        print(f"Error: Could not reveal file in Finder")
     
def get_base_path(file_name):
    timestamp = _get_timestamp()
    return f"{TASKS_DIR}/{file_name}_{timestamp}"

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