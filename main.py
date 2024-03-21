from fastapi import FastAPI

app = FastAPI()

@app.get('/matvey_pidar')
async def matvey():
    return "МАТВЕЙ ПИДАР И САСЕТ ХУЙ!!!! ЗНАЙТЕ ВСЕ! И НИКТО К ТЕБЕ НА ФАН ВСТРЕЧУ НЕ ПРИДЕТ ПАТАМУШТА ТЫ ТУПА СКУФЯРА СКУФАНОИДОВИЧ"
