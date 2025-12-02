from fastapi import APIRouter, status, Response, JSONResponse


UserRouter = APIRouter()

@UserRouter.get("/{uid}")
def get_users(uid:int):
    data = {user_id: uid, version: 1}
    return JSONResponse(status_code=status.HTTP_200_OK, content=data)


"""
@UserRouter.get("/users/{uid}", status_code=status.HTTP_200_OK)
def get_users(uid:int):
    return {'uid': uid, 'name': name}
    return Response(status_code=status.HTTP_200_OK)

@UserRouter.post("/users", status_code=status.HTTP_201_CREATED)
def create_users():
    return {'uid': uid, 'name': name}
    return Response(status_code=status.HTTP_201_CREATED)

@UserRouter.patch("/users/{uid}", status_code=status.HTTP_200_OK)
def update_users(uid:int):
    return {'uid': uid, 'name': name}
    return Response(status_code=status.HTTP_200_OK)

@UserRouter.put("/users/{uid}", status_code=status.HTTP_200_OK)
def update_users(uid:int):
    return {'uid': uid, 'name': name}
    return Response(status_code=status.HTTP_200_OK)

@UserRouter.delete("/users/{uid}", status_code=status.HTTP_204_NO_CONTENT)
def delete_users(uid:int):
    return {'uid': uid, 'name': name}
    return Response(status_code=status.HTTP_204_NO_CONTENT)

"""