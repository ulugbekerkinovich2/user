import json
import time
import requests

BOT_TOKEN = '5971062170:AAHefPLb-ktSiQXEDybGTGR-cIqn9KRePEE'
GROUP_CHAT_ID = '935920479'
import json
import time
import requests
from bs4 import BeautifulSoup


def telebots(mess):
    requests.get(
        url=f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={GROUP_CHAT_ID}&parse_mode=HTML&text={mess}")


def telebot(mess, image_url):
    send_message_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"

    # Prepare the payload
    payload = {
        'chat_id': GROUP_CHAT_ID,
        'caption': mess,
        'parse_mode': 'HTML',
    }

    # Attach the image file
    files = {'photo': open(image_url, 'rb')}

    # Send the message with image
    response = requests.post(send_message_url, data=payload, files=files)
    print(response.json())


image_url = 'C:/Users/ulugbek/PycharmProjects/mentalaba/datas/mentalaba_rasm.jpg'

file_path = 'C:/Users/ulugbek/Downloads/namangan2.json'

with open(file_path, 'r', encoding='utf-8-sig') as file:
    json_data = json.load(file)

data = json_data
# data = json.dumps(data, indent=4)
for obj in data:
    name = obj['Namangan viloyati']
    telegram = obj['telegram']
    sayt = obj['sayt']
    print(name, telegram, sayt)
    message = f"""<p>📚 Abituriyentlar va maktab bitiruvchilari diqqatiga!</p>
    <br/>
    <p>Oʻz kelajagingiz yoʻlida keyingi qadamni qoʻyishga tayyormisiz❓</p>
    <br/>
    <p><a href="{telegram}">Mentalaba.uz</a> eng nufuzli taʼlim muassasalariga hujjat topshirishning oson va qulay usulini taqdim etadi hamda orzularingizga erishishingizga yordam beradi.</p>
    <br/>
    <p>Ariza topshirishning murakkab tartibi haqida unuting. <a href="{sayt}">Mentalaba.uz</a> sayti orqali oʻnlab oliygohlarga bir zumda hujjat topshiring va muvaffaqiyatli talabalar qatoriga qoʻshiling!</p>
    <br/>
    <p>Nimani kutyapsiz? 🤔 Hoziroq ariza topshiring va yorqin kelajagingiz sari yoʻl oching!</p>
    <br/>
    <p>Taʼlim boʻyicha qaynoq yangiliklar bilan <a href="{telegram}">Men talaba</a> telegram kanalida tanishib borish mumkin.</p>
    <br/>
    <p><a href="{telegram}">Telegram</a> | <a href="{sayt}">Sayt</a></p>
    """

    # Remove unsupported tags
    soup = BeautifulSoup(message, 'html.parser')
    for unsupported_tag in soup.find_all(['br', 'p']):
        unsupported_tag.unwrap()
    message = soup.get_text().strip()

    telebot(message, image_url)
    time.sleep(1)
    telebots(name)
    text = '______________________'
    telebots(text)
    break
