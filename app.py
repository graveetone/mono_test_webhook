from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/webhook")
async def post_test_webhook(body: dict):
    # body = await request.json()
    print(body)
    return {"status": "ok", "body": body}

@app.get("/webhook")
async def get_test_webhook(request: Request):
    print(f"Webhook received aaaaaaaaaaaaaaaaaaaaaa")
