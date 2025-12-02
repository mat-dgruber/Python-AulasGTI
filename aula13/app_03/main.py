from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from .core.exceptions import ResorceNotFoundException

app = FastAPI()

async def resoutce_not_found_handler(request: Request, exc: ResorceNotFoundException):
     # RFC 9457
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
          "type": "about:blank",
          "title": "Recurso não encontrado",
          "status": 404,
          "detail": str(exc),
          "instance": request.url.path
        }
    )

async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "type": "about:blank",
            "title": "Erro de Validação",
            "status": 422,
            "detail": exc.errors(),
            "instance": request.url.path
        }
    )

app.add_exception_handler(ResorceNotFoundException, resoutce_not_found_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)

@app.get("/test404")
def test_404():
     raise ResorceNotFoundException("Mochila", 42)