# Mathosynthesis Project

Mathosynthesis is a Python-based tool that generates mathematical tasks as PDF files. It uses JSON setup files to define the tasks and Pandoc to convert Markdown to PDF. The project supports multiple languages and offers customizable options for generating worksheets.

## Prerequisites

Before running the project, ensure you have the following installed:

- **Python 3.6+**
- **Pandoc**: Required for converting Markdown to PDF.
- **Lora Font**: Used by default in the generated PDFs.

### Installing Pandoc

- **macOS (Homebrew)**: `brew install pandoc `
- **Windows**: Download the installer from [pandoc.org](https://pandoc.org/installing.html).
- **Linux (Debian/Ubuntu)**: `sudo apt-get install pandoc`

## Installation

1.  Clone the repository or download the source code.
2.  Install the required Python dependencies: ```pip install -r requirements.txt```

## Usage

Run the script with: ```python main.py ```

You will see a list of available setup files. Enter the number corresponding to the setup you want to generate.

### Command-Line Arguments

- `--setup`, `-s`: Specify the name of the JSON setup file (e.g., `basic_operations.json`).
- `--open`, `-o`: Open the generated PDF file after creation. (Default: `True` if flag is present without value, or pass `true`/`false`).
- `--reveal`, `-r`: Reveal the generated PDF file in the system file manager (Finder/Explorer).
- `--markdown`, `-md`: Keep the intermediate Markdown file after PDF creation.
- `--language`, `-lang`: Specify one or more languages for the generated tasks (e.g., `en`, `de`).

**Examples:**

Generate tasks using `basic_operations.json` and open the PDF:
```
python main.py --setup basic_operations.json --open
```

Generate tasks in Ukrainian, keeping the Markdown file:
```
python main.py --language uk --markdown
```

## Project Structure

- `main.py`: The entry point of the application.
- `config/`: Configuration files and default settings.
- `generators/`: Logic for generating different types of mathematical problems.
- `handlers/`: Helper modules for file handling, CLI parsing, and generation logic.
- `setups/`: JSON files defining the structure and content of task såheets.
- `math-tasks/`: Directory where generated PDF and Markdown files are saved.

## Supported Languages

- English (en)
- German (de)
- Ukrainian (uk)

You can extend the supported languages by modifying the configuration and ensuring your JSON setup files include the necessary translations.