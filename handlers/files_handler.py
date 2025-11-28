import os
import subprocess
import datetime
import logging
from pathlib import Path

from config import TASKS_DIR, SETUPS_DIR, WEEK_DATE_FORMAT, PDF_FONT

logger = logging.getLogger(__name__)

def _get_timestamp(week_date_format: bool = WEEK_DATE_FORMAT) -> str:
    """
    Return the current timestamp as a formatted string.

    Args:
        week_date_format: If True, return ISO week date format (YYYY-Www-DTHH-MM-SS).
                          If False, return standard datetime format (YYYY-MM-DDTHH-MM-SS).

    Returns:
        A string representing the current date and time in the specified format.
    """
    now = datetime.datetime.now()
    if week_date_format:
        iso_year, iso_week, iso_weekday = now.isocalendar()
        time_str = now.strftime("%H-%M-%S")
        datetime_stamp = f"{iso_year}-W{iso_week}-{iso_weekday}T{time_str}"
    else:
        datetime_stamp = now.strftime("%Y-%m-%dT%H-%M-%S")
    return datetime_stamp

def create_folder(folder_dir: str | Path) -> None:
    """
    Create a folder at the specified path, including any necessary parent directories.

    Args:
        folder_dir: Path to the folder to create.

    Logs an error if folder creation fails.
    """
    try:
        os.makedirs(folder_dir, exist_ok=True)
    except OSError as e:
        logger.error(f"Couldn't create folder: {e}")

def create_md(content: list[str], file_name: str | Path) -> None:
    """
    Write a list of strings to a Markdown file, each string as a separate line.

    Args:
        content: List of lines to write.
        file_name: Path to the Markdown file to create.
    """
    with open(file_name, 'w') as file:
        for line in content:
            file.write(line + '\n')

def create_pdf(md_file_path: str | Path, pdf_file_path: str | Path) -> None:
    """
    Convert a Markdown file to a PDF using Pandoc and XeLaTeX.

    Args:
        md_file_path: Path to the source Markdown file.
        pdf_file_path: Path where the generated PDF will be saved.

    Logs success or failure of the conversion process.
    """  
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
        logger.info(f"PDF created: {pdf_file_path}")
    except subprocess.CalledProcessError:
        logger.error("Pandoc conversion failed!")

def open_file(file_path: str | Path) -> None:
    """
    Open a file with the default application (macOS 'open' command).

    Args:
        file_path: Path to the file to open.

    Logs an error if the file cannot be opened.
    """ 
    open_pdf_command = [
        "open",
        file_path
        ]
    try:
        subprocess.run(open_pdf_command, check=True)
    except subprocess.CalledProcessError as e:
        logger.error(f"Could not open file: {e}")

def delete_file(file_path: str | Path) -> None:
    """
    Delete the specified file from the filesystem.

    Args:
        file_path: Path to the file to delete.

    Logs success or failure of the deletion operation.
    """
    try:
        os.remove(file_path)
        logger.info(f"Deleted: {file_path}")
    except FileNotFoundError:
        logger.error("File not found!")
    except OSError as e:
        logger.error(f"Couldn't delete file: {e}")
      
def reveal_file(file_path: str | Path) -> None:
    """
    Reveal the specified file in macOS Finder.

    Args:
        file_path: Path to the file to reveal.

    Logs an error if the file cannot be revealed.
    """
    try:
        subprocess.run(["open", "-R", file_path], check=True)
    except OSError as e:
        logger.error(f"Could not reveal file in Finder: {e}")
     
def get_base_path(file_name: str) -> Path:
    """
    Generate a base file path inside the TASKS_DIR with a timestamp suffix.

    Args:
        file_name: Base name for the file or folder.

    Returns:
        A Path object combining TASKS_DIR, file_name, and a timestamp.
    """
    timestamp = _get_timestamp()
    path = Path(f"{TASKS_DIR}/{file_name}_{timestamp}")
    return path

def get_setups() -> dict[str, list[str]] | None:
    """
    Retrieve all JSON setup files organized by category from SETUPS_DIR.

    Returns:
        A dictionary mapping category names to lists of JSON filenames.
        Includes a 'NO_CATEGORY' key for files directly inside SETUPS_DIR.
        Returns None if no setup files are found.

    Logs an error if no setups are found.
    """
    setups: dict[str, list[str]] = {}

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
    
    if not setups:
        logger.error("No setups found!")
        return None

    return setups