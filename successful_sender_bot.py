import json
import time

import requests
import html

BOT_TOKEN = '5971062170:AAHefPLb-ktSiQXEDybGTGR-cIqn9KRePEE'
GROUP_CHAT_ID = '935920479'


def telebots(mess):
    requests.get(
        url=f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={GROUP_CHAT_ID}&parse_mode=HTML&text={mess}")


def telebot(mess, image_path=None):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"

    if image_path is None:
        # Send a regular text message
        params = {
            'chat_id': GROUP_CHAT_ID,
            'parse_mode': 'HTML',
            'text': html.unescape(mess)
        }
        response = requests.get(url, params=params)
    else:
        # Send an image with caption
        caption = f'{html.unescape(mess)}'
        files = {
            'photo': open(image_path, 'rb')
        }
        data = {
            'chat_id': GROUP_CHAT_ID,
            'caption': caption,
            'parse_mode': 'HTML'
        }
        response = requests.post(url, data=data, files=files)

    if response.status_code == 200:
        print("Image sent successfully!")
    else:
        print("Failed to send image.")


image_path = 'C:/Users/ulugbek/PycharmProjects/mentalaba/datas/mentalaba_rasm.jpg'
file_path = 'C:/Users/ulugbek/Downloads/namangan_latest.json'

with open(file_path, 'r', encoding='utf-8-sig') as file:
    json_data = json.load(file)

data = json_data

for obj in data:
    name = obj["Namangan viloyati"]
    telegram = obj['telegram']
    sayt = obj['sayt']
    mess = f"""
📚 Abituriyentlar va maktab bitiruvchilari diqqatiga!
    
Oʻz kelajagingiz yoʻlida keyingi qadamni qoʻyishga tayyormisiz❓
    
<a href="{telegram}">Mentalaba.uz</a> eng nufuzli taʼlim muassasalariga hujjat topshirishning oson va qulay usulini taqdim etadi hamda orzularingizga erishishingizga yordam beradi.
    
Ariza topshirishning murakkab tartibi haqida unuting. <a href="{sayt}">Mentalaba.uz</a> sayti orqali oʻnlab oliygohlarga bir zumda hujjat topshiring va muvaffaqiyatli talabalar qatoriga qoʻshiling!
    
Nimani kutyapsiz? 🤔 Hoziroq ariza topshiring va yorqin kelajagingiz sari yoʻl oching!
    
Taʼlim boʻyicha qaynoq yangiliklar bilan <a href="{telegram}">Men talaba</a> telegram kanalida tanishib borish mumkin.
    
<a href="{telegram}">Telegram</a> | <a href="{sayt}">Sayt</a>
    """

    telebot(mess, image_path)
    telebots(name)
    telebots('______________________')
    time.sleep(3)
