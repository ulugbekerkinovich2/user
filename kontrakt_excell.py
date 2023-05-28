import json

import pandas as pd
import re


def data_excell(name):
    sheet_name = 'Latest'
    df = pd.read_excel('Universities and directions (4).xlsx', sheet_name=sheet_name)
    # columns = df.columns
    # contract_price = df['contract_price']
    data = df.values
    for i in range(len(data)):
        # print(data[i][1])
        # print(data[i][2])
        if name == data[i][1]:
            return data[i][2]


def name_uz(id):
    sheet_name1 = 'New Directions'
    df = pd.read_excel('Universities and directions (4).xlsx', sheet_name=sheet_name1)
    # columns = df.columns
    # contract_price = df['contract_price']
    data = df.values
    try:
        for i in range(len(data)):
            direction_id = int(data[i][0])
            # print(direction_id)
            # print(data[i][3])
            if id == direction_id:
                return data[i][3]
    except:
        print('tugadi')


# a = name_uz(2000)
# print(a)


# name_uz()


def get_direction_id(name):
    sheet_name = 'Worksheet'
    df = pd.read_excel('data-1679635962239 — копия.xlsx', sheet_name=sheet_name)
    data = df.values
    for i in range(115, len(data)):
        if i == 2440:
            break
        direction_id = data[i][0]
        direction_name = data[i][1]
        # print(direction_id, direction_name)
        if name == direction_name:
            return direction_id


# a = get_direction_id('O‘rmonchilik (o‘rmonchilar va ularning farzandlari uchun)')
# print(a)

def get_direction_type_id1(id):
    sheet_name = 'Latest'
    df = pd.read_excel('Universities and directions (4).xlsx', sheet_name=sheet_name)
    data = df.values
    for i in range(len(data)):
        # print(f'{i, data[i]}\n')
        direction_id1 = data[i][0]
        direction_name1 = data[i][1]
        direction_type_id1 = data[i][5]
        # name2 = direction_name1.replace("‘", '')
        # name1 = name.replace("‘", '')
        if id == int(direction_id1):
            # print(direction_type_id1, direction_name1, direction_id1, 'asdasdasd')
            return direction_type_id1


# a = get_direction_type_id(129, 'Gidrotexnika inshootlari va nasos stansiyalaridan foydalanish')
# print(a)
# b = [int(f) for f in a.split(',')]
# print(b)
try:
    result = []
    sheet_name = 'Worksheet'
    df = pd.read_excel('data-1679635962239.xlsx', sheet_name=sheet_name)
    datas = df.values
    for i in range(0, len(datas) + 1):
        if i == 2440:
            break
        direction_id = datas[i][0]
        direction_name = datas[i][1]
        direction_ru = name_uz(int(direction_id))
        contact_price = data_excell(direction_name)
        direction_type = str(get_direction_type_id1(int(direction_id))).split(',')
        direction_type = ' '.join(map(str, direction_type))
        direction_type = direction_type.split('.')
        direction_type = ' '.join(map(str, direction_type))
        direction_type = direction_type.split(' ')
        # direction_type = str(get_direction_type_id1(int(direction_id))).split(',')
        # direction_type1 = get_direction_type_id1(int(direction_id))
        # print(direction_id)
        # print(direction_name, type(direction_name))
        # print(direction_ru, type(direction_ru))
        # print(contact_price, type(contact_price))
        # print(direction_type, type(direction_type))
        # print(direction_type1, type(direction_type1))
        # if type(direction_type) is float:
        #     direction_type = direction_type[0].replace('.', '')
        #     print(direction_type)
        if len(direction_type) >= 2:
            direction_type = [int(f) for f in direction_type]
            for k in range(len(direction_type)):
                print(k)
                data = {
                    "name_ru": direction_ru,
                    "direction_id": int(direction_id),
                    "education_type_id": int(direction_type[k]),
                    "local_tuition_fee": contact_price
                }
                print('\n')
                print(direction_id, type(direction_id))
                print(direction_name, type(direction_name))
                print(direction_ru, type(direction_ru))
                print(contact_price, type(contact_price))
                print(direction_type[k], type(direction_type))
                result.append(data)
        if len(direction_type) == 1:
            if direction_type[0]:
                print(direction_type[0], 'direction 0')
                data = {
                    "name_ru": direction_ru,
                    "direction_id": int(direction_id),
                    "education_type_id": int(direction_type[0]),
                    "local_tuition_fee": contact_price
                }
                print('\n')
                print(direction_id, type(direction_id))
                print(direction_name, type(direction_name))
                print(direction_ru, type(direction_ru))
                print(contact_price, type(contact_price))
                print(direction_type[0], type(direction_type[0]))
                result.append(data)
        with open('result_1.json', 'w') as outfile:
            json.dump(result, outfile)
except:
    print('tugadi')
