from fastapi import APIRouter

from model.Product import Product

router = APIRouter(prefix="/api/products", tags=["Products"])


@router.get("/")
def index():
    return {
        "message": "----- FastAPI Rest | Products | Index -----"
    }


@router.post("/")
def create_product(product: Product):
    return {
        "message": "Produto criado com sucesso",
        "product": product
    }