import random
import time

import requests

from mensagens import mensagens_de_amor

BASE_URL = 'https://server-evolutionapi.uwqcav.easypanel.host'
API_KEY = 'Jr59IRl66nL0sJtq2EmBfQNMVQqwvKyi'
CHAT = 'JoseLuiz'
telefone = '559492883002'

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

    response = requests.post(
        f'{BASE_URL}/message/sendText/{CHAT}',
        json=body,
        headers=headers,
    )

    print(response.json())

    time.sleep(600)
