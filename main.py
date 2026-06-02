from fastapi import FastAPI
from templates.users import router as users_router
from templates.products import router as products_router

app = FastAPI()
app.include_router(users_router)
app.include_router(products_router)


@app.get("/")
async def root():
    return {"message": "----- FastAPI Rest | Root -----"}


@app.get("/index/{message}")
async def index_message(message: str):
    return {"message": f"Message: {message}"}
