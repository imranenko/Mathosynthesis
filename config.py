from files_handler import get_timestamp

timestamp = get_timestamp()

OUTPUT_FOLDER = "Math Tasks"

OUTPUT_FILENAME = "math_task"
OUTPUT_FILENAME_WITH_TIMESTAMP = f"{OUTPUT_FILENAME}_{timestamp}"

OUTPUT_FILE_PATH_WITH_TIMESTAMP = f"{OUTPUT_FOLDER}/{OUTPUT_FILENAME_WITH_TIMESTAMP}"