import json
import time

file_path = 'last_data3.json'

with open(file_path, 'r', encoding='utf-8-sig') as file:
    json_data = json.load(file)

data = json_data


# for j in i.items():
# if value == '':
#     break
# print(key, value, 'bu--')

# if j[1] == '' and j[0] == 'Yo\'nalish kodi':
#     print('finded ✅')
#     time.sleep(5)
#     continue
# if j[0] == "Yo'nalish kodi" and j[1] != '':
#     if j[0] == "Kunduzgi ta'lim" and j[1] == '1':
#         print('worked ✅✅✅')
# print(j)
# time.sleep(0.22)

def return_id(name_uz, uni_id):
    file_path = 'uni_id_direction_id.json'

    with open(file_path, 'r', encoding='utf-8-sig') as file:
        json_data = json.load(file)

    direction_id = None  # Initialize direction_id with None

    for i in json_data:
        name = i['name_uz']
        univer_id = i['uni_id']
        if name == name_uz and univer_id == uni_id:
            direction_id = i['id']
            break

    return direction_id


array = []


def add_object(**kwargs):
    obj = {
        "direction_id": int(kwargs["direction_id"]),
        "id_number": kwargs["yonalish_kodi"],
        "education_type_id": kwargs["education_type_id"],
        "education_language_id": kwargs["education_language_id"],
        "grant": kwargs["grant"],
        "contract": kwargs["contract"],
        "grant_quota": kwargs['grant_quota'],
        "contract_quota": kwargs['contract_quota']

    }
    array.append(obj)


for i in data:
    university_id = i['Universities']
    yonalish_kodi = i["Yo'nalish kodi"]
    talim_yonalish = i["Tal'lim yo'nalishi"]
    kunduzgi_ozbek = i['Kunduzgi o\'zbek ta\'lim']
    kunduzgi_rus = i["Kunduzgi rus ta'lim"]
    kunduzgi_turkman = i["Kunduzgi turkman ta'lim"]
    kunduzgi_qozoq = i["Kunduzgi qozoq ta'lim"]
    kunduzgi_qoraqalpoq = i["Kunduzgi qoraqalpoq ta'lim"]
    kunduzgi_qirgiz = i["Kunduzgi qirg'iz ta'lim"]
    kunduzgi_tojik = i["Kunduzgi tojik ta'lim"]
    sirtqi_ozbek = i["Sirtqi o'zbek ta'lim"]
    sirtqi_rus = i["Sirtqi rus ta'lim"]
    sirtqi_turkman = i["Sirtqi turkman ta'lim"]
    sirtqi_qozoq = i["Sirtqi qozoq ta'lim"]
    sirtqi_qoraqalpoq = i["Sirtqi qoraqalpoq ta'lim"]
    sirtqi_tojik = i["Sirtqi tojik ta'lim"]
    kechki_ozbek = i["Kechki o'zbek ta'lim"]
    kechki_rus = i["Kechki rus ta'lim"]
    kechki_qoraqalpoq = i["Kechki qoraqalpoq ta'lim"]
    kechki_tojik = i["Kechki tojik ta'lim"]
    masofaviy_ozbek = i["Masofaviy o'zbek ta'lim"]
    masofaviy_rus = i["Masofaviy rus ta'lim"]
    masofaviy_qoraqalpoq = i["Masofaviy qoraqalpoq ta'lim"]
    kunduzgi_ozbek_qabul = i["Kunduzgi o'zbek qabul"]
    kunduzgi_rus_qabul = i["Kunduzgi rus qabul"]
    kunduzgi_turkman_qabul = i["Kunduzgi turkman qabul"]
    kunduzgi_qozoq_qabul = i["Kunduzgi qozoq qabul"]
    kunduzgi_qirgiz_qabul = i["Kunduzgi qirg'iz qabul"]
    kunduzgi_qoraqalpoq_qabul = i["Kunduzgi qoraqalpoq qabul"]
    kunduzgi_tojik_qabul = i["Kunduzgi tojik qabul"]
    sirtqi_ozbek_qabul = i["Sirtqi o'zbek qabul"]
    sirtqi_rus_qabul = i["Sirtqi rus qabul"]
    sirtqi_turkman_qabul = i["Sirtqi turkman qabul"]
    sirtqi_qozoq_qabul = i["Sirtqi qozoq qabul"]
    sirtqi_qoraqalpoq_qabul = i["Sirtqi qoraqalpoq qabul"]
    sirtqi_tojik_qabul = i["Sirtqi tojik qabul"]
    kechki_ozbek_qabul = i["Kechki o'zbek qabul"]
    kechki_rus_qabul = i["Kechki rus qabul"]
    kechki_qoraqalpoq_qabul = i["Kechki qoraqalpoq qabul"]
    kechki_tojik_qabul = i["Kechki tojik qabul"]
    masofaviy_ozbek_qabul = i["Masofaviy o'zbek qabul"]
    masofaviy_rus_qabul = i["Masofaviy rus qabul"]
    masofaviy_qoraqalpoq_qabul = i["Masofaviy qoraqalpoq qabul"]
    kunduzgi_ozbek_grand = i["Kunduzgi o'zbek grand"]
    kunduzgi_rus_grand = i["Kunduzgi rus grand"]
    kunduzgi_turkman_grand = i["Kunduzgi turkman grand"]
    kunduzgi_qozoq_grand = i["Kunduzgi qozoq grand"]
    kunduzgi_qirgiz_grand = i["Kunduzgi qirg'iz grand"]
    kunduzgi_qoraqalpoq_grand = i['Kunduzgi qoraqalpoq grand']
    kunduzgi_tojik_grand = i["Kunduzgi tojik grand"]
    kunduzgi_ozbek_kontrakt = i["Kunduzgi o'zbek kontrakt"]
    kunduzgi_rus_kontrakt = i["Kunduzgi rus kontrakt"]
    kunduzgi_turkman_kontrakt = i["Kunduzgi turkman kontrakt"]
    kunduzgi_qozoq_kontrakt = i["Kuduzgi qozoq kontrakt"]
    kunduzgi_qirgiz_kontrakt = i["Kunduzgi qirg'iz kontrakt"]
    kunduzgi_qoraqalpoq_kontrakt = i["Kunduzgi qoraqalpoq kontrakt"]
    kunduzgi_tojik_kontrakt = i["Kunduzgi tojik kontrakt"]
    sirtqi_ozbek_kontrakt = i["Sirtqi o'zbek kontrakt"]
    sirtqi_rus_kontrakt = i["Sirtqi rus kontrakt"]
    sirtqi_qozoq_kontrakt = i["Sirtqi qozoq kontrakt"]
    sirtqi_qoraqalpoq_kontrakt = i["Sirtqi qoraqalpoq kontrakt"]
    sirtqi_tojik_kontrakt = i["Sirtqi tojik kontrakt"]
    kechki_ozbek_kontrakt = i["Kechki o'zbek kontrakt"]
    kechki_rus_kontrakt = i["Kechki rus kontrakt"]
    kechki_tojik_kontrakt = i["Kechki tojik kontrakt"]
    masofaviy_ozbek_kontrakt = i["Masofaviy o'zbek kontrakt"]
    masofaviy_rus_kontrakt = i["Masofaviy rus kontrakt"]
    masofaviy_qoraqalpoq_kontrakt = i["Masofaviy qoraqalpoq kontrakt"]

    direction_id = return_id(talim_yonalish, university_id)
    if direction_id is not None:
        if kunduzgi_ozbek:
            edu_type = int(str(kunduzgi_ozbek).split(",")[0].strip())
            edu_lang = int(str(kunduzgi_ozbek).split(",")[1].strip())
            grant_quota = int(str(kunduzgi_ozbek_qabul).split("/")[0].strip())
            kontrakt_quota = int(str(kunduzgi_ozbek_qabul).split("/")[1].strip())
            if kunduzgi_ozbek_grand != '-':
                grant = float(kunduzgi_ozbek_grand)
            else:
                grant = ''
            if kunduzgi_ozbek_kontrakt != '-':
                kontrakt = float(kunduzgi_ozbek_kontrakt)
            else:
                kontrakt = ''
            add_object(direction_id=direction_id, yonalish_kodi=yonalish_kodi,
                       education_type_id=edu_type, education_language_id=edu_lang,
                       grant=grant, contract=kontrakt,
                       grant_quota=grant_quota, contract_quota=kontrakt_quota)
        if kunduzgi_rus:
            edu_type = int(str(kunduzgi_rus).split(",")[0].strip())
            edu_lang = int(str(kunduzgi_rus).split(",")[1].strip())
            grand_quota = int(str(kunduzgi_rus_qabul).split("/")[0].strip())
            kontrakt_quota = int(str(kunduzgi_rus_qabul).split("/")[1].strip())
            if kunduzgi_rus_grand != '-':
                grant = float(kunduzgi_rus_grand)
            else:
                grant = ''
            if kunduzgi_rus_kontrakt != '-':
                kontrakt = float(kunduzgi_rus_kontrakt)
            else:
                kontrakt = ''
            add_object(direction_id=direction_id, yonalish_kodi=yonalish_kodi,
                       education_type_id=edu_type, education_language_id=edu_lang,
                       grant=grant, contract=kontrakt,
                       grant_quota=grand_quota, contract_quota=kontrakt_quota)
            if kunduzgi_turkman:
                edu_type = int(str(kunduzgi_turkman).split(",")[0].strip())
                edu_lang = int(str(kunduzgi_turkman).split(",")[1].strip())
                grand_quota = int(str(kunduzgi_turkman_qabul).split("/")[0].strip())
                kontrakt_quota = int(str(kunduzgi_turkman_qabul).split("/")[1].strip())
                if kunduzgi_turkman_grand != '-':
                    grant = float(kunduzgi_turkman_grand)
                else:
                    grant = ''
                if kunduzgi_turkman_kontrakt != '-':
                    kontrakt = float(kunduzgi_turkman_kontrakt)
                else:
                    kontrakt = ''
                add_object(direction_id=direction_id, yonalish_kodi=yonalish_kodi,
                           education_type_id=edu_type, education_language_id=edu_lang,
                           grant=grant, contract=kontrakt,
                           grant_quota=grand_quota, contract_quota=kontrakt_quota)
            if kunduzgi_qozoq:
                edu_type = int(str(kunduzgi_qozoq).split(",")[0].strip())
                edu_lang = int(str(kunduzgi_qozoq).split(",")[1].strip())
                grand_quota = int(str(kunduzgi_qozoq_qabul).split("/")[0].strip())
                kontrakt_quota = int(str(kunduzgi_qozoq_qabul).split("/")[1].strip())
                if kunduzgi_qozoq_grand != '-':
                    grant = float(kunduzgi_qozoq_grand)
                else:
                    grant = ''
                if kunduzgi_qozoq_kontrakt != '-':
                    kontrakt = float(kunduzgi_qozoq_kontrakt)
                else:
                    kontrakt = ''
                add_object(direction_id=direction_id, yonalish_kodi=yonalish_kodi,
                           education_type_id=edu_type, education_language_id=edu_lang,
                           grant=grant, contract=kontrakt,
                           grant_quota=grand_quota, contract_quota=kontrakt_quota)
            if kunduzgi_qoraqalpoq:
                edu_type = int(str(kunduzgi_qoraqalpoq).split(",")[0].strip())
                edu_lang = int(str(kunduzgi_qoraqalpoq).split(",")[1].strip())
                grand_quota = int(str(kunduzgi_qoraqalpoq_qabul).split("/")[0].strip())
                kontrakt_quota = int(str(kunduzgi_qoraqalpoq_qabul).split("/")[1].strip())
                if kunduzgi_qoraqalpoq_grand != '-':
                    grant = float(kunduzgi_qoraqalpoq_grand)
                else:
                    grant = ''
                if kunduzgi_qoraqalpoq_kontrakt != '-':
                    kontrakt = float(kunduzgi_qoraqalpoq_kontrakt)
                else:
                    kontrakt = ''
                add_object(direction_id=direction_id, yonalish_kodi=yonalish_kodi,
                           education_type_id=edu_type, education_language_id=edu_lang,
                           grant=grant, contract=kontrakt,
                           grant_quota=grand_quota, contract_quota=kontrakt_quota)
            if kunduzgi_qirgiz:
                edu_type = int(str(kunduzgi_qirgiz).split(",")[0].strip())
                edu_lang = int(str(kunduzgi_qirgiz).split(",")[1].strip())
                grand_quota = int(str(kunduzgi_qirgiz_qabul).split("/")[0].strip())
                kontrakt_quota = int(str(kunduzgi_qirgiz_qabul).split("/")[1].strip())
                if kunduzgi_qirgiz_grand != '-':
                    grant = float(kunduzgi_qirgiz_grand)
                else:
                    grant = ''
                if kunduzgi_qirgiz_kontrakt != '-':
                    kontrakt = float(kunduzgi_qirgiz_kontrakt)
                else:
                    kontrakt = ''
                add_object(direction_id=direction_id, yonalish_kodi=yonalish_kodi,
                           education_type_id=edu_type, education_language_id=edu_lang,
                           grant=grant, contract=kontrakt,
                           grant_quota=grand_quota, contract_quota=kontrakt_quota)
            if kunduzgi_tojik:
                edu_type = int(str(kunduzgi_tojik).split(",")[0].strip())
                edu_lang = int(str(kunduzgi_tojik).split(",")[1].strip())
                grand_quota = int(str(kunduzgi_tojik_qabul).split("/")[0].strip())
                kontrakt_quota = int(str(kunduzgi_tojik_qabul).split("/")[1].strip())
                if kunduzgi_tojik_grand != '-':
                    grant = float(kunduzgi_tojik_grand)
                else:
                    grant = ''
                if kunduzgi_tojik_kontrakt != '-':
                    kontrakt = float(kunduzgi_tojik_kontrakt)
                else:
                    kontrakt = ''
                add_object(direction_id=direction_id, yonalish_kodi=yonalish_kodi,
                           education_type_id=edu_type, education_language_id=edu_lang,
                           grant=grant, contract=kontrakt,
                           grant_quota=grand_quota, contract_quota=kontrakt_quota)
            if sirtqi_ozbek:
                edu_type = int(str(sirtqi_ozbek).split(",")[0].strip())
                edu_lang = int(str(sirtqi_ozbek).split(",")[1].strip())
                grand_quota = int(str(sirtqi_ozbek_qabul).split("/")[0].strip())
                kontrakt_quota = int(str(sirtqi_ozbek_qabul).split("/")[1].strip())
                grand = ''
                if sirtqi_ozbek_kontrakt != '-':
                    kontrakt = float(sirtqi_ozbek_kontrakt)
                else:
                    kontrakt = ''
                add_object(direction_id=direction_id, yonalish_kodi=yonalish_kodi,
                           education_type_id=edu_type, education_language_id=edu_lang,
                           grant=grand, contract=kontrakt,
                           grant_quota=grand_quota, contract_quota=kontrakt_quota)
            if sirtqi_rus:
                edu_type = int(str(sirtqi_rus).split(",")[0].strip())
                edu_lang = int(str(sirtqi_rus).split(",")[1].strip())
                grand_quota = int(str(sirtqi_rus_qabul).split("/")[0].strip())
                kontrakt_quota = int(str(sirtqi_rus_qabul).split("/")[1].strip())
                grand = ''
                if sirtqi_rus_kontrakt != '-':
                    kontrakt = float(sirtqi_rus_kontrakt)
                else:
                    kontrakt = ''
                add_object(direction_id=direction_id, yonalish_kodi=yonalish_kodi,
                           education_type_id=edu_type, education_language_id=edu_lang,
                           grant=grand, contract=kontrakt,
                           grant_quota=grand_quota, contract_quota=kontrakt_quota)
            if sirtqi_qozoq:
                edu_type = int(str(sirtqi_qozoq).split(",")[0].strip())
                edu_lang = int(str(sirtqi_qozoq).split(",")[1].strip())
                grand_quota = int(str(sirtqi_qozoq_qabul).split("/")[0].strip())
                kontrakt_quota = int(str(sirtqi_qozoq_qabul).split("/")[1].strip())
                grand = ''
                if sirtqi_qozoq_kontrakt != '-':
                    kontrakt = float(sirtqi_qozoq_kontrakt)
                else:
                    kontrakt = ''
                add_object(direction_id=direction_id, yonalish_kodi=yonalish_kodi,
                           education_type_id=edu_type, education_language_id=edu_lang,
                           grant=grand, contract=kontrakt,
                           grant_quota=grand_quota, contract_quota=kontrakt_quota)
            if sirtqi_qoraqalpoq:
                edu_type = int(str(sirtqi_qoraqalpoq).split(",")[0].strip())
                edu_lang = int(str(sirtqi_qoraqalpoq).split(",")[1].strip())
                grand_quota = int(str(sirtqi_qoraqalpoq_qabul).split("/")[0].strip())
                kontrakt_quota = int(str(sirtqi_qoraqalpoq_qabul).split("/")[1].strip())
                grand = ''
                if sirtqi_qoraqalpoq_kontrakt != '-':
                    kontrakt = float(sirtqi_qoraqalpoq_kontrakt)
                else:
                    kontrakt = ''
                add_object(direction_id=direction_id, yonalish_kodi=yonalish_kodi,
                           education_type_id=edu_type, education_language_id=edu_lang,
                           grant=grand, contract=kontrakt,
                           grant_quota=grand_quota, contract_quota=kontrakt_quota)
            if sirtqi_tojik:
                edu_type = int(str(sirtqi_tojik).split(",")[0].strip())
                edu_lang = int(str(sirtqi_tojik).split(",")[1].strip())
                grand_quota = int(str(sirtqi_tojik_qabul).split("/")[0].strip())
                kontrakt_quota = int(str(sirtqi_tojik_qabul).split("/")[1].strip())
                grand = ''
                if sirtqi_tojik_kontrakt != '-':
                    kontrakt = float(sirtqi_tojik_kontrakt)
                else:
                    kontrakt = ''
                add_object(direction_id=direction_id, yonalish_kodi=yonalish_kodi,
                           education_type_id=edu_type, education_language_id=edu_lang,
                           grant=grand, contract=kontrakt,
                           grant_quota=grand_quota, contract_quota=kontrakt_quota)
            if kechki_ozbek:
                edu_type = int(str(kechki_ozbek).split(",")[0].strip())
                edu_lang = int(str(kechki_ozbek).split(",")[1].strip())
                grand_quota = int(str(kechki_ozbek_qabul).split("/")[0].strip())
                kontrakt_quota = int(str(kechki_ozbek_qabul).split("/")[1].strip())
                grand = ''
                if kechki_ozbek_kontrakt != '-':
                    kontrakt = float(kechki_ozbek_kontrakt)
                else:
                    kontrakt = ''
                add_object(direction_id=direction_id, yonalish_kodi=yonalish_kodi,
                           education_type_id=edu_type, education_language_id=edu_lang,
                           grant=grand, contract=kontrakt,
                           grant_quota=grand_quota, contract_quota=kontrakt_quota)
            if kechki_rus:
                edu_type = int(str(kechki_rus).split(",")[0].strip())
                edu_lang = int(str(kechki_rus).split(",")[1].strip())
                grand_quota = int(str(kechki_rus_qabul).split("/")[0].strip())
                kontrakt_quota = int(str(kechki_rus_qabul).split("/")[1].strip())
                grand = ''
                if kechki_rus_kontrakt != '-':
                    kontrakt = float(kechki_rus_kontrakt)
                else:
                    kontrakt = ''
                add_object(direction_id=direction_id, yonalish_kodi=yonalish_kodi,
                           education_type_id=edu_type, education_language_id=edu_lang,
                           grant=grand, contract=kontrakt,
                           grant_quota=grand_quota, contract_quota=kontrakt_quota)
            if kechki_tojik:
                edu_type = int(str(kechki_tojik).split(",")[0].strip())
                edu_lang = int(str(kechki_tojik).split(",")[1].strip())
                grand_quota = int(str(kechki_tojik_qabul).split("/")[0].strip())
                kontrakt_quota = int(str(kechki_tojik_qabul).split("/")[1].strip())
                grand = ''
                if kechki_tojik_kontrakt != '-':
                    kontrakt = float(kechki_tojik_kontrakt)
                else:
                    kontrakt = ''
                add_object(direction_id=direction_id, yonalish_kodi=yonalish_kodi,
                           education_type_id=edu_type, education_language_id=edu_lang,
                           grant=grand, contract=kontrakt,
                           grant_quota=grand_quota, contract_quota=kontrakt_quota)
            if masofaviy_ozbek:
                edu_type = int(str(masofaviy_ozbek).split(",")[0].strip())
                edu_lang = int(str(masofaviy_ozbek).split(",")[1].strip())
                grand_quota = int(str(masofaviy_ozbek_qabul).split("/")[0].strip())
                kontrakt_quota = int(str(masofaviy_ozbek_qabul).split("/")[1].strip())
                grand = ''
                if masofaviy_ozbek_kontrakt != '-':
                    kontrakt = float(masofaviy_ozbek_kontrakt)
                else:
                    kontrakt = ''
                add_object(direction_id=direction_id, yonalish_kodi=yonalish_kodi,
                           education_type_id=edu_type, education_language_id=edu_lang,
                           grant=grand, contract=kontrakt,
                           grant_quota=grand_quota, contract_quota=kontrakt_quota)
            if masofaviy_rus:
                edu_type = int(str(masofaviy_rus).split(",")[0].strip())
                edu_lang = int(str(masofaviy_rus).split(",")[1].strip())
                grand_quota = int(str(masofaviy_rus_qabul).split("/")[0].strip())
                kontrakt_quota = int(str(masofaviy_rus_qabul).split("/")[1].strip())
                grand = ''
                if masofaviy_rus_kontrakt != '-':
                    kontrakt = float(masofaviy_rus_kontrakt)
                else:
                    kontrakt = ''
                add_object(direction_id=direction_id, yonalish_kodi=yonalish_kodi,
                           education_type_id=edu_type, education_language_id=edu_lang,
                           grant=grand, contract=kontrakt,
                           grant_quota=grand_quota, contract_quota=kontrakt_quota)
            if masofaviy_qoraqalpoq:
                edu_type = int(str(masofaviy_qoraqalpoq).split(",")[0].strip())
                edu_lang = int(str(masofaviy_qoraqalpoq).split(",")[1].strip())
                grand_quota = int(str(masofaviy_qoraqalpoq_qabul).split("/")[0].strip())
                kontrakt_quota = int(str(masofaviy_qoraqalpoq_qabul).split("/")[1].strip())
                grand = ''
                if masofaviy_qoraqalpoq_kontrakt != '-':
                    kontrakt = float(masofaviy_qoraqalpoq_kontrakt)
                else:
                    kontrakt = ''
                add_object(direction_id=direction_id, yonalish_kodi=yonalish_kodi,
                           education_type_id=edu_type, education_language_id=edu_lang,
                           grant=grand, contract=kontrakt,
                           grant_quota=grand_quota, contract_quota=kontrakt_quota)

file_path = "result2.json"

with open(file_path, "w") as file:
    json.dump(array, file)
