import json

import openpyxl

# Open an existing workbook
workbook = openpyxl.load_workbook('datas/data-1680063667931.xlsx')

# Select a worksheet by name
worksheet = workbook['da']
datas = []
for i in range(2, 117):
    edu_type_full = worksheet[f'E{i}'].value
    edu_type_part = worksheet[f'F{i}'].value
    edu_type_even = worksheet[f'G{i}'].value
    dir_id = int(worksheet[f'A{i}'].value)
    print(f'{dir_id}---> {edu_type_full}-{edu_type_part}-{edu_type_even}')

    if edu_type_full is not None:
        data = {
            'direction_id': dir_id,
            'education_type_id': 1,
            'local_tuition_fee': edu_type_full
        }
        datas.append(data)
    if edu_type_part is not None:
        data = {
            'direction_id': dir_id,
            'education_type_id': 2,
            'local_tuition_fee': edu_type_part
        }
        datas.append(data)
    if edu_type_even is not None:
        data = {
            'direction_id': dir_id,
            'education_type_id': 3,
            'local_tuition_fee': edu_type_even
        }
        datas.append(data)

with open('datas/json_data1.json', 'w') as f:
    json.dump(datas, f)
