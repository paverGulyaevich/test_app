from fastapi import FastAPI

app = FastAPI()

@app.get('/matvey_pidar')
async def matvey():
    return "МАТВЕЙ ПИДАР И САСЕТ ХУЙ!!!! ЗНАЙТЕ ВСЕ!"
