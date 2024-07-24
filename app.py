import time
from datetime import datetime

import schedule


def enviar_mensagem_de_amor():
    mensagens = [
        "Bom dia",

    ]
    mensagem = mensagens[datetime.now().day % len(mensagens)]
    print(mensagem)


schedule.every().day.at("14:08").do(enviar_mensagem_de_amor)

while True:
    schedule.run_pending()
    time.sleep(1)
