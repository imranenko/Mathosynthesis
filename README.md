# Mathosynthesis Project

Mathosynthesis is a Python-based tool that generates mathematical tasks as PDF files. It uses JSON setup files to define the tasks and LaTeX to natively generate high-quality, perfectly formatted worksheets. The project supports multiple languages and offers customizable options for generating worksheets.

## Prerequisites

Before running the project, ensure you have the following installed:

- **Python 3.10+**
- **TeX Live / MacTeX**: Required for compiling LaTeX to PDF (`xelatex`).

### Installing LaTeX (xelatex)

- **Windows**: Install [MiKTeX](https://miktex.org/download) or [TeX Live](https://www.tug.org/texlive/).
- **macOS**: `brew install --cask mactex`
- **Linux (Debian/Ubuntu)**: `sudo apt-get install texlive-xetex`

## Installation

1.  Clone the repository or download the source code.
2.  Create a virtual environment and activate it.
3.  Install the required Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4.  Install the project in editable mode (this installs the `mathos` CLI command):

    ```bash
    pip install -e .
    ```

## Usage

Run the script using the installed CLI command:

```bash
mathos
```
You will see a list of available setup files. Enter the number corresponding to the setup you want to generate.

### Command-Line Arguments

- `--setup`, `-s`: Specify the name or number of the JSON setup file (e.g., `1` or `basic_operations.json`).
- `--open`, `-o`: Open the generated PDF file after creation.
- `--file`, `-f`: Reveal the generated PDF file in the system file manager (Finder/Explorer).
- `--latex`, `-tex`: Keep the intermediate LaTeX (`.tex`) source file after PDF creation.
- `--language`, `-lang`: Specify one or more languages for the generated tasks (e.g., `en`, `de`).

**Examples:**

Generate tasks using setup 1 and open the PDF:
```bash
mathos -s 1 --open
```

Generate tasks in Ukrainian, keeping the LaTeX source file:
```bash
mathos -lang uk --latex
```

## Project Structure

- `main.py`: The entry point of the application.
- `config/`: Configuration files and default settings.
- `generators/`: Logic for generating different types of mathematical problems.
- `handlers/`: Helper modules for file handling, CLI parsing, and generation logic.
- `setups/`: JSON files defining the structure and content of task sheets.
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
                "...": { "range": [1, 9, 1] },
                "...": { "choices": [1, 3, 5, 7] }
            }
        }
    ]
}
```

- **`id`**: Supported operation types:
  - `addition`,
  - `subtraction`,
  - `multiplication`,
  - `multiplication_with_round_numbers`
  - `division`,
  - `exponentiation`,
  - `logarithm`,
  - `root`.
- **`description`** (optional): Title or instructions for this specific mathematical block in various languages.
- **`columns`** (optional): Number of columns to layout the tasks.
- **`settings`**: Configuration for random number generation. Always requires `amount` for the number of tasks.


### Operation Settings Reference
In the `settings` object, you can specify ranges for the components of each operation type. The ranges are provided as `{"range": [min, max]}`.

- **Addition (`addition`)**
  - `summand1`: Configuration for the first number.
  - `summand2`: Configuration for the second number.

- **Subtraction (`subtraction`)**
  - `minuend`: Configuration for the initial number in the subtraction.
  - `subtrahend`: Configuration for the number to be subtracted.

- **Multiplication (`multiplication`)**
  - `factor1`: Configuration for the first multiplier.
  - `factor2`: Configuration for the second multiplier.

- **Multiplication with round numbers (`multiplication_with_round_numbers`)**
  - `factor1`: Configuration for the first multiplier.
  - `factor2`: Configuration for the second multiplier.
  - `ten_power1`: Configuration for the power of 10 of 1st number
  - `ten_power2`: Configuration for the power of 10 of 2nd number

- **Division (`division`)**
  - `divisor`: Configuration for the dividing number.
  - `quotient`: Configuration for the resulting whole number answer.

- **Exponentiation (`exponentiation`)**
  - `base`: Configuration for the base number.
  - `exponent`: Configuration for the exponent (power).
- **Logarithm (`logarithm`)**
  - `base`: Configuration for the base of the logarithm.
  - `log`: Configuration for the value of the logarithm (result).

- **Root (`root`)**
  - `root`: Configuration for the solution/root value.
  - `index`: Configuration for the root degree (e.g., 2 for a square root).

## Supported Languages

- English (en)
- German (de)
- Ukrainian (uk)

You can extend the supported languages by modifying the configuration and ensuring your JSON setup files include the necessary translations.