from fastapi import APIRouter, status, Response

router = APIRouter()

@router.get("/users/{uid}", status_code=status.HTTP_200_OK)
def get_users(uid:int):
    return {'uid': uid, 'name': name}
    return Response(status_code=status.HTTP_200_OK)

@router.post("/users", status_code=status.HTTP_201_CREATED)
def create_users():
    return {'uid': uid, 'name': name}
    return Response(status_code=status.HTTP_201_CREATED)

@router.patch("/users/{uid}", status_code=status.HTTP_200_OK)
def update_users(uid:int):
    return {'uid': uid, 'name': name}
    return Response(status_code=status.HTTP_200_OK)

@router.put("/users/{uid}", status_code=status.HTTP_200_OK)
def update_users(uid:int):
    return {'uid': uid, 'name': name}
    return Response(status_code=status.HTTP_200_OK)

@router.delete("/orders/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_orders(id:int):
    return {'id': id}
    return Response(status_code=status.HTTP_204_NO_CONTENT)