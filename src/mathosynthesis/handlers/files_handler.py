import os
import subprocess
import datetime
import logging
import json
from pathlib import Path

from mathosynthesis.config.config import TASKS_DIR, SETUPS_DIR, WEEK_DATE_FORMAT

logger = logging.getLogger(__name__)

# In-memory cache for setup metadata
# Format: { file_path: { "metadata": ..., "mtime": ... } }
_METADATA_CACHE: dict[str, dict] = {}

def _get_metadata(file_path: Path) -> dict:
    """Read metadata from a JSON setup file with caching based on file modification time."""
    global _METADATA_CACHE
    
    try:
        mtime = os.path.getmtime(file_path)
        cached = _METADATA_CACHE.get(str(file_path))
        
        if cached and isinstance(cached, dict) and cached.get("mtime") == mtime:
            return cached.get("metadata", {})
            
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            metadata = data.get("metadata", {})
            _METADATA_CACHE[str(file_path)] = {
                "metadata": metadata,
                "mtime": mtime
            }
            return metadata
    except (json.JSONDecodeError, OSError) as e:
        logger.error(f"Error reading metadata from {file_path}: {e}")
        return {}

def _get_timestamp(week_date_format: bool = WEEK_DATE_FORMAT) -> str:
    """Return the current timestamp in specified format."""
    now = datetime.datetime.now()
    if week_date_format:
        iso_year, iso_week, iso_weekday = now.isocalendar()
        time_str = now.strftime("%H-%M-%S")
        datetime_stamp = f"on {iso_year}-W{iso_week:02d}-{iso_weekday} at {time_str}"
    else:
        datetime_stamp = now.strftime("on %Y-%m-%d at %H-%M-%S")
    return datetime_stamp

def create_folder(folder_dir: str | Path) -> None:
    """Create folder at specified path."""
    try:
        os.makedirs(folder_dir, exist_ok=True)
        logger.info(f"Created folder: {folder_dir}")
    except OSError as e:
        logger.error(f"Couldn't create folder: {e}")

def create_tex(content: str, file_name: str | Path) -> None:
    """Write string content to a LaTeX file."""
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(content)
        logger.info(f"Created LaTeX source: {file_name}")
    except OSError as e:
        logger.error(f"Couldn't create tex file: {e}")

def create_pdf(tex_file_path: str | Path, pdf_file_path: str | Path) -> None:
    """
    Compile a LaTeX file to PDF using xelatex.
    """
    tex_path = Path(tex_file_path)
    output_dir = tex_path.parent
    
    # We run xelatex to compile the PDF
    # -interaction=nonstopmode prevents it from hanging on errors
    command = [
        "xelatex",
        "-interaction=nonstopmode",
        f"-output-directory={output_dir}",
        str(tex_path)
    ]
    
    try:
        # Run xelatex
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        logger.info(f"Created PDF: {pdf_file_path}")
    except subprocess.CalledProcessError as e:
        error_msg = f"LaTeX compilation failed for {tex_path.name}:\n"
        if e.stdout:
            error_msg += f"STDOUT: {e.stdout[-2000:]}\n"
        if e.stderr:
            error_msg += f"STDERR: {e.stderr}\n"
        logger.error(error_msg)
    finally:
        # Always clean up auxiliary LaTeX files
        for ext in [".aux", ".log", ".out"]:
            garbage = tex_path.with_suffix(ext)
            if garbage.exists():
                try:
                    os.remove(garbage)
                except OSError as e:
                    logger.warning(f"Could not delete {garbage.name}: {e}")

def open_file(file_path: str | Path) -> None:
    """Open a file with the default application.""" 
    try:
        subprocess.run(["open", str(file_path)], check=True)
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        logger.error(f"Could not open file: {e}")

def delete_file(file_path: str | Path) -> None:
    """Delete a file from the filesystem."""
    try:
        os.remove(file_path)
        logger.info(f"Deleted: {file_path}")
    except FileNotFoundError:
        logger.error("File not found to delete!")
    except OSError as e:
        logger.error(f"Couldn't delete file: {e}")
      
def reveal_file(file_path: str | Path) -> None:
    """Reveal file in Finder/Explorer."""
    try:
        subprocess.run(["open", "-R", str(file_path)], check=True)
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        logger.error(f"Could not reveal file: {e}")
     
def get_base_path(file_name: str) -> Path:
    """Generate a base file path inside TASKS_DIR with timestamp."""
    timestamp = _get_timestamp()
    return Path(TASKS_DIR) / f"{file_name} {timestamp}"

def get_setups() -> dict[str, list[dict]] | None:
    """
    Retrieve setup files grouped by category.
    Returns: { category: [ {"filename": str, "name": dict, "path": Path}, ... ] }
    """
    setups = {}
    if not SETUPS_DIR.exists():
        logger.error(f"Setups directory not found: {SETUPS_DIR}")
        return None

    all_items = sorted(os.listdir(SETUPS_DIR))
    files = [f for f in all_items if os.path.isfile(SETUPS_DIR / f) and f.endswith('.json')]
    folders = [d for d in all_items if os.path.isdir(SETUPS_DIR / d)]

    if files:
        setups['NO_CATEGORY'] = [
            {
                "filename": f,
                "name": _get_metadata(SETUPS_DIR / f).get("name", {}),
                "path": SETUPS_DIR / f
            }
            for f in files
        ]

    for folder in folders:
        folder_path = SETUPS_DIR / folder
        child_files = sorted([f for f in os.listdir(folder_path) if f.endswith('.json')])
        if child_files:
            setups[folder] = [
                {
                    "filename": f,
                    "name": _get_metadata(folder_path / f).get("name", {}),
                    "path": folder_path / f
                }
                for f in child_files
            ]
    
    if not setups:
        logger.error("No setups found!")
        return None
    return setups

def get_setup_path_by_number(setup_number: int) -> Path:
    """Return path to setup by its 1-based index."""
    setups_dict = get_setups()
    if not setups_dict:
        raise ValueError("No setups available.")

    setups_list = []
    # Use list(setups_dict.keys()) to match display order in CLI
    for category in list(setups_dict.keys()):
        for item in setups_dict[category]:
            setups_list.append(item["path"])

    index = setup_number - 1
    if index < 0 or index >= len(setups_list):
        raise ValueError("Invalid setup number.")

    return setups_list[index]
    
def get_setup_path_by_name(setup_name: str) -> Path:
    """Return path to setup by its name."""
    setups_dict = get_setups()
    if not setups_dict:
        raise ValueError("No setups available.")

    for category, items in setups_dict.items():
        for item in items:
            if item["filename"] == setup_name:
                return item["path"]

    raise ValueError(f"Setup '{setup_name}' not found.")