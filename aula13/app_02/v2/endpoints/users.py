from fastapi import APIRouter, status, Response, JSONResponse


UserRouter = APIRouter()

@UserRouter.get("/{uid}")
def get_users(uid:int):
    data = {user_id: uid, version: 2}
    return JSONResponse(status_code=status.HTTP_200_OK, content=data)