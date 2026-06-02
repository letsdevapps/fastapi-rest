from fastapi import APIRouter

router = APIRouter(prefix="/products")

@router.get("/")
def index():
    #return []
    return '----- FastAPI Rest | Products -----'