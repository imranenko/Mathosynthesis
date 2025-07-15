from generators.addition import *
from generators.multiplication import *
from files_handler import *

from config import OUTPUT_FILE_PATH_WITH_TIMESTAMP


if __name__ == "__main__":
    
    tasks = []
    
    tasks += [generate_addition_task((100, 1000), (100, 1000)) for i in  range (10)]
    tasks += "\n"
    tasks += [generate_multiplication_task((5, 9), (21, 29)) for i in range(10)]


    md_file_path = OUTPUT_FILE_PATH_WITH_TIMESTAMP + '.md'
    pdf_file_path = OUTPUT_FILE_PATH_WITH_TIMESTAMP + '.pdf'
    
    # Save the tasks to a markdown file
    save_md(tasks, output_path=md_file_path)
    
    # Convert the markdown file to PDF
    md_to_pdf(
        input_path=md_file_path,
        output_path=pdf_file_path
        )