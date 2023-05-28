import re
import time

import pandas as pd


def maktabk_manzillar():
    sheet_name = 'Тош вил'
    df = pd.read_excel('C:/Users/ulugbek/Downloads/Telegram Desktop/Dislokatsiya.xlsx', sheet_name=sheet_name)
    data = df.values
    new_data = []
    for i in range(len(data)):
        num_id = str(data[i][0])
        hudud = str(data[i][1])  # Corrected column index
        tuman = str(data[i][2])  # Corrected column index
        maktab_raqam = str(data[i][3])  # Corrected column index
        olis_hudud = str(data[i][4])  # Corrected column index
        mfy = str(data[i][5])  # Corrected column index
        manzili = str(data[i][6])  # Corrected column index
        inn = str(data[i][7])  # Corrected column index
        name = str(data[i][8])  # Corrected column index
        raqam = str(data[i][9])
        if raqam is not None:
            raqamlar = raqam.replace('(', '').replace(')', '').replace('-', '').replace(' ', '').replace('  ',
                                                                                                         '').replace(
                '.', '').replace(',', '').replace('/', '')
            if not raqamlar.startswith('998'):
                raqamlar = f'998{raqamlar}'
            if '998+' in raqamlar:
                raqamlar = raqamlar.split('+')[1]
            if 'nan' in raqamlar or len(raqamlar) < 9:
                continue
            if len(raqamlar) >= 14:
                raqamlar = raqamlar.split(',')[0]
            if len(raqamlar) > 14:
                raqamlar = ''.join(list(raqamlar)[:12])
            if len(raqamlar) < 12:
                continue
            print(raqamlar)
        # time.sleep(0.2)
        row_data = {
            # 'Num_ID': num_id,
            # 'Hudud_Nomi': hudud,
            # 'Tuman_Shahar_Nomi': tuman,
            # 'Maktab_Raqami': maktab_raqam,
            # 'Joylashgan_Hudud': olis_hudud,
            # 'MFY_Nomi': mfy,
            # 'Manzili': manzili,
            # 'INN': inn,
            # 'Maktab_drektorining_FISH': name,
            'Telefon_Raqam': raqamlar
        }
        new_data.append(row_data)

    new_df = pd.DataFrame(new_data)
    new_df.to_excel('1New_Maktab_Manzillar.xlsx', index=False)


# maktabk_manzillar()

def buxoro_manzillar():
    new_data = []
    for i in range(1, 9):
        sheet_name = 'барча ПТМ'
        df = pd.read_excel('C:/Users/ulugbek/PycharmProjects/mentalaba/datas/navoiy_raqamlar.xlsx',
                           sheet_name=sheet_name)
        data = df.values
        print(len(data))
        for i in range(len(data)):
            num_id = str(data[i][0])
            hudu_nomi = str(data[i][1])
            maktab_raqami = str(data[i][2])
            name_ceo = str(data[i][3])
            name_ceo_number = str(data[i][4])
            # name_ceo_1 = str(data[i][5])
            # name_ceo_1_number = str(data[i][6])
            # name_ceo_2 = str(data[i][7])
            # name_ceo_2_number = str(data[i][8])
            # name_ceo_3 = str(data[i][9])
            # name_ceo_3_number = str(data[i][10])
            # if 'nan' in name_ceo_number or name_ceo_1_number or name_ceo_2_number or name_ceo_3_number:
            #     continue
            # if name_ceo_2.startswith('+998') or name_ceo_1_number.startswith(
            #         '+998') or name_ceo_2_number.startswith(
            #     '+998') or name_ceo_3_number.startswith('+998') or name_ceo_2.startswith(
            #     '998') or name_ceo_1_number.startswith('998') \
            #         or name_ceo_2_number.startswith('998') or name_ceo_3_number.startswith('998'):
            #     continue
            if name_ceo_number.startswith('+998') or name_ceo_number.startswith('998'):
                name_ceo_number = name_ceo_number.replace('+', '')
            name_ceo_number = name_ceo_number.replace('(', '').replace(')', '').replace('-', '').replace(' ',
                                                                                                         '').replace(
                '  ',
                '').replace(
                '.', '').replace(',', '').replace('/', '')

            # name_ceo_1_number = name_ceo_1_number.replace('(', '').replace(')', '').replace('-', '').replace(' ',
            #                                                                                                  '').replace(
            #     '  ',
            #     '').replace(
            #     '.', '').replace(',', '').replace('/', '')
            # name_ceo_2_number = name_ceo_2_number.replace('(', '').replace(')', '').replace('-', '').replace(' ',
            #                                                                                                    '').replace(
            #     '  ',
            #     '').replace(
            #     '.', '').replace(',', '').replace('/', '')
            # name_ceo_3_number = name_ceo_3_number.replace('(', '').replace(')', '').replace('-', '').replace(' ',
            #                                                                                                  '').replace(
            #     '  ',
            #     '').replace(
            #     '.', '').replace(',', '').replace('/', '')

            name_ceo_number = re.sub(r'[\(\)\- ]', '', name_ceo_number)
            name_ceo_number = re.sub(r'\.', '', name_ceo_number)
            if not name_ceo_number.startswith('998'):
                name_ceo_number = f'998{name_ceo_number}'

            # name_ceo_1_number = re.sub(r'[\(\)\- ]', '', name_ceo_1_number)
            # name_ceo_1_number = f'998{name_ceo_1_number}'
            # name_ceo_1_number = re.sub(r'\.', '', name_ceo_1_number)
            #
            # name_ceo_2_number = re.sub(r'[\(\)\- ]', '', name_ceo_2_number)
            # name_ceo_2_number = f'998{name_ceo_2_number}'
            # name_ceo_2_number = re.sub(r'\.', '', name_ceo_2_number)
            #
            # name_ceo_3_number = re.sub(r'[\(\)\- ]', '', name_ceo_3_number)
            # name_ceo_3_number = f'998{name_ceo_3_number}'
            # name_ceo_3_number = re.sub(r'\.', '', name_ceo_3_number)

            # print(name_ceo_number, name_ceo_1_number, name_ceo_2_number, name_ceo_3_number)
            row_data = {
                'number4': name_ceo_number,
                # 'number1': name_ceo_2_number,
                # 'number2': name_ceo_1_number,
                # 'number3': name_ceo_number,
            }
            new_data.append(row_data)
    new_df = pd.DataFrame(new_data)
    new_df.to_excel('navoiy_data.xlsx', index=False)


# buxoro_manzillar()


def dislokatsiya():
    sheet_name = 'Тош вил'
    df = pd.read_excel('C:/Users/ulugbek/Downloads/Dislokatsiya.xlsx', sheet_name=sheet_name)
    data = df.values
    new_data = []

    for i in range(len(data)):
        # try:
        #     # print(data[i])
        nomer = str(data[i][7]).replace('-', '').replace('.', '').replace('/', '').replace(' ', '').replace('+', '')
        #     # if ',' in nomer:
        #     #     nomer = nomer.split(',')[0]
        #
        #     print(nomer, data[i][7])
        #     obj = {
        #         'number': nomer
        #     }
        #     new_data.append(obj)
        # except:
        #     print(nomer, 'shu nomer', data[i][7])
        #     obj = {
        #         'number': nomer
        #     }
        #     new_data.append(obj)
        if nomer.startswith('+998'):
            nomer = len(nomer.replace('+998', ''))
            if nomer == 9:
                nomer = str(data[i][7]).replace('-', '').replace('.', '').replace('/', '').replace(' ', '').replace('+',
                                                                                                                    '')
                nomer = nomer.replace('+', '')
                obj = {
                    'nomer': nomer
                }
                new_data.append(obj)

        if len(nomer) == 9:
            nomer = f'998{nomer}'
            obj = {
                'number': nomer
            }
            new_data.append(obj)

        if len(nomer) == 8:
            nomer = str(data[i][7]).replace('-', '').replace('.', '').replace('/', '').replace(' ', '').replace('+', '')
            nomer = f'9989{nomer}'
            obj = {
                'number': nomer
            }
            new_data.append(obj)
        nomer = str(data[i][7]).replace('-', '').replace('.', '').replace('/', '').replace(' ', '').replace('+', '')
        if nomer.startswith('998'):
            nomer = nomer.replace('998', '')
            if len(nomer) == 8:
                nomer = data[i][7].replace('-', '').replace('.', '').replace('/', '').replace(' ', '').replace('+', '')
                nomer = f'9989{nomer}'

                obj = {
                    'number': nomer
                }
                new_data.append(obj)

        nomer = str(data[i][7]).replace('-', '').replace('.', '').replace('/', '').replace(' ', '').replace('+', '')
        if nomer.startswith('998'):
            nomer = nomer.replace('998', '')
            if len(nomer) == 9:
                nomer = data[i][7].replace('-', '').replace('.', '').replace('/', '').replace(' ', '').replace('+', '')

                obj = {
                    'number': nomer
                }
                new_data.append(obj)
    new_df = pd.DataFrame(new_data)
    new_df.to_excel('111dislokatsiya_data.xlsx', index=False)


# dislokatsiya()
def qashqadaryo():
    datas = []
    for i in range(1, 80):
        sheet_name = f'Table {i}'
        file_path = 'C://Users/ulugbek/Downloads/Qashqadaryo_.xlsx'  # Update with your file path
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        data = df.values
        for j in range(len(data)):
            a = data[j]
            for k in range(1, 16):
                try:
                    n = a[k]
                    obj = {f'n{k}': n}
                    datas.append(obj)
                except IndexError:
                    print(f'n{k} yoq ekan')

    new_df1 = pd.DataFrame(datas)
    new_df1.to_excel('qashqadaryo_datas.xlsx', index=False)


# qashqadaryo()

def prezident_maktablari():
    sheet_name = '3-006-0006'
    df = pd.read_excel('C:/Users/ulugbek/Downloads/Telegram Desktop/Prezident matkablari.xlsx', sheet_name=sheet_name)
    data = df.values
    new_data = []

    for i in range(len(data)):
        number_1 = data[i][5]
        number_2 = data[i][6]
        if str(number_1).endswith('71') or str(number_1).endswith('55') or str(number_1).endswith('72') or str(
                number_1).endswith('73'):
            continue
        if len(str(number_2)) < 7:
            continue
        number = f'{number_1}{number_2}'
        new_data.append(number)
    new_df2 = pd.DataFrame(new_data)
    new_df2.to_excel('Prezident_maktablari.xlsx', index=False)


# prezident_maktablari()


def akademik_listey():
    new_data = []
    sheet_name = 'Умумий'
    df = pd.read_excel('C:/Users/ulugbek/Downloads/Telegram Desktop/Директорларни телефони ОТВга.xlsx',
                       sheet_name=sheet_name)
    data = df.values
    for i in range(len(data)):
        number = str(data[i][5]).replace('-', '').replace(' ', '').replace('(', ''). \
            replace(')', '').strip()
        number = f'998{number}'

        if len(number) == 12:
            print(number)
            obj = {
                'number': number
            }
            new_data.append(obj)
        elif len(number) >= 12:
            number = str(number)[:12]
            print(number)
            obj = {
                'number': number
            }
            new_data.append(obj)
    new_df2 = pd.DataFrame(new_data)
    new_df2.to_excel('direktorlar_data1.xlsx', index=False)


akademik_listey()
