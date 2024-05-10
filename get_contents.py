import os

import openpyxl
from get_excel import read_value

def get_all_file_names(directory='CONTENTS'):
    file_names = []
    items = os.listdir(directory)
    for item in items:
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            file_names.append(item)
    return file_names

def get_content_box():
    file_names = get_all_file_names()
    content_box = {}

    for file_name in file_names:
        file_path = f'CONTENTS/{file_name}'
        workbook = openpyxl.load_workbook(file_path)
        content_type = file_name.split('.')[0]
        content_box[content_type] = []

        a = 1
        while True:
            b = 1
            question = read_value(workbook, a, b)
            if question:
                box = [question]
            else:
                break

            while True:
                b += 1
                answer = read_value(workbook, a, b)
                if answer:
                    box.append(answer)
                else:
                    break
            a += 1

            content_box[content_type].append(box)

    return content_box