from Fastapi import APIRouter
from schemas.product import ProcudtSchema
from schemas.responde import ResponseEnvelope

router = APIRouter()

@router.get('/{id}', response_model=ResponseEnvelope[ProductSchema])
def get_product(id:int):
     product_data = ProdectSchema(id=id, name=f)