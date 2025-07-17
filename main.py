from generators.addition import *
from generators.subtraction import *
from generators.multiplication import *
from generators.division import *

from files_handler import *

from config import OUTPUT_FILE_PATH_WITH_TIMESTAMP

if __name__ == "__main__":
    
    tasks = []
    
    tasks += [Addition.generate_task((100, 1000), (100, 1000)) for _ in  range (5)]
    tasks += "\n"

    tasks += [Subtraction.generate_task((100, 1000), (100, 1000), only_pos=True) for _ in range(5)]
    tasks += "\n"
    
    tasks += [Multiplication.generate_task((5, 9), (21, 29)) for _ in range(5)]
    tasks += "\n"
    
    tasks += [Division.generate_task((5, 9), (21, 29)) for _ in range(5)]


    md_file_path = OUTPUT_FILE_PATH_WITH_TIMESTAMP + '.md'
    pdf_file_path = OUTPUT_FILE_PATH_WITH_TIMESTAMP + '.pdf'
    
    # Save the tasks to a markdown file
    save_md(tasks, output_path=md_file_path)
    
    # Convert the markdown file to PDF
    md_to_pdf(
        input_path=md_file_path,
        output_path=pdf_file_path
        )