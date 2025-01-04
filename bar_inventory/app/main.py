from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def read_root():
    return {"message": "Добро пожаловать в приложение по барному учету!"}