import json
import time
import html
import requests

BOT_TOKEN = '5971062170:AAHefPLb-ktSiQXEDybGTGR-cIqn9KRePEE'
GROUP_CHAT_ID = '935920479'


# @uzsupportautobot

def telebo1t(mess):
    requests.get(
        url=f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={GROUP_CHAT_ID}&parse_mode=HTML&text={mess}")


def telebot(mess, image_url):
    send_photo_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    send_message_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    # Send the message
    response = requests.get(send_message_url, params={
        'chat_id': GROUP_CHAT_ID,
        'text': mess
    })

    if response.status_code == 200 and response.json()['ok']:
        # Get the message ID for the image caption
        message_id = response.json()['result']['message_id']

        # Prepare the payload for sending the image
        payload = {
            'chat_id': GROUP_CHAT_ID,
            'caption': '',
            'reply_to_message_id': message_id,
            'parse_mode': 'HTML'
        }

        # Attach the image URL
        files = {
            'photo': image_url
        }

        # Send the image with caption
        response = requests.post(send_photo_url, data=payload, files=files)

        if response.status_code == 200:
            print("Image sent successfully!")
        else:
            print("Failed to send image.")
            print(response.json())
    else:
        print("Failed to send message.")
        print(response.json())


image_url = 'https://example.com/image.jpg'

file_path = 'C:/Users/ulugbek/Downloads/namangan2.json'

with open(file_path, 'r', encoding='utf-8-sig') as file:
    json_data = json.load(file)

data = json_data

for obj in data:
    name = obj['Namangan viloyati']
    telegram = obj['telegram']
    sayt = obj['sayt']
    message = f"""Abituriyentlar va maktab bitiruvchilari diqqatiga!

Oʻz kelajagingiz yoʻlida keyingi qadamni qoʻyishga tayyormisiz?

Mentalaba.uz eng nufuzli taʼlim muassasalariga hujjat topshirishning oson va qulay usulini taqdim etadi hamda orzularingizga erishishingizga yordam beradi.

Ariza topshirishning murakkab tartibi haqida unuting. Mentalaba.uz sayti orqali oʻnlab oliygohlarga bir zumda hujjat topshiring va muvaffaqiyatli talabalar qatoriga qoʻshiling!

Nimani kutyapsiz? Hoziroq ariza topshiring va yorqin kelajagingiz sarilin!

Taʼlim boʻyicha qaynoq yangiliklar bilan Men talaba telegram kanalida tanishib borish mumkin.

Telegram ({telegram}) | Sayt ({sayt})"""

    telebot(message, image_url)
    time.sleep(1)
    break
