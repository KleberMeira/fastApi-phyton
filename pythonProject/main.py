from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from time import sleep
from fastapi import Depends

from routes import curso_route
from routes import usuario_route

app = FastAPI()
app.include_router(curso_route.router, tags=['cursos'])
app.include_router(usuario_route.router, tags=['usuarios'])


if __name__ == 'main':
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1",
                port=8000, log_level="info", reload=True)