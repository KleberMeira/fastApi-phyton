from fastapi import FastAPI

app = FastAPI()

cursos = {
    1: {
        "titulo": "Programação",
        "aulas": 10,
        "horas": 58
    },
    2: {
        "titulo": "Estrutura de dados",
        "aulas": 50,
        "horas": 80
    }
}
@app.get('/cursos')
async def get_cursos():
    return cursos

@app.get('/curso/{curso_id}')
async  def get_curso(curso_id: int):
    curso = cursos[curso_id]
    curso.update({"id": curso_id})
    return curso


if __name__ == 'main':
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1",
                port=8000, log_level="info", reload=True)


