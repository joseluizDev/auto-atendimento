import random
import time

import requests

from mensagens import mensagens_de_amor

BASE_URL = 'https://server-evolutionapi.uwqcav.easypanel.host'
API_KEY = 'Jr59IRl66nL0sJtq2EmBfQNMVQqwvKyi'
CHAT = 'JoseLuiz'
telefone = '5522981484436'
telefone2 = '553299644257'
telefone3 = '5511963866977'
headers = {
    'Apikey': API_KEY,
}

while True:
    mensagem = random.choice(mensagens_de_amor)
    print(mensagem)
    body = {
        "number": f"{telefone}@s.whatsapp.net",
        "textMessage": {
            "text": f"{mensagem.replace('\n', '\\n')}"
        },
        "options": {
            "delay": 1200,
            "presence": "composing"
        }
    }
    body2 = {
        "number": f"{telefone2}@s.whatsapp.net",
        "textMessage": {
            "text": f"{mensagem.replace('\n', '\\n')}"
        },
        "options": {
            "delay": 1200,
            "presence": "composing"
        }
    }
    body3 = {
        "number": f"{telefone3}@s.whatsapp.net",
        "textMessage": {
            "text": f"{mensagem.replace('\n', '\\n')}"
        },
        "options": {
            "delay": 1200,
            "presence": "composing"
        }
    }

    response = requests.post(
        f'{BASE_URL}/message/sendText/{CHAT}',
        json=body,
        headers=headers,
    )

    response = requests.post(
        f'{BASE_URL}/message/sendText/{CHAT}',
        json=body2,
        headers=headers,
    )

    response = requests.post(
        f'{BASE_URL}/message/sendText/{CHAT}',
        json=body3,
        headers=headers,
    )

    print(response.json())

    time.sleep(600)
