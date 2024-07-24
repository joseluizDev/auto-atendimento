from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from fastapi import FastAPI

app = FastAPI()

mensagens = [
    "Bom dia",
]


def enviar_mensagem_de_amor():
    mensagem = mensagens[datetime.now().day % len(mensagens)]
    print(mensagem)


scheduler = BackgroundScheduler()
scheduler.add_job(enviar_mensagem_de_amor, 'cron', hour=14, minute=8)
scheduler.start()


@app.get("/")
def read_root():
    return {"message": "API de Mensagens de Amor"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
