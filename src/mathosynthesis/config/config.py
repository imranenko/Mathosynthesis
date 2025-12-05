from pathlib import Path

# File and Folder names
TASKS_DIR = "math-tasks"
SETUPS_DIR = Path(__file__).resolve().parent.parent / "setups"

# TASK_NAME = "math-task"


# Default settings
AUTO_OPEN_FILE = False
AUTO_REVEAL_FILE = False
KEEP_MD_FILE = False

WEEK_DATE_FORMAT = True

PREFERRED_LANGUAGES = [
    "en",
    "de",
    "uk",
    ]

PDF_FONT = "Lora"

LOG_LEVEL = "INFO"
LOG_FILE_PATH = Path("logs/mathosynthesis.log")