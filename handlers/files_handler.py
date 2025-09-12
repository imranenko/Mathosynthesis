import subprocess
import os

import datetime

from config import TASK_PATH, TASKS_FOLDER


# Uses ISO 8601 timestamp with week date format
# Uses '-' instead of ':' for supported file naming
# Example: 2025-W29-5_T13-42-06
def get_timestamp():
    now = datetime.datetime.now()
    iso_year, iso_week, iso_weekday = now.isocalendar()
    time_str = now.strftime("%H-%M-%S")
    return f"{iso_year}-W{iso_week}-{iso_weekday}T{time_str}"


def create_folder(folder_dir=TASKS_FOLDER):
    try:
        os.makedirs(folder_dir, exist_ok=True)
    except OSError as e:
        print(f"Error creating folder: {e}")


def create_md(content, file_name):
    with open(file_name, 'w') as file:
        for line in content:
            file.write(line + '\n')


def create_pdf(md_file_path, pdf_file_path):
    create_pdf_command = [
        "pandoc",
        md_file_path,
        "-o", pdf_file_path,
        "-V", "documentclass=extarticle",    # allows larger font sizes
        "-V", "fontsize=20pt", # 10 or 12pt is common for default
        "-V", "geometry=margin=1.5cm",
        "-V", "papersize=a4",
        "-V", "pagestyle=empty" # to remove page numbers
    ]
    try:
        subprocess.run(create_pdf_command, check=True)
        print(f"PDF created: {pdf_file_path}")
    except subprocess.CalledProcessError:
        print("Error: Pandoc conversion failed.")


def open_file(file_path):
    open_pdf_command = [
        "open",
        file_path
        ]
    try:
        subprocess.run(open_pdf_command, check=True)
    except subprocess.CalledProcessError:
        print("Error: Could not open file")
        
        
def reveal_file(file_path):
    try:
        subprocess.run(["open", "-R", file_path], check=True)
    except OSError as e:
        print(f"Error: Could not reveal file in Finder")
        
        
def create_files(content, file_path=TASK_PATH, auto_open=False, auto_reveal=False):
    create_folder()
    
    timestamp = get_timestamp()
    md_file_path = f"{file_path}_{timestamp}.md"
    pdf_file_path = f"{file_path}_{timestamp}.pdf"
    
    create_md(content, md_file_path)
    create_pdf(md_file_path, pdf_file_path)
    
    if auto_open:
        open_file(pdf_file_path)
    
    if auto_reveal:
        reveal_file(pdf_file_path)


