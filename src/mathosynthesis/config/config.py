from pathlib import Path
import os

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent

# Folder absolute paths
DATA_DIR = PROJECT_ROOT / "data"
SETUPS_DIR = DATA_DIR / "setups"
TEMPLATE_DIR = DATA_DIR / "templates"
TASK_SHEET_TEMPLATE = TEMPLATE_DIR / "task_sheet.tex.jinja"
TASKS_DIR = PROJECT_ROOT / "math-tasks"

WEEK_DATE_FORMAT = True

PREFERRED_LANGUAGES = [
    "en",
    "de",
    "uk",
]

PDF_FONT = "Lora"

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOGS_DIR = PROJECT_ROOT / "logs"
LOG_FILE_PATH = LOGS_DIR / "mathosynthesis.log"