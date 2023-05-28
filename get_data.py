import openpyxl

from kontrakt_excell import data_excell

# Open an existing workbook
workbook = openpyxl.load_workbook('datas/State university directions (2).xlsx')

# Select a worksheet by name
worksheet = workbook['Sheet1']
arr = ['tumani', 'shahri', 'viloyati', 'respublikasi']
# Read data from the worksheet
arr_type = []
arr_lang = []
for i in range(2, 6100):
    code = worksheet[f'A{i}'].value
    name = worksheet[f'B{i}'].value

    kunduzgi = worksheet[f'C{i}'].value
    sirtqi = worksheet[f'D{i}'].value
    kechki = worksheet[f'E{i}'].value
    online = worksheet[f'F{i}'].value

    kunduzgi_uz = worksheet[f'G{i}'].value
    kunduzgi_ru = worksheet[f'H{i}'].value
    kunduzgi_turk = worksheet[f'I{i}'].value
    kunduzgi_qozoq = worksheet[f'J{i}'].value
    kunduzgi_qoraqalpoq = worksheet[f'K{i}'].value
    kunduzgi_qirgiz = worksheet[f'L{i}'].value
    kunduzgi_tojik = worksheet[f'M{i}'].value
    sirtqi_uz = worksheet[f'N{i}'].value
    sirtqi_ru = worksheet[f'O{i}'].value
    sirtqi_turk = worksheet[f'P{i}'].value
    sirtqi_qozoq = worksheet[f'Q{i}'].value
    sirtqi_qoraqalpoq = worksheet[f'R{i}'].value
    sirtqi_tojik = worksheet[f'S{i}'].value
    kechki_uz = worksheet[f'T{i}'].value
    kechki_ru = worksheet[f'U{i}'].value
    kechki_qoraqalpoq = worksheet[f'V{i}'].value
    kechki_tojik = worksheet[f'W{i}'].value
    masof_uz = worksheet[f'X{i}'].value
    masof_ru = worksheet[f'Y{i}'].value
    masof_qoraqalpoq = worksheet[f'Z{i}'].value
    kontrakt = data_excell(f'{name}')
    if kunduzgi_uz == '+':
        arr_type.append(1)
    if kunduzgi_ru == '+':
        arr_type.append(1)
    if kunduzgi_turk == '+':
        arr_type.append(1)
    if kunduzgi_qozoq == '+':
        arr_type.append(1)
    if kunduzgi_qoraqalpoq == '+':
        arr_type.append(1)
    if kunduzgi_qirgiz == '+':
        arr_type.append(1)
    if kunduzgi_tojik == '+':
        arr_type.append(1)
    if sirtqi_uz == '+':
        arr_type.append(2)
    if sirtqi_ru == '+':
        arr_type.append(2)
    if sirtqi_turk == '+':
        arr_type.append(2)
    if sirtqi_qozoq == '+':
        arr_type.append(2)
    if sirtqi_qoraqalpoq == '+':
        arr_type.append(2)
    if sirtqi_tojik == '+':
        arr_type.append(2)
    if kechki_uz == '+':
        arr_type.append(3)
    if kechki_ru == '+':
        arr_type.append(3)
    if kechki_qoraqalpoq == '+':
        arr_type.append(3)
    if kechki_tojik == '+':
        arr_type.append(3)
    if masof_uz == '+':
        arr_type.append(4)
    if masof_ru == '+':
        arr_type.append(4)
    if masof_qoraqalpoq == '+':
        arr_type.append(4)

        # or kunduzgi_ru or kunduzgi_qirgiz or kunduzgi_tojik or kunduzgi_qoraqalpoq \
        #    or kunduzgi_turk or kunduzgi_qozoq or kunduzgi_qirgiz or sirtqi_uz or sirtqi_ru or sirtqi_turk or \
        #    sirtqi_qozoq or sirtqi_qoraqalpoq or sirtqi_tojik or kechki_tojik or kechki_ru or kechki_uz or \
        #    kechki_qoraqalpoq or masof_qoraqalpoq or masof_ru or masof_uz == '+':
    arr.append(name)

# try:
#     if any(h in name for h in arr):
#         continue
# except:
#     continue
# if code is None:
#     arr = []
print(arr)
print(f'{code}\n{name}----> {kunduzgi_uz, kunduzgi_uz == "+"}, {kontrakt}')
worksheet['A1'] = 'ID'
worksheet['B1'] = 'Talim yonalish'
worksheet['C1'] = 'Talim tili'
worksheet['A2'] = 'John'
worksheet['B2'] = 25
# worksheet['A3'] = 'Jane'
# worksheet['B3'] = 30
#
# # Save the workbook
# workbook.save('example.xlsx')
