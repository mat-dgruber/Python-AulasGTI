from fastapi import FastAPI
from api.v1.endpoints.products import router as ProductRouter
from api.v1.endpoints.atividade import router as AtividadeRouter

app = FastAPI()

app.include_router(ProductRouter, prefix="/products")
app.include_router(AtividadeRouter, prefix="/atividade")