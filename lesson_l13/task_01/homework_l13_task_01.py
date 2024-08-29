import csv

from pathlib import Path

path = Path('/home/mtrykoz/Projects/AQA_course/lesson_l13/task_01')


def read_csv_file_to_list(file_name):
    data_list: list = []
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        for data_row in reader:
            data_list.append('; '.join(list(data_row)))
    return data_list, header

def write_list_to_csv_file(input_list, list_header):
    with open(f'{path}/result_Trykoz.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(list_header)
        writer.writerow(input_list)

_, header_csv = read_csv_file_to_list(f"{path}/work_with_csv/r-m-c.csv")
first_data_list, _ = read_csv_file_to_list(f"{path}/work_with_csv/r-m-c.csv")
second_data_list, _ = read_csv_file_to_list(f"{path}/work_with_csv/rmc.csv")

result = list(set(first_data_list) ^ set(second_data_list))

write_list_to_csv_file(result, header_csv)
