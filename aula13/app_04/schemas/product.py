from pydantic import BaseModel

class ProductShema(BaseModel):
     name: str
     price: float
     description: str | None = None