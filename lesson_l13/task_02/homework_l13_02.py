import json
import  logging

from pathlib import Path

path = Path('/home/mtrykoz/Projects/AQA_course/lesson_l13/task_02/work_with_json')

logging.basicConfig(
        filename="json_Trykoz.log",
        level=logging.ERROR,
        format="%(asctime)s - %(message)s",
        datefmt="%d-%m-%Y %H:%M:%S"
        )

def read_json(files_name):
    with open(files_name, 'r') as file:
        data = json.load(file)
    return data

files_list = [d for d in path.iterdir() if d.is_file()]

for file_name in files_list:
    try:
        read_json(file_name)
    except json.decoder.JSONDecodeError as e:
        logging.error(f"Catch exception: {e} in json file {file_name}")
