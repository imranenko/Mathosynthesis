import subprocess
import datetime
import os

from config import FILE_PATH

def get_timestamp():
    # Uses ISO 8601 timestamp with week date format
    week_timestamp = datetime.datetime.now().strftime("%Y-W%W-%uT%H:%M:%S")
    return week_timestamp


def create_md(content, file_name):
    with open(file_name, 'w') as file:
        for task in content:
            file.write(task)

def create_pdf(md_file_path, pdf_file_path, open_pdf=False):
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

    if open_pdf:
        open_file_command = [
            "open",
            "-a", "Preview",
            pdf_file_path
            ]
        try:
            subprocess.run(open_file_command, check=True)
        except subprocess.CalledProcessError:
            print("Error: PDF file open failed.")


def create_files(content, file_path=FILE_PATH):
    timestamp = get_timestamp()
    md_file_path = f"{file_path}_{timestamp}.md"
    pdf_file_path = f"{file_path}_{timestamp}.pdf"
    
    create_md(content, md_file_path)
    create_pdf(md_file_path, pdf_file_path)
