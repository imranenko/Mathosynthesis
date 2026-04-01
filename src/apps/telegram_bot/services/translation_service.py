import json
import os
from pathlib import Path

# Base path for locales
LOCALES_PATH = Path(__file__).resolve().parent.parent / "locales"

# Memory cache for translations
_translations = {}

def load_translations():
    """Load all JSON files from the locales directory."""
    if not LOCALES_PATH.exists():
        return

    for file in os.listdir(LOCALES_PATH):
        if file.endswith(".json"):
            lang_code = file.split(".")[0]
            file_path = LOCALES_PATH / file
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    _translations[lang_code] = json.load(f)
            except Exception as e:
                print(f"Error loading translation file {file}: {e}")

# Initial load
load_translations()

def get_text(key: str, lang_code: str = 'en', **kwargs) -> str:
    """Retrieve localized string by key and language code."""
    # Ensure default fallback to English if language not found
    lang_translations = _translations.get(lang_code, _translations.get('en', {}))
    
    # Get the text or the key if not found in current lang OR English
    text = lang_translations.get(key, _translations.get('en', {}).get(key, key))
    
    if kwargs:
        try:
            return text.format(**kwargs)
        except (KeyError, ValueError, IndexError):
            return text
    return text
