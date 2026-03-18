# Mathosynthesis Project

Mathosynthesis is a Python-based tool that generates mathematical tasks as PDF files. It uses JSON setup files to define the tasks and Pandoc to convert Markdown to PDF. The project supports multiple languages and offers customizable options for generating worksheets.

## Prerequisites

Before running the project, ensure you have the following installed:

- **Python 3.6+**
- **Pandoc**: Required for converting Markdown to PDF.
- **Lora Font**: Used by default in the generated PDFs.

### Installing Pandoc

- **Windows**: Download the installer from [pandoc.org](https://pandoc.org/installing.html).
- **macOS (Homebrew)**: `brew install pandoc `
- **Linux (Debian/Ubuntu)**: `sudo apt-get install pandoc`

## Installation

1.  Clone the repository or download the source code.
2.  Create a virtual environment and activate it.
3.  Install the required Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4.  Install the project in editable mode:

    ```bash
    pip install -e .
    ```

## Usage

Run the script with:

```bash
python -m mathosynthesis.main
```

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

## JSON Setup Formats

Mathosynthesis uses JSON files in the `setups/` directory to define the mathematical tasks generated. Each file consists of an array of `task_blocks` that determine the type of problems, their settings, and the layout.

### General Structure
A basic JSON setup file looks like this:

```json
{
    "task_blocks": [
        {
            "id": "operation_type",
            "description": {
                "en": "Description in English:",
                "de": "Description in German:",
                "uk": "Description in Ukrainian:"
            },
            "columns": 2,
            "settings": {
                "amount": 10,
                "...": { "range": [1, 9] }
            }
        }
    ]
}
```

- **`id`**: Supported operation types: `addition`, `subtraction`, `multiplication`, `division`, `exponentiation`, `logarithm`, `root`.
- **`description`**: (Optional) Title or instructions for this specific mathematical block in various languages.
- **`columns`**: (Optional) Number of columns to layout the tasks.
- **`settings`**: Configuration for random number generation. Always requires `amount` for the number of tasks.

### Operation Settings Reference
In the `settings` object, you can specify ranges for the components of each operation type. The ranges are provided as `{"range": [min, max]}`.

* **Addition (`addition`)**
  * `summand1`: Configuration for the first number.
  * `summand2`: Configuration for the second number.

* **Subtraction (`subtraction`)**
  * `minuend`: Configuration for the initial number in the subtraction.
  * `subtrahend`: Configuration for the number to be subtracted.

* **Multiplication (`multiplication`)**
  * `factor1`: Configuration for the first multiplier.
  * `factor2`: Configuration for the second multiplier.

* **Division (`division`)**
  * `divisor`: Configuration for the dividing number.
  * `quotient`: Configuration for the resulting whole number answer.

* **Exponentiation (`exponentiation`)**
  * `base`: Configuration for the base number.
  * `exponent`: Configuration for the exponent (power).

* **Logarithm (`logarithm`)**
  * `base`: Configuration for the base of the logarithm.
  * `log`: Configuration for the value of the logarithm (result).

* **Root (`root`)**
  * `root`: Configuration for the solution/root value.
  * `index`: Configuration for the root degree (e.g., 2 for a square root).

## Supported Languages

- English (en)
- German (de)
- Ukrainian (uk)

You can extend the supported languages by modifying the configuration and ensuring your JSON setup files include the necessary translations.