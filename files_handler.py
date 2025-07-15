import subprocess
import datetime
import os

# Uses ISO 8601 timestamp with week date format
def get_timestamp():
    week_timestamp = datetime.datetime.now().strftime("%Y-W%W-%uT%H:%M:%S")
    return week_timestamp


def save_md(content, output_path):
    with open(output_path, 'w') as file:
        for task in content:
            file.write(task)

def md_to_pdf(input_path, output_path, open_pdf=False):
    create_pdf_command = [
        "pandoc",
        input_path,
        "-o", output_path,
        "-V", "documentclass=extarticle",    # allows larger font sizes
        "-V", "fontsize=20pt", # 10 or 12pt is common for default
        "-V", "geometry=margin=1.5cm",
        "-V", "papersize=a4",
        "-V", "pagestyle=empty" # to remove page numbers
    ]
    try:
        subprocess.run(create_pdf_command, check=True)
        print(f"PDF created: {output_path}")
    except subprocess.CalledProcessError:
        print("Error: Pandoc conversion failed.")

    if open_pdf:
        open_file_command = [
            "open",
            "-a", "Preview",
            input_path
            ]
        try:
            subprocess.run(open_file_command, check=True)
        except subprocess.CalledProcessError:
            print("Error: PDF file open failed.")
