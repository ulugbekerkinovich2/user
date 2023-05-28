import pandas as pd


def maktab_manzillar():
    sheet_name = 'Sheet1'
    df = pd.read_excel('C:/Users/ulugbek/PycharmProjects/mentalaba/datas/Prezident_maktablari.xlsx',
                       sheet_name=sheet_name)
    data = df.values
    new_data = []
    for i in range(len(data)):
        print(data[i])
        tg1 = f't.me/+{data[i][0]}'
        # tg2 = f't.me/+{data[i][1]}'
        # tg3 = f't.me/+{data[i][2]}'
        # tg4 = f't.me/+{data[i][3]}'
        # print(tg1, tg4, tg3, tg2)
        new_row = {
            'toshkent': tg1,
            # 'buxoro2': tg2,
            # 'buxoro3': tg3,
            # 'buxoro4': tg4
        }
        new_data.append(new_row)
    new_df = pd.DataFrame(new_data)
    new_df.to_excel('toshkent_prezident_maktablari.xlsx', index=False)


maktab_manzillar()


def data_farqi():
    sheet_name = 'Sheet1'
    df = pd.read_excel('C:/Users/ulugbek/PycharmProjects/mentalaba/datas/111dislokatsiya_data.xlsx',
                       sheet_name=sheet_name)
    df_eski = pd.read_excel('C:/Users/ulugbek/Downloads/dislokatsiya_data_eski.xlsx')
    data_eski = df_eski.values
    data = df.values
    new_data = []
    for i in range(len(data_eski)):
        new_data.append(data_eski[i])
        # print(data_eski[i])
    data_farqi = []
    for j in range(len(data)):
        if data[j] not in new_data:
            data_farqi.append(data[j])
            # print(data[j])
    new_df = pd.DataFrame(data_farqi)
    new_df.to_excel('1111yangi_toshkent_data_telegram.xlsx', index=False)

# data_farqi()