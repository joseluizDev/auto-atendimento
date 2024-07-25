from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()


class WebhookData(BaseModel):
    key: str


@app.post("/webhook")
async def webhook():

    return {"status": "sucesso", "message": "Webhook recebido!"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
