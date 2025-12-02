from fastapi import FastAPI
from api.v1.endopoints.products import router as product_router

app = FastAPI()

app.include_router(product_router, prefix="products")