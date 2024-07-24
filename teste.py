import random
import time

import openai
import requests

BASE_URL = 'https://server-evolutionapi.uwqcav.easypanel.host'
API_KEY = 'Jr59IRl66nL0sJtq2EmBfQNMVQqwvKyi'
CHAT = 'JoseLuiz'
telefone = '559492883002'
telefone2 = '553299644257'
OPENAI_API_KEY = 'your-openai-api-key'

headers = {
    'Apikey': API_KEY,
}

openai.api_key = OPENAI_API_KEY


def generate_love_message():
    prompt = "gerar mensagem de"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50
    )
    message = response.choices[0].text.strip()
    return message


while True:
    mensagem = generate_love_message()
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

    time.sleep(1200)
