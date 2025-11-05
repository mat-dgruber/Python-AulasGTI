from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any, Optional

app = FastAPI()
# Simulação de dados
produtos_db: List[Dict[str, Any]] = [
    {"id": 1, "nome": "caneta esferográfica", "preco": 2.50},
    {"id": 2, "nome": "caderno universitario", "preco": 15.00},
]

# --- NOVO MODELO PYDANTIC ---
# Usamos 'Optional' para indicar que o campo pode ou não estar presente (embora aqui só teremos o preco)
class PrecoUpdate(BaseModel):
    preco: float

@app.patch("/produtos/{produto_id}")
def atualizar_preco_produto(produto_id: int, novos_dados: PrecoUpdate):
    """
    PATCH: Atualiza apenas o preço de um produto existente.
    """
    for i, produto in enumerate(produtos_db):
        if produto["id"] == produto_id:
            produtos_db[i]["preco"] = novos_dados.preco
            return produtos_db[i]

    raise HTTPException(status_code=404, detail="Produto não encontrado")
    

    # **SEU CÓDIGO TERMINA AQUI**

    pass # Substitua o 'pass' pelo seu retorno.