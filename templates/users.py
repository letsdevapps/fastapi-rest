from fastapi import APIRouter

router = APIRouter(prefix="/users")

@router.get("/")
def index():
    #return []
    return '----- FastAPI Rest | Users -----'