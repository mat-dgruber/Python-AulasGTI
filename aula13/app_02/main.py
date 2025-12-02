from fastapi import FastAPI
from api.v1.router import api_router as v1_api_router
from api.v2.router import api_router as v2_api_router


app = FastAPI()

app.include_router(v1_api_router, prefix="/api/v1")
app.include_router(v2_api_router, prefix="/api/v2")