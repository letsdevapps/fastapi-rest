from fastapi import FastAPI
from api.users_api import router as users_router
from api.products_api import router as products_router
from consume.consume_api import router as consume_router

app = FastAPI()
app.include_router(users_router)
app.include_router(products_router)
app.include_router(consume_router)

@app.get("/")
async def root():
    return {"message": "----- FastAPI Rest | Root -----"}


@app.get("/index/{message}")
async def index_message(message: str):
    return {"message": f"Message: {message}"}
