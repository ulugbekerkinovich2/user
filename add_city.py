import math
import time

import pandas as pd

data = []


def get_uni():
    sheet_name = 'Лист1'
    df = pd.read_excel('C:/Users/ulugbek/Downloads/Telegram Desktop/State university directions (2)1.xlsx',
                       sheet_name=sheet_name)
    data = df.values
    for j in range(len(data)):
        print(data[j])
        # uni_name = data[j][0]
        # city = data[j][1]


# get_uni()


def maktabk_manzillar():
    sheet_name1 = 'Лист1'
    df1 = pd.read_excel('C:/Users/ulugbek/Downloads/Telegram Desktop/State university directions (2)1.xlsx',
                        sheet_name=sheet_name1)

    sheet_name = 'Sheet1'
    df = pd.read_excel('C:/Users/ulugbek/Downloads/Telegram Desktop/State university directions (2)1.xlsx',
                       sheet_name=sheet_name)
    data = df.values
    data1 = df1.values
    # print(data)
    # print(data1)
    # time.sleep(5000)
    new_data = []
    for j in range(len(data1)):
        uni_name = data1[j][0]
        city = data1[j][1]
        leng = len(data)
        for i in range(leng):
            obj = {
                'Shahar': city, 'Universitet': uni_name
            }
            if not math.isnan(data[i][2]):
                new_data.append(obj)
                leng -= 1
            if math.isnan(data[i][2]):
                print(math.isnan(data[i][2]))
                obj = {
                    'Shahar': math.nan, 'Universitet': math.nan
                }
                new_data.append(obj)
                leng -= 1
                break
    # print(obj)

    new_df = pd.DataFrame(new_data)
    new_df.to_excel('asdasdad.xlsx', index=False)


maktabk_manzillar()
