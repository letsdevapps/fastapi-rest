import requests
from fastapi import APIRouter

BASE_URL = "http://127.0.0.1:8000"

router = APIRouter(prefix="/consume", tags=["Consume API"])

@router.get("/")
@router.get("")
def get_root_message():
    url = f"{BASE_URL}/"
    response = requests.get(url)
    if response.status_code == 200:
        print("Mensagem do root:")
        print(response.json())
        return response.json()
    else:
        print(f"Erro {response.status_code}: {response.text}")
        return response.text

@router.get("/users")
def get_users_index():
    url = f"{BASE_URL}/api/users/"
    response = requests.get(url)
    if response.status_code == 200:
        print("Resposta da API Users:")
        print(response.json())  # Se retornar JSON
        return response.json()
    else:
        print(f"Erro {response.status_code}: {response.text}")
        return response.text

@router.get("/products")
def get_products_index():
    url = f"{BASE_URL}/api/products/"
    response = requests.get(url)
    if response.status_code == 200:
        print("Resposta da API Products`:")
        print(response.json())  # Se retornar JSON
        return response.json()
    else:
        print(f"Erro {response.status_code}: {response.text}")
        return response.text

# if __name__ == "__main__":
#     get_root_message()
#     get_users_index()
#     get_products_index()