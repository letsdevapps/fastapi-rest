# FastAPI Rest

## Pycharm

Projeto criado com o Pycharm no Ubuntu, Isso instala a versão Community (gratuita)

    sudo snap install pycharm-community --classic
    
    pycharm-community

Se quiser a versão Professional

    sudo snap install pycharm-professional --classic

    pycharm-professional

### Ambiente Virtual (venv)

Pycharm cria o ambiente virtual automaticamente em novos projetos

    python -m venv .venv

Lembre-se de ativar para usar

    source .venv/bin/activate

Para sair

    deactivate

### Requirements

Export

    source .venv/bin/activate

    pip freeze > requirements.txt

Import
    
    source .venv/bin/activate

    pip install -r requirements.txt

## Run

Projeto simples, http://127.0.0.1:8000

    uvicorn main:app

Modo desenvolvimento (auto reload)

    uvicorn main:app --reload

Com ambiente virtual

    source .venv/bin/activate
    uvicorn main:app --reload

Executando como módulo Python (Reload). Reinicia o servidor automaticamente quando o código muda. Mostra tracebacks detalhados dos erros no terminal.

    python -m uvicorn main:app --reload

Documentação

    http://127.0.0.1:8000/docs
    http://127.0.0.1:8000/redoc

Desenvolvimento

    uvicorn main:app --reload

Acessível na rede local

    uvicorn main:app --host 0.0.0.0 --port 8000 --reload

Porta customizada

    uvicorn main:app --port 5000 --reload