from fastapi import APIRouter

from model.User import User

router = APIRouter(prefix="/api/users", tags=["Users"])


@router.get("/")
def index():
    return {
        "message": "----- FastAPI Rest | Users | Index -----"
    }


@router.post("/")
def create_user(user: User):
    return {
        "message" : "Usuario criado com sucesso",
        "user" : user
    }
